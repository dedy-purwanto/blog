from fabric.api import local, lcd

def build():
    local("pelican . -o build/ -s pelican.conf.py")
    local("cp -r externals build/")

def deploy():
    print "Deploying..\n"
    build()
    with lcd("build/"):
        local("git add .")
        local("git commit --all --message 'New build'")
        local("push")
    local("git add build")
    local("git commit --all --message 'New build'")
