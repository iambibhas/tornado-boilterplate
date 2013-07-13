from tornado import web
from settings import settings
from utils import include

from apps.main.views import HomeHandler

urls = [
    (r"/", HomeHandler),
    (r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
]
urls += include(r"/main/", "apps.main.urls")
