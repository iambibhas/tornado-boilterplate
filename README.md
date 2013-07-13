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


Bits
----

 - Settings as a dictionary, with full reference
 - Added shell to play with the system
 - Added apps folder to separate logic in modules
 - *Enabled importing/including urls from different apps, maintaing pattern*
 - Showing message when starting and stoping the server