import logging
import os
from os.path import dirname

from workers import celery, STORAGES

logging.basicConfig(level=logging.INFO)

cur_dir = dirname(os.path.realpath(__file__))
TEMP_DIR = os.path.join(dirname(cur_dir), 'temp')


@celery.task
def upload_to_server(file_id, filename, upload_to):
    path_to_file = os.path.join(TEMP_DIR, file_id)
    if not os.path.exists(path_to_file):
        logging.error(f'No file found: {path_to_file}')
        return

    with open(path_to_file, 'rb') as file:
        file_body = file.read()

    logging.info(f'Uploaded file: {filename}')

    os.remove(path_to_file)
    logging.info(f'Removed file: {path_to_file}')
