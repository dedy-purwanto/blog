import os
from subprocess import call

f = open('wordpress_media_urls.txt', 'r')


files = []
for r in f:
    url = r
    if url not in files:
        files.append(url)
        dest = r.split('/')[-3:]
        dest = 'wordpress_media/%s' % '-'.join(dest)
        dest = dest.strip()
        print 'Downloading %s to %s' % (url, dest)
        call(['curl', url, '-o', dest])

