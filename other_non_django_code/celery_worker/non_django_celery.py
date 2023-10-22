from datetime import timedelta
import logging
from celery import Celery

logger = logging.getLogger(__name__)

app = Celery("non_django_celery_worker_app")

app.config_from_object("celery_worker.celery_config")

app.conf.task_routes = {
    "celery_worker.non_django_celery.add_numbers": {"queue": "non_django_queue"},
}

app.conf.beat_schedule = {
    # Periodic Tasks
    "non_celery_task": {
        "task": "celery_worker.non_django_celery.add_numbers",
        "args": (1, 2),
        "schedule": timedelta(seconds=35),
    }
}


# this shouldn't really be in here, should it?
@app.task
def add_numbers(a, b, **kwargs):
    logger.info(f"{add_numbers.__name__} started with args: a=%s, b=%s", a, b)
    result = a + b
    logger.info(f"{add_numbers.__name__} finished. Result: %s", result)
    return result
