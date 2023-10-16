import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")


@app.task
def add_numbers():
    return


# Tell Celery to look for tasks in all installed apps for tasks.py
app.autodiscover_tasks()
