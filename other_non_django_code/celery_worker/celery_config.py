import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis_service:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis_service:6379/0")