import os

f = open('wordpress_media_urls.txt', 'r')


files = []
for r in f:
    url = r
    if url not in files:
        files.append(url)
        dest = r.split('/')[-3:]
        dest = 'wordpress_media/%s' % '-'.join(dest)
        print 'Downloading %s to %s' % (url, dest)
        os.system('wget %s %s' % (url, dest))

