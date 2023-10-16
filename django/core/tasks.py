from celery import shared_task


@shared_task
def shared_core_task():
    return
