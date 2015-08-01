#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Denis Sergeev'
SITENAME = u'Meteodenny'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['pdfs']

THEME = '../pelican-themes/gum'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['liquid_tags.notebook']

NOTEBOOK_DIR = 'notebooks'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('EarthPy', 'http://earthpy.org/'),
         ('Polar Lows', 'http://polarlows.wordpress.com/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sharing
TWITTER_USER = 'meteodenny'
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
