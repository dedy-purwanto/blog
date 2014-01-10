from fabric.api import local

def build():
    local("pelican . -o build/ -s pelican.conf.py")

def deploy():
    print "Deploying..\n"
    build()
