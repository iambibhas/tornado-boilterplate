import logging
import tornado
import tornado.options
import os.path
from tornado.options import define

DEBUG = True

path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()

STATIC_ROOT = path(ROOT, "static")
TEMPLATES_ROOT = path(ROOT, "templates")

settings = {}

settings['debug'] = DEBUG
settings["static_path"] = STATIC_ROOT
settings["template_path"] = TEMPLATES_ROOT
settings["xsrf_cookies"] = True
settings["cookie_secret"] = "mA8dCYKjsgXpHrlLnxeuDNawitcTEYKRFtMU4GqeWv1hLzN3D7"