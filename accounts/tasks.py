from asyncore import read

from celery import Celery, shared_task

app = Celery("tasks", broker="pyamqp://guest@localhost//")


@app.task
def add(x, y):
    return x + y


@shared_task
def save_safaricom_farmers_from_csv(csv_file):
    from accounts.save_from_csv import read_csv

    return read_csv(csv_file)
