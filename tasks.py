from celery import Celery
import time 

celery = Celery('tasks', backend='redis://localhost', broker='amqp://')


@celery.task
def test(strs):
    return strs
    
