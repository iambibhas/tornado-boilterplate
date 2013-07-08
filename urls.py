from handlers.main.views import HomeHandler

def include(module_path):
    module = __import__(module_path, globals(), locals(), fromlist=["*"])
    urls = getattr(module, 'urls')
    return urls


urls = [
    # (r"/", HomeHandler),
]
urls += include("handlers.main.urls")
