import os
import sys
import re
from datetime import datetime

from bs4 import BeautifulSoup
from slugify import slugify
from urllib import urlretrieve
from fabric.api import local, lcd, warn_only, env

env.BUILD_POOL = False


# Check all possible changes in the sub path,
# it will not detect changes of files in the root path
def run_build_server():
    def path_checker():
        t = 0
        while True:
            t_new = os.path.getmtime((yield))
            if t < t_new: t = t_new; build()

    paths = []
    base_path = os.path.abspath(os.path.dirname(__file__))
    for dn, dns, fns  in \
        os.walk(base_path):
        paths.extend([os.path.join(dn, sdn) for sdn in dns])

    checker = path_checker()
    checker.next()
    while True:
        for p in paths: checker.send(p)

def pool():
    env.BUILD_POOL = True

def build(production=False):
    sys.stdout.write("==== Build starts on %s ====\n" % datetime.now())
    args = "-r" if env.BUILD_POOL else ""
    if production:
        settings = "data/settings-production.py"
    else:
        settings = "data/settings.py"

    command = "pelican . -o build/ -s %s %s" % (settings, args)
    print command
    local(command)
    local("cp -r data/media/* build/")
    sys.stdout.write("==== Build ends on %s ====\n" % datetime.now())

def deploy():
    print "Deploying..\n"
    build(production=True)

    with lcd("build/"):
        local("git add .")
        local("git commit --all --message 'New build'")
        local("git push")

    local("git add build")
    local("git commit --all --message 'New build'")

def import_tumblr():
    doc = BeautifulSoup(open('data/tumblr.xml', 'r'))
    local('rm -rf data/tumblr')
    local('mkdir -p data/tumblr'.split(' '))

    for item in doc.findAll('item'):
        date = item.find("wp:post_date").text
        title = item.find("title").text.encode('ascii', 'ignore')
        content = item.find("content:encoded").text.encode('ascii', 'ignore')

        if title is None or len(title) == 0:
            title = date

        
        f = open('data/tumblr/%s.md' % slugify(title), 'w')

        f.write("title:%s\ndate:%s\nstatus:draft\n\n%s" % (title.encode('ascii', 'ignore'), date, content.encode('ascii', 'ignore')))

def wp_download_media():
    f = open('data/wp.xml', 'r')
    r = re.compile("http://[./a-zA-Z0-9_]*.(jpg|png|jpeg|gif)")
    source = f.read()
    urls = []
    for img in r.finditer(source):
        url = img.group()
        if url not in urls: urls.append(url)

    local('mkdir -p data/wp_media'.split(' '))
    for url in urls:
        dest = url.split('/')[-3:]
        dest = 'data/wp_media/%s' % '-'.join(dest)
        dest = dest.strip()
        print 'Downloading %s to %s' % (url, dest)
        urlretrieve(url, dest)

def wp_reformat(content):
    content = BeautifulSoup(content)
    for img in content.find_all('img'):
        src = img['src']
        src = re.sub('http://kecebongsoft.files.wordpress.com/(\d+)/(\d+)/', r'/img/wordpress/\1-\2-', src)
        img.replace_with('![image](%s)' % src)
    #content = re.sub('http://kecebongsoft.files.wordpress.com/(\d+)/(\d+)/', r'/img/wordpress/\1-\2-', content)
    #content = re.sub('<im.*src=(\'|")(.*)["\'].*>', r"![image](\2)", content)

    content = re.sub('\[caption.*?\](.|\n)*?\!(.*?\))(.|\n)*?caption]', r'\2', content.encode('ascii', 'ignore'))

    content = re.sub('\[source.*?\]((.|\n)*?)\[/sourcecode\]', r'\t:::txt\1', content.encode('ascii', 'ignore'))
    

    return content

def wp_import():
    doc = BeautifulSoup(open('data/wp.xml', 'r'))

    local('rm -rf data/wordpress')
    local('mkdir -p data/wordpress')
    for item in doc.findAll('item'):
        post_type = item.find("wp:post_type").text
        if post_type == "post":
            title = item.find("title").text
            date = item.find("wp:post_date").text
            content = item.find("content:encoded").text
            content = wp_reformat(content)

            filename = slugify("%s-%s" % (title, date))

            f = open('data/wordpress/%s.md' % filename, 'w')
            f.write("title:%s\ndate:%s\n\n%s" % (title.encode('ascii', 'ignore'), date, content.encode('ascii', 'ignore')))


