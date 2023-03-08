import time

from calendr.celery import celery_app


@celery_app.task(name="first_task")
def first_task():
    print("Testing first task")
    time.sleep(5)
    return True
