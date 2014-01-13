from fabric.api import local, lcd
from bs4 import BeautifulSoup
from slugify import slugify
import os
from subprocess import call

def build():
    local("pelican . -o build/ -s pelican.conf.py")
    local("cp -r externals build/")
    local("cp -r img build/")

def deploy():
    print "Deploying..\n"
    build()

    with lcd("build/"):
        local("git add .")
        local("git commit --all --message 'New build'")
        local("git push")

    local("git add build")
    local("git commit --all --message 'New build'")

def import_tumblr():
    doc = BeautifulSoup(open('data/tumblr.xml', 'r'))
    call('mkdir data/tumblr'.split(' '))

    for item in doc.findAll('item'):
        date = item.find("wp:post_date").text
        title = item.find("title").text.encode('ascii', 'ignore')
        content = item.find("content:encoded").text.encode('ascii', 'ignore')

        if title is None or len(title) == 0:
            title = date

        
        f = open('data/tumblr/%s.md' % slugify(title), 'w')

        f.write("title:%s\ndate:%s\nstatus:draft\n\n%s" % (title.encode('ascii', 'ignore'), date, content.encode('ascii', 'ignore')))

def wp_download_media():
    call("ack -o 'http://[./a-zA-Z0-9_]*.jpg*' wordpress.xml | cat >> data/wp_media.txt".split(' '))
    call("ack -o 'http://[./a-zA-Z0-9_]*.jpeg*' wordpress.xml | cat >> data/wp_media.txt".split(' '))
    call("ack -o 'http://[./a-zA-Z0-9_]*.gif*' wordpress.xml | cat >> data/wp_media.txt".split(' '))
    call("ack -o 'http://[./a-zA-Z0-9_]*.png*' wordpress.xml | cat >> data/wp_media.txt".split(' '))
    f = open('wp_media.txt', 'r')
    files = []
    for r in f:
        url = r
        if url not in files:
            files.append(url)
            dest = r.split('/')[-3:]
            dest = 'data/wp_media/%s' % '-'.join(dest)
            dest = dest.strip()
            print 'Downloading %s to %s' % (url, dest)
            call(['curl', url, '-o', dest])