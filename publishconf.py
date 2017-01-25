#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

#SITEURL = 'http://sitn.ne.ch/web/gmf'
SITEURL = 'https://map.nyon.ch/sitnyon/gmf'
RELATIVE_URLS = False

AUTHOR = u'GeoMapFish user community'
SITENAME = u'GeoMapFish'

GITHUB_URL = 'http://github.com/camptocamp/c2cgeoportal'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

PAGE_ORDER_BY = 'basename'

STATIC_PATHS = ['images']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

DEFAULT_PAGINATION = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
