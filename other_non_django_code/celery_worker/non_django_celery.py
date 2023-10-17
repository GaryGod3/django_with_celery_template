from celery import Celery

app = Celery("non_django_celery_worker_app")

app.config_from_object("celery_worker.celery_config")


@app.task
def add_numbers():
    return
