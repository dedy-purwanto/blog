#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#from pelican.settings import _DEFAULT_CONFIG

AUTHOR = u"Dedi Purwanto"
SITENAME = u"Dedi Purwanto"
SITEURL = 'http://localhost:9000'
SITETAGLINE = u""
FOOTERTEXT = u"&copy; Dedi Purwanto. "

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG='id'

LINKS = (
         )

DEFAULT_PAGINATION = 5

PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
#DIRECT_TEMPLATES = list(_DEFAULT_CONFIG['DIRECT_TEMPLATES']) + ['stories',]

REVERSE_ARCHIVE_ORDER = True

FEED_DOMAIN = 'http://kecebongsoft.com'

THEME = 'notmyidea'

PAGE_EXCLUDES = (
            'mytheme',
            'build',
            'data',
        )

ARTICLE_EXCLUDES = (
            'mytheme',
            'build',
            'data',
        )

#DISQUS_SITENAME = 'kecebongsoft'
THEME = 'mytheme'
#GITHUB_URL = 'https://github.com/kecebongsoft'
GOOGLE_ANALYTICS = 'UA-36468240-1'
