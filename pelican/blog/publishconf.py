#!/usr/bin/env python2
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *



#SITEURL = 'http://localhost/dodcott'
#SITEURL = 'http://localhost:8000'
SITEURL = 'http://dodcott.org'

#SITEURL = 'http://geekinthesticks.github.io/dodcott-cum-wilkesley'

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
