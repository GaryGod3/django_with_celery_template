from celery import shared_task
from datetime import timedelta
from celery_worker.celery import app
from celery.schedules import crontab
import logging

logger = logging.getLogger(__name__)

app.conf.beat_schedule = {
    # Periodic Tasks
    "core_task": {
        "task": "core.tasks.shared_core_task",
        "schedule": timedelta(minutes=10),
    },
    "frontend_task": {
        "task": "frontend.tasks.shared_frontend_task",
        "schedule": timedelta(seconds=200),
    },
    "worker_task": {
        "task": "celery_worker.tasks.shared_worker_task",
        "schedule": timedelta(seconds=30),
    },
    "core_app_task_1": {
        "task": "core.tasks.task1_in_beat_definition",
        "schedule": timedelta(hours=2),
    },
    # Crontab tasks
    "crontab_core_task_with_args": {
        "task": "core.tasks.task_with_args",
        # Schedule below is every 10 minutes (between 0-59 minutes of the hour - same as */10),
        # between midnight and 5:59am on mondays  *UTC*
        # "schedule": crontab(minute="0-59/10", hour="0-5", day_of_week="mon"),
        #
        # Be very careful with day names, make sure they are crontab compatible
        # or you'll have to get into the database to change them.
        #
        # Schedule below is every minute between 10 and 12:59 on Thursdays *UTC*
        "schedule": crontab(minute="*/1", hour="10-13", day_of_week="sun"),
        # "kwargs": {"foo": "bar"},  # that's foo = bar
        "args": (1, 2),
        "options": {
            "queue": "django_queue",
            "priory": 5,
        },
    },
}


@app.task()
def task_with_args(a, b, **kwargs):
    logger.info(f"{task_with_args.__name__} started with args: a=%s, b=%s", a, b)
    result = a + b
    logger.info(f"{task_with_args.__name__} finished. Result: %s", result)
    return result


@shared_task
def shared_core_task():
    logger.info("Running shared_core_task")
    return


@app.task()
def task1_in_beat_definition():
    logger.info("Running task 1")
    return


@app.task()
def task2_in_beat_definition():
    logger.info("Running task 2")
    return


"""
+------------- Minute (0 - 59)
| +----------- Hour (0 - 23)
| | +--------- Day of the Month (1 - 31)
| | | +------- Month (1 - 12)
| | | | +----- Day of the Week (0 - 6) (Sunday=0 or 7)
| | | | |
* * * * *
"""

"""
* * * * *       # Run every minute
*/5 * * * *     # Run every 5 minutes
30 * * * *      # Run every hour at 30 minutes past the hour
0 9 * * *       # Run every day at 9 AM
0 14 * * 1      # Run every Monday at 2 PM
0 0 1,15 * *    # Run on the 1st and 15th of each month
0 20,23 * * 5   # Run every Friday at 8 PM and 11 PM
*/15 * * * * *  # Run every 15 seconds (non-standard)
0 0 * * *       # Run every day at midnight
0 12 * * MON    # Run every Monday at 12 PM
0 0 1-7 * *     # Run on the first 7 days of each month
0 0/2 * * *     # Run every 2 hours
0 */6 * * *     # Run every 6 hours
0 0-8/2 * * *   # Run every 2 hours from midnight to 8 AM
0 0,12 * * *    # Run at midnight and noon every day
0 0 * * 0       # Run every Sunday at midnight
0 0 1 1 *       # Run on January 1st every year
0 0 1 1 MON     # Run on the first Monday of January every year
"""
