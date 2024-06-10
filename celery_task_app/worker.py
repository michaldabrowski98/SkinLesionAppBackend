from celery import Celery
import multiprocessing

multiprocessing.set_start_method('spawn', force=True)

BROKER_URI = "amqp://admin:mypass@rabbit:5672"
BACKEND_URI = "rpc://"

app = Celery(
    'celery_task_app',
    broker=BROKER_URI,
    backend=BACKEND_URI,
    include=['celery_task_app.tasks']
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

if __name__ == '__main__':
    app.start()
