#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pathlib import Path

AUTHOR = u'Denis Sergeev'
SITENAME = u'Meteodenny'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['extra/robots.txt', 'extra', 'cv/cv-sergeev-long.pdf',
                'extra/favicon.ico', 'extra/custom.css']
ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = ['cv']
STATIC_EXCLUDES = ['cv/.git']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'extra/custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
}
CUSTOM_CSS = 'extra/custom.css'

THEME = 'theme'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'default'
OVERWRITE_NB_HEADER = True
if not Path('_nb_header.html').exists():
    Path('_nb_header.html').touch()
EXTRA_HEADER = open('_nb_header.html').read()

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['tag_cloud', 'summary', 'i18n_subsites',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

NOTEBOOK_DIR = 'notebooks'

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_ARTICLE_CATEGORY = False
SHOW_ARTICLE_AUTHOR = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [('Blog', '/blog/')]

ARCHIVES_SAVE_AS = 'archives.html'
DIRECT_TEMPLATES = ['index', 'archives']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# SOCIAL
ACADEM = True
SOCIAL = (('twitter', 'https://twitter.com/meteodenny'),
          ('linkedin', 'https://www.linkedin.com/in/denis-sergeev-a3837078/'),
          ('github', 'https://github.com/dennissergeev'),
          ('stackoverflow', 'https://stackexchange.com/users/6998329/denis-sergeev', 'stack-overflow'),
          ('academia', 'https://eastanglia.academia.edu/DenisSergeev'),
          ('google-scholar', 'https://scholar.google.co.uk/citations?user=_TPM1CcAAAAJ'),
          ('mendeley', 'https://www.mendeley.com/profiles/dennis-sergeev'),
          ('orcid', 'https://orcid.org/0000-0001-8832-5288'),
          ('researchgate', 'https://www.researchgate.net/profile/Denis_Sergeev2')
         )

# Blogroll
LINKS = (('EarthPy', 'http://earthpy.org/'),
         ('Python4Oceanographers', 'https://ocefpaf.github.io/python4oceanographers/'),
         ('PyAOS', 'http://pyaos.johnny-lin.com/'),
         ('Polar Lows', 'http://polarlows.wordpress.com/'),
         ('Weather and Climate @ Reading', 'http://blogs.reading.ac.uk/weather-and-climate-at-reading'),
         ('FrictionVelocity', 'http://frictionvelocity.wordpress.com/'),
         ('Looking Aloft', 'http://lukemweather.blogspot.com/'),
         ('PyHOGs', 'http://pyhogs.github.io/'),
         ('MyCarta', 'http://mycarta.wordpress.com/'),
         ('SciSnack', 'http://www.scisnack.com/'),
         ('Dr Climate', 'http://drclimate.wordpress.com/'),
         ('Eloquent Science', 'http://eloquentscience.com/'),
         )

DEFAULT_PAGINATION = 5

ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Sharing
DISQUS_SITENAME = 'disqus_5BMRcIJAsI'
ADDTHIS_PROFILE = 'ra-55c2777d723325cf'
TWITTER_WIDGET_ID = '572463710745427968'
TWITTER_USER = 'meteodenny'
TWITTER_USERNAME = 'meteodenny'
GITHUB_URL = 'https://github.com/dennissergeev'
FACEBOOK_LIKE = True
GOOGLE_PLUS_ONE = True
GOOGLE_CUSTOM_SEARCH_SIDEBAR = False
