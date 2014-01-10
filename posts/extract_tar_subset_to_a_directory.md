Title: Extracting a subset of tar archive to a specific directory
date: 20/07/2012

I came across a task where I need to automatically download solr
package and extract the files in example/ directory to a specific 
folder so here's how it's done:

    :::sh
    $ mkdir -p /dest/path/ && tar -xf file.tar source/path --strip=n

This will create a directory and extract a folder *source/path* in the
file.tar. Notice that there's a *--strip=n--*, this will let you 
skip the directory structure up to certain level from the root. So if I
want to extract the whole content of *source/path* to *dest/path* 
without recreating *source/path* folder inside *dest/path*, I can put
*--strip=2* to the argument to skip directory *source/* and 
*source/path*



