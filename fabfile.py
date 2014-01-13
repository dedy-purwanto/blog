from fabric.api import local, lcd
from bs4 import BeautifulSoup
from slugify import slugify

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
    doc = BeautifulSoup(open('tumblr_kecebongsoft.xml', 'r'))

    for item in doc.findAll('item'):
        date = item.find("wp:post_date").text
        title = item.find("title").text.encode('ascii', 'ignore')
        content = item.find("content:encoded").text.encode('ascii', 'ignore')

        if title is None or len(title) == 0:
            title = date

        f = open('tumblr/%s.md' % slugify(title), 'w')

        f.write("title:%s\ndate:%s\nstatus:draft\n\n%s" % (title.encode('ascii', 'ignore'), date, content.encode('ascii', 'ignore')))

