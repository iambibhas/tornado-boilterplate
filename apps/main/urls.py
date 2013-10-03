from tornado.web import URLSpec as url
from .views import TestHandler

urls = [
    url(r"test/", TestHandler),
]