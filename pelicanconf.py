#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Denis Sergeev'
SITENAME = u'Meteodenny'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['pdfs', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = '../theme4myblog'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['liquid_tags.notebook']

NOTEBOOK_DIR = 'notebooks'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('EarthPy', 'http://earthpy.org/'),
         ('Python4Oceanographers', 'https://ocefpaf.github.io/python4oceanographers/'),
         ('PyAOS', 'http://pyaos.johnny-lin.com/'),
         ('Polar Lows', 'http://polarlows.wordpress.com/'),
         ('Weather and Climate @ Reading', 'http://blogs.reading.ac.uk/weather-and-climate-at-reading'),
         ('FrictionVelocity', 'http://frictionvelocity.wordpress.com/'),
         ('Looking Aloft', 'http://lukemweather.blogspot.com/'),
         ('PyHOGs', 'http://pyhogs.github.io/'),
         ('The II-I blog', 'http://andrewrushby.com/'),
         ('MyCarta', 'http://mycarta.wordpress.com/'),
         ('ClimateSnack', 'http://www.climatesnack.com/'),
         ('Dr Climate', 'http://drclimate.wordpress.com/'),
         ('Eloquent Science', 'http://eloquentscience.com/'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sharing
TWITTER_WIDGET_ID = 3063887915
TWITTER_USER = 'meteodenny'
TWITTER_USERNAME = 'meteodenny'
GITHUB_URL = 'https://github.com/dennissergeev'
FACEBOOK_LIKE = True
GOOGLE_PLUS_ONE = True
GOOGLE_CUSTOM_SEARCH_SIDEBAR = False
