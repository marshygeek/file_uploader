from aiohttp import web
import redis

from routes import upload_file, get_files_list

redis = redis.Redis(host='redis')

app = web.Application()
app.router.add_put('/upload', upload_file)
app.router.add_get('/list', get_files_list)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)
