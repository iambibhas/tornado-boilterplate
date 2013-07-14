Tornado Boilerplate v3.1
===================

This is a quick boilerplate to start building apps with Tornado.
It has an almost similar organization of a Django project, as most people are
familar with it. This is how it looks -

    .
    ├── server.py
    ├── apps
    │   ├── __init__.py
    │   └── main
    │       ├── __init__.py
    │       ├── urls.py
    │       └── views.py
    ├── __init__.py
    ├── settings.py
    ├── static
    │   └── style.css
    ├── templates
    │   ├── base.html
    │   └── home.html
    └── urls.py


## Settings ##
Settings as a dictionary, with full reference

    settings = {
        # debug: If True the application runs in debug mode
        'debug': True,

        ...
    }

***
## Shell ##
Added shell to play with the system

    (venv) ~/Works/tornado-boilerplate/project$ python shell.py
    >>> import tornado.web
    >>>

***
## Apps ##
Added apps folder to separate logic in modules

***
## Importing urls ##
Enabled importing/including urls from different apps, maintaing pattern

    urls = [
        (r"/", HomeHandler),
        (r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
    ]
    # this will include patterns from urls.py inside `main` app.
    urls += include(r"/main/", "apps.main.urls")

`/apps/main/urls.py`

    urls = [
        (r"test/", TestHandler),  # This is `/main/test/`
    ]

***
## Server start/stop message ##
Showing message when starting and stoping the server

    (venv) ~/Works/tornado-boilerplate/project$ python server.py
    Starting server on http://127.0.0.1:8888
    ^C
    Stopping server.
