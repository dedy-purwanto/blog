title: PyCharm: Build with bash remotely
date: 2015-10-28

One thing that's greatly missing in PyCharm is the ability to run build config
using bash, there are plugins to support bash for build configuration, but it
doesn't support remote execution unlike the rest of PyCharm's build configuration.

There are various cases where I need to run remote bash execution during remote
development, such as fabric script, and custom test runner. When searching
through the web, I found the solutions are often hackish (well it suppose to be)
and require creating additional files which are not very relevant to the project.

After a while I came up something I consider the simplest and require least step:

1. Create a Python build configuration.
2. Leave the script name empty.
3. Change the working directory as desired.
4. Use this for the script parameter:

    -c "import os; print os.system('command goes here')"
    
It's very important to have the double quote on the outside. Another thing is,
if you want to run environment-specific command, such as when using virtualenv,
you will need to activate it first:

    -c "import os; print os.system('. /path/to/env/bin/activate && more commands')"

This is far from perfect and will look ugly when it goes longer. But for all my
stuff this serves the best.