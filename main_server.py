#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import sys
import asyncio
import logging

import tornado
import tornado.websocket
import tornado.log
from tornado.options import define, options

PRJ_DIR = os.path.abspath(os.path.dirname(__file__))

define("debug", default=bool(os.environ.get('CS_DEBUG', 'false')), help="enable debug mode")
define("data_dir", default=os.environ.get('CS_DATA_DIR', '/data'), help="data directory")
define("port", default=int(os.environ.get('CS_PORT', '80')), help="clipboard server listen port")

#parse the app config
cfg_file = os.path.join(PRJ_DIR, 'settings.cfg')
if os.path.exists(cfg_file):
    tornado.autoreload.watch(cfg_file)
    tornado.options.parse_config_file(cfg_file, final=False)

WS_CLIENTS = set()

logger = logging.getLogger('clipboard_server')

if options.debug:
    if options.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(tornado.log.LogFormatter(color=False))
logger.addHandler(handler)

class BroadcastWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        logger.info("ws opened. ip: %s, id: %#x" % (self.request.remote_ip, id(self)))
        WS_CLIENTS.add(self)
        self.write_notify({"action": "assignId", "id": id(self)})

    def on_message(self, message):
        logger.info("ws recv message and broadcast. size: %s, src_ip: %s, src_id: %#x" 
                    %(len(message), self.request.remote_ip, id(self)))
        notify = {"action": "notify", "srcId": id(self), "content": message}
        for client in WS_CLIENTS:
            if client is self:
                continue
            client.write_notify(notify)
        self.write_notify({"action":"confirm", "sendNum": len(WS_CLIENTS) - 1})

    def on_close(self):
        logger.info("ws closed. ip: %s, id: %#x" %(self.request.remote_ip, id(self)))
        WS_CLIENTS.remove(self)

    def write_notify(self, msg):
        self.write_message(tornado.escape.json_encode(msg))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html") 

def make_app():
    settings = dict(
        title="Clipboard by lzmyhzy@gmail.com",
        template_path=os.path.join(PRJ_DIR, "templates"),
        static_path=os.path.join(PRJ_DIR, "static"),
        debug=options.debug,
    )

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", BroadcastWebSocket),
    ], **settings)

async def main():
    app = make_app()
    app.listen(options.port)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
