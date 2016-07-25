#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'makefu'
SITENAME = 'Adventures in NixOS unstable'
SITEURL = 'http://nixos.unstable.krebsco.de'
#SITESUBTITLE = 'A collection of pseudocode snippets'

TIMEZONE = 'Europe/Berlin'
THEME = './pelican-themes/gum/'
DEFAULT_LANG = 'en'
#DEFAULT_CATEGORY = 'misc'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
STATIC_PATHS = ['extra/robots.txt','extra','img']
EXTRA_PATH_METADATA = { 'extra/robots.txt': {'path': 'robots.txt'}, }

# Blogroll
LINKS =  (
        ('eloop congress', 'http://eloop.org'),
        ('Binaergewitter', 'http://krepel.us'),
        ('makefu\'s blog', 'http://euer.krebsco.de'),
        ('exco\'s blog', 'http://excogitation.de'),
        )

# Social widget
SOCIAL = (('@makefoo', 'http://twitter.com/makefoo') ,)
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'nixos-unstable'
GOOGLE_ANALYTICS = "UA-81296513-1"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MENUITEMS = ( ( 'Wiki', 'http://wiki.euer.krebsco.de/makefu.html'), )

READERS = {"html": None}

PLUGIN_PATHS = ['plugins',]
PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
