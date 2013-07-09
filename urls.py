from tornado import web
from settings import STATIC_ROOT

from handlers.main.views import HomeHandler

def include(prefix, module_path):
    module = __import__(module_path, globals(), locals(), fromlist=["*"])
    urls = getattr(module, 'urls')
    final_urls = list()
    for url in urls:
        pattern, view = url
        if not pattern.startswith("/"):
            pattern = r"%s/%s" % (prefix, pattern)
        else:
            pattern = r"%s%s" % (prefix, pattern)
        final_urls.append((pattern, view))
    return final_urls


urls = [
    (r"/", HomeHandler),
    (r"/static/(.*)", web.StaticFileHandler, {"path": STATIC_ROOT}),
]
urls += include(r"/main", "handlers.main.urls")
