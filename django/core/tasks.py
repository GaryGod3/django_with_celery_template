from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def shared_core_task():
    logger.info("Running shared_core_task")
    return
