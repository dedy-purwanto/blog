Title: puppet-sentry
date: 08/08/2012
tags: komputer

When I'm tasked to cast a new installation of sentry with puppet, I was
faced with problem that sentry need to interactively ask a superuser
creation when _syncdb_ is performed, which came from Django's. Fortunately.
in Django you can have initial predefined data that will be imported
when _syncdb_ is performed. By having a json formatted file in the root
project path and passing _--no-input_ in the command, Django will 
import the data and find the superuser information in the file.

To make it easier for people, I created a puppet module to install 
sentry without having to interactively enter superuser information. 
Check it here: <a href='http://github.com/kecebongsoft/puppet-sentry'>
kecebongsoft/puppet-sentry</a>
