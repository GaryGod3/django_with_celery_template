import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("celery_django_worker_app")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_routes = {
    "core.tasks.shared_core_task": {"queue": "django_queue"},
    "core.tasks.task1_in_beat_definition": {"queue": "django_queue"},
    "core.tasks.task2_in_beat_definition": {"queue": "django_queue"},
    "core.tasks.task_with_args": {"queue": "django_queue"},
    "frontend.tasks.shared_frontend_task": {"queue": "django_queue"},
    "celery_worker.celery.add_numbers": {"queue": "django_queue"},
    "celery_worker.tasks.shared_worker_task": {"queue": "django_queue"},
}


@app.task
def add_numbers():
    return


# Tell Celery to look for tasks in all installed apps for tasks.py
app.autodiscover_tasks()
