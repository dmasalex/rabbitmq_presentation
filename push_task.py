from celery import Celery
from kombu import Queue
import time


app = Celery('celery_test',
             broker='amqp://guest:guest@127.0.0.1:5672/')


app.conf.task_queues = (
    Queue("new_celery", routing_key="new_celery", queue_arguments={'x-max-priority': 9}),
)


@app.task(name="run_one")
def run_one(args):
    time.sleep(2)
    print(args)


@app.task(name="run_two")
def run_two(args):
    time.sleep(2)
    print(args)


@app.task(name="run_three")
def run_three(args):
    time.sleep(2)
    print(args)

