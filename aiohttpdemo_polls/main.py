from aiohttp import web
from routes import setup_routes
from settings import config, BASE_DIR
from db import pg_context
from asyncio import (
    get_event_loop, set_event_loop_policy,
    WindowsSelectorEventLoopPolicy
)
from middlewares import setup_middlewares

import aiohttp_jinja2
import jinja2
import sys

if sys.platform == 'win32':
    set_event_loop_policy(WindowsSelectorEventLoopPolicy())

app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(
        str(BASE_DIR / 'aiohttpdemo_polls' / 'templates')
    )
)
setup_routes(app)
setup_middlewares(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)
