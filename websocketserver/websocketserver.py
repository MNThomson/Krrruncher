#!/usr/bin/env python3

import logging
import socketio
from aiohttp import web
from typing import Dict

sio = socketio.AsyncServer(
    async_mode='aiohttp',
    cors_allowed_origins='*'  # hack (not secure in real life)
)


async def on_start(app: web.Application):
    logging.basicConfig(level=logging.INFO)
    logging.debug(app)
    logging.info("on_start")


async def on_cleanup(app: web.Application):
    logging.debug(app)
    logging.info("on_cleanup")


async def broadcast(request: web.Request) -> web.Response:
    # function is a bit of a hack so I can lazily test to see if websocket clients are receiving messages
    logging.debug(request)
    # message will go to ALL clients connected. Need to add client/user management if we want to send individual
    # messages to a single client. but since this is just a for FUN project don't over-engineer ;)
    # To test this:
    # docker exec -it websocketserver bash
    # $ curl localhost:5001/broadcast
    # check your browser console and you should see the message arrive ;)
    # todo: in reality, we should have a background task that listens to rabbitmq and sends the corresponding messages.
    await sio.emit('broadcast', data={'ben': 'test'})
    return web.Response()


@sio.event
async def connect(sid: str, environ: Dict[str, str]):
    logging.debug(environ)
    logging.info(f"connect for {sid}")


@sio.event
async def disconnect(sid: str):
    logging.info(f"disconnect for {sid}")


def main():
    app = web.Application()
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_cleanup)
    routes = [web.get('/broadcast', broadcast)]
    app.add_routes(routes)
    sio.attach(app)
    try:
        web.run_app(app, port=5001)
    finally:
        logging.info(f"websocketserver quitting")


if __name__ == '__main__':
    main()
