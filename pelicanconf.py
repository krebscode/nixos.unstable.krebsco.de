#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'makefu'
SITENAME = 'only code is pure'
SITEURL = 'http://syntax-fehler.de'
#SITESUBTITLE = 'A collection of pseudocode snippets'

TIMEZONE = 'Europe/Berlin'
THEME = './pelican-themes/gum/'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
# Blogroll
STATIC_PATHS = [ 'extra/robots.txt', ]
EXTRA_PATH_METADATA = { 'extra/robots.txt': {'path': 'robots.txt'}, }

LINKS =  (('exco\'s blog', 'http://excogitation.de'),
        ('Binaergewitter', 'http://krepel.us'),)

# Social widget
SOCIAL = (('@makefoo', 'http://twitter.com/makefoo') ,)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MENUITEMS = (( 'RSS', '/feeds/all.atom.xml'),)
