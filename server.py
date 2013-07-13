import sys

import tornado.ioloop
import tornado.web
from tornado.options import options

from urls import urls
from settings import settings


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, urls, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    print "Starting server on http://127.0.0.1:%s" % options.port

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print "\nStopping server."