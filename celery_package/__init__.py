from celery import Celery

celery = Celery('celery_package', broker='redis://localhost', include=['celery_package.tasks'])
