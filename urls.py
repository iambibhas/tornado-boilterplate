from tornado import web
from settings import STATIC_ROOT

from handlers.main.views import HomeHandler

def include(module_path):
    module = __import__(module_path, globals(), locals(), fromlist=["*"])
    urls = getattr(module, 'urls')
    return urls


urls = [
    (r"/", HomeHandler),
    (r"/static/(.*)", web.StaticFileHandler, {"path": STATIC_ROOT}),
]
urls += include("handlers.main.urls")
