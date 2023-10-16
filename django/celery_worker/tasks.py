from celery import shared_task


@shared_task
def shared_worker_task():
    return
