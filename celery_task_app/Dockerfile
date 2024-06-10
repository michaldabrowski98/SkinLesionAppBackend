FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/celery_task_app

ENV PYTHONPATH="${PYTHONPATH}:/code/celery_task_app"

CMD ["celery", "-A", "celery_task_app.worker.app", "worker", "--loglevel=info"]

