import logging
import os
from asyncore import read

from celery import Celery, shared_task

is_docker = os.environ.get("IS_DOCKER", False)

broker = "redis://redis:6379/0" if is_docker else "redis://localhost:6379"


app = Celery("tasks", broker=broker)

logger = logging.getLogger(__name__)


@app.task
def add(x, y):
    return x + y


@shared_task
def save_safaricom_farmers_from_csv(csv_file, command_str):
    logger.info("shared task reached: save_safaricom_farmers_from_csv func called")
    from accounts.save_from_csv import read_csv

    return read_csv(csv_file, command_str)


@shared_task
def add_two_numbers(x, y):
    return x + y
