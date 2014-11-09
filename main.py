"""Contains the main WSGI application for the application site."""
import logging

from handlers import home
from handlers import copy_me

import webapp2

app = webapp2.WSGIApplication(
    [
        ('/', home.Handler),
        # ('/copy_me', copy_me.Handler),
    ]
)
