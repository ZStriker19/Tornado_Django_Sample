#!/usr/bin/env python

# Run this with
# PYTHONPATH=. DJANGO_SETTINGS_MODULE=testsite.settings testsite/tornado_main.py
# Serves by default at
# http://localhost:8080/hello-tornado and
# http://localhost:8080/hello-django
# from ddtrace import patch_all
# patch_all()

from ddtrace import tracer, patch
patch(tornado=True)
patch(django=True)

import logging

from ddtrace import tracer

logging.basicConfig(level=logging.DEBUG)

tracer.debug_logging = True


from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
from django.conf import settings
import tornado.gen



# if django.VERSION[1] > 5:
django.setup()


define('port', type=int, default=8080)

class HelloHandler(tornado.web.RequestHandler):
  # @tracer.wrap()
  def get(self):
    self.write('Hello from tornado')

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        self.write("Hello, world")


def main():

  parse_command_line()
  wsgi_app = tornado.wsgi.WSGIContainer(
    django.core.handlers.wsgi.WSGIHandler())
  tornado_app = tornado.web.Application(
    [
      ('/hello-tornado', HelloHandler),
      ('/hello-other-tornado', MainHandler),
      ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
      ])
  server = tornado.httpserver.HTTPServer(tornado_app)
  server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()
  # tornado.ioloop.IOLoop.current().start()




if __name__ == '__main__':
  main()
