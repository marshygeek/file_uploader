import uuid
import os

from aiohttp import web

from workers.tasks import upload_to_server
from workers import STORAGES
import resolvers

cur_dir = os.path.dirname(os.path.realpath(__file__))
TEMP_DIR = os.path.join(cur_dir, 'temp')


def parse_storage_num(num):
    return int(num) - 1 if num.lower() != 'all' else num


async def upload_file(request: web.Request):
    params = await request.post()
    if 'file' not in params or 'upload_to' not in params:
        return web.Response(text='Missing parameters', status=400)

    upload_to = parse_storage_num(params['upload_to'])
    if upload_to != 'all' and len(STORAGES) <= upload_to:
        return web.Response(text='Wrong storage number', status=400)

    file = params['file']
    file_id = str(uuid.uuid4())
    if not os.path.exists(TEMP_DIR):
        os.mkdir(TEMP_DIR)
    with open(os.path.join(TEMP_DIR, file_id), 'wb') as out:
        out.write(file.file.read())

    upload_to_server.delay(file_id, file.filename, upload_to)

    return web.Response(text='OK')


async def get_files_list(request: web.Request):
    params = request.query
    if 'server' not in params:
        return web.Response(text='Missing parameters', status=400)

    storage_num = parse_storage_num(params['server'])
    if storage_num != 'all' and len(STORAGES) <= storage_num:
        return web.Response(text='Wrong storage number', status=400)

    files_list = resolvers.get_files_list(storage_num)
    if files_list is False:
        return web.Response(text='Error while fetching files list', status=500)

    return web.Response(text=files_list)
