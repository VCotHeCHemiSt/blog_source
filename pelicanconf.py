#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Valentina Colapicchioni, Ph.D.'
SITENAME = 'VCotHeCHemiSt'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = '../output'
THEME = 'theme'
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']


###Backdrop settings
SITESUBTITLE="Science blog"
EMAIL='vale.colapicchioni@gmail.com'
YEAR='2020'
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')


TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/valentina.colapicchioni/'),
          ('LinkedIn', 'https://www.linkedin.com/in/valentina-colapicchioni-228285100'),
          ('Scopus', 'https://www.scopus.com/authid/detail.uri?authorId=55790308800'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
