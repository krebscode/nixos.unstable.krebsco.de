#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://euer.krebsco.de'
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

DISQUS_SITENAME = 'euer'
#GOOGLE_ANALYTICS = ""
PIWIK_URL='mediengewitter.krebsco.de:10000'
PIWIK_SITE_ID=1
