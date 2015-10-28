#!/usr/bin/env python
# -*- coding: utf-8 -*- #

#from pelican.settings import _DEFAULT_CONFIG

AUTHOR = u"Dedy Purwanto"
SITENAME = u"Dedy Purwanto"
SITEURL = 'http://dev:9005'
SITESUBTITLE = u"&copy;2004-2015 Dedy Purwanto"

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

PAGE_EXCLUDES = (
            'themes',
            'build',
            'data',
            'drafts',
        )

ARTICLE_EXCLUDES = (
            'themes',
            'build',
            'data',
            'drafts',
        )

#DISQUS_SITENAME = 'kecebongsoft'
THEME = 'themes/polos'
# THEME = 'themes/pelican-elegant-master'
LANDING_PAGE_ABOUT = {
        'details': "Seorang programmer, suami dan ayah.  Saya terlahir di Samarinda, Indonesia; sekolah di SMKTI Airlangga Samarinda, lalu melanjutkan studi software engineering di INTI International University Malaysia. Saat ini tinggal di Kuala Lumpur, Malaysia.<br /><br /> Di sela-sela waktu saya menulis tentang komputer dan pemrograman, di waktu lain saya juga menulis tentang perspektif saya terhadap berbagai hal, serta kehidupan personal saya.<br /><br />Saya juga bisa ditemukan di <a href='http://facebook.com/kecebongsoft/'>Facebook</a>, <a href='http://twitter.com/kecebongsoft'>Twitter</a>, dan <a href='http://github.com/kecebongsoft/'>Github</a>. Blog ini dibuat dengan menggunakan Pelican dan Elegance Theme, semua tulisan disini adalah murni milik saya dan tidak mewakili pihak manapun.",
}
#GITHUB_URL = 'https://github.com/kecebongsoft'
GOOGLE_ANALYTICS = 'UA-36468240-1'
