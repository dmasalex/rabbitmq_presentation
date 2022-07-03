from push_task import Celery
from push_task import app

celery = Celery()
celery.config_from_object(app.conf)

for i in range(10):
    celery.send_task('run_one', [2222222], queue="new_celery", routing_key="new_celery", priority=2)
    celery.send_task('run_two', [8888888], queue="new_celery", routing_key="new_celery", priority=8)
    celery.send_task('run_three', [5555555], queue="new_celery", routing_key="new_celery")
