title: My new Pelican build mechanics
date: 17/11/2012

As you know, my blog is powered by a python static blog engine, named Pelican. I really like it in many ways: simplicity, _geekyness_, and hostings. Yes, hostings, this blog is hosted with the help of Github user pages, enabling you to create a static website through repository, and accessible with your Github username, plus you don't have to think about reliability and scaling, Github will handle it for you.

Pelican, as a static blog engine, of course will generate static html files that you will have to push to your repository, these auto-generated files are pretty much meaningless, you don't want to 'manage' them, but it has to stay in the repo to serve request, and above that, it has to be placed in the root path of the repository. Meanwhile we also have some other files such as static files, the blog sources (posts, config file, build script, custom themes, etc), and in my case, I also have submodules repository which is a separate static site, they are mostly HTML5 slides.

For me, I always wanted to keep everything clean, whenever I trigger a new build, I wanted to wipe all recent build files first. But I can't just do that with all other necessary files as mentioned, so few things need to be done before I trigger a build:

* Exclude all git submodules path from deletion.
* Exclude files that are not part of pelican auto-generated files.
* Wipe the rest.
* Trigger the build.

While the last one is pretty much straightforward, the first three are quite tricky, but I finally figured it out with a bash script, note that I'm not a bash hacker, you might find my build script an eyesore, well, here it is:

    :::sh
    #!/usr/bin/env bash
    GITMODULES=`grep path ../.gitmodules | sed 's/path = /\\\|/g' | sed 's/ //g' | sed 's/\t//g' | tr '\\n' '#' | sed 's/#//g' | sed 's/^\\\|//g'`
    FILES='README\|pelican\|CNAME\|static'
    EXCEPTIONS=$GITMODULES'\|'$FILES
    ls ../ | grep -v $EXCEPTIONS | xargs -i rm -rf ../{}
    source env/bin/activate
    pelican . -o ../ -s pelican.conf.py

First I grab all the submodules path and combine them together with a '\|' separator for regex purpose later, and manually list out all other excluded files with the same regex separator, and then use an inverse grep to delete the others. In my case, the manual list is really static and not always changed, so it will be safe to keep it this way, as for submodules, I have to make it dynamic to reduce the coupling.
