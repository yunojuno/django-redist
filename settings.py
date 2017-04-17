# -*- coding: utf-8 -*-
import os

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django-redist',
    }
}

SECRET_KEY = "donotshare"

GEOIP_PATH = os.path.dirname(__file__)

assert DEBUG is True, "This project is only intended to be used for testing."
