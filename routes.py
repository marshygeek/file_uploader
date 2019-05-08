from aiohttp import web
from celery_package.tasks import *


async def upload_file(request: web.Request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def get_files_list(request: web.Request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
