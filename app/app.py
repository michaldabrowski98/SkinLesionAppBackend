from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas
import crud
from database import SessionLocal
from celery import Celery


app = FastAPI()

simple_app = Celery('celery_task_app',
                    broker='amqp://admin:mypass@rabbit:5672',
                    backend='rpc://')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/api/start-task')
def call_method(image: schemas.Image):
    r = simple_app.send_task('celery_task_app.tasks.predict_single', kwargs={'image': image.content})
    return {"task_id": r.id}


@app.get('/api/task-status/{task_id}')
def task_status(task_id: str):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    result = status.result
    if status.state == 'FAILURE':
        return {"status": status.state, "result": str(result), "traceback": status.traceback}
    return {"status": status.state, "result": str(result)}


@app.get('/api/task-result/{task_id}')
def task_result(task_id: str, db: Session = Depends(get_db)):
    result = simple_app.AsyncResult(task_id).result
    lesion = crud.get_skin_lesion_by_code(db, result)
    if not lesion:
        raise HTTPException(status_code=404, detail="Result not found")
    return lesion

@app.get('/')
def index():
    return {'message': 'This is skin lesion classification API'}

@app.get('/api/lesions-info')
def lesions_info(db: Session = Depends(get_db)):
    lesions = crud.get_all_skin_lesions(db)
    if lesions is None:
        raise HTTPException(status_code=500, details="Internal server error")
    
    return lesions
