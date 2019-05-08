FROM python:3.6

ADD requirements.txt /app/requirements.txt
ADD ./workers/ /app/
WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT celery worker -A workers:celery --loglevel=info