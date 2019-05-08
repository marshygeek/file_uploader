import os

from celery import Celery

redis_host = os.environ.get('REDIS_HOST', 'localhost')

celery = Celery('workers', broker=f'redis://{redis_host}:6379/0', include=['workers.tasks'])

STORAGES = ['2000', '2001']
STORAGE_AUTH = ('root', 'ssh_1245')
