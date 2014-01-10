from fabric.api import local

def build():
    local("pelican . -o build/ -s pelican.conf.py")
    local("cp -r externals build/")

def deploy():
    print "Deploying..\n"
    build()
