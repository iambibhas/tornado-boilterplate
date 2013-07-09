from tornado import web
from settings import STATIC_ROOT
from utils import include

from handlers.main.views import HomeHandler

urls = [
    (r"/", HomeHandler),
    (r"/static/(.*)", web.StaticFileHandler, {"path": STATIC_ROOT}),
]
urls += include(r"/main", "handlers.main.urls")
