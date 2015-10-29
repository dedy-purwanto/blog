title: PyCharm
date: 2015-10-28

I have been using PyCharm for all kinds of development for a month. I was using
vim for a few years, and I'm blown away by PyCharm.

Okay, the journey to PyCharm was long, I've tried it several times but it didn't
stick, mainly because I was so into terminal and vim. But lately I have been
rambling about how it sucks to be developing on virtual machines. In short: it was
slow and I can hardly get into the flow.

Meet PyCharm, I know it was great, all along. But I wouldn't want to install it
in my virtual machine just to meet the same slowness problem. I want something
native that can make me happy. There are 2 choices in mind: Sublime Text,
and PyCharm.

Sublime Text was good, but it was not enough to make me switch to native 
development, there are troubles, especially syncing my local files with server.
So I skipped this option.

Now PyCharm, little I know their current release support remote development. What
that means is now you can code in your local computer, and all the changes will
be uploaded _instantly_ to your server.

I know it sounded so gimmick. I've tried many ways before, rsync and the likes.
They are very slow in practice, and I've spent too many hours figuring out how
to do selective syncing (just sync the files I've changed locally).

In PyCharm it's better, it does selective syncing and it's automatic, be that you
are coding in PyCharm, or when changing branch. 

So that started off my trial period for PyCharm, and man, I love it. It's not perfect
but I am able to be way more productive with it. I know I shouldn't compare it with
vim, but still. 

Okay, let me just name the stuff I like during my first month using PyCharm full-time:

### Code navigation & completion
I've tried SublimeText plugins and vim, you can name whatever famous plugins for
both, I've probably tried them. They suck. One way or another. They lose context,
they suggest wrong keywords, and they crash often.

In Pycharm, these 2 understand context, suppose I have code below:

    #!python
    def add():
        pass
    
    def complex():
        def add():
            pass
        
        a = add()

I know it's not the best code you've seen, but PyCharm understand the context
of the above code, if you use 'Go To Definition' on the last line, you will go
to the right place. Context is almost everywhere, and it's like a second nature
that you will not have to think about the accuracy anymore, you just get where
you want to go.

### Finding usages
Just like the point above, Finding usages is very helpful when developing in
a big codebase, I can work faster and don't have to spent time doing manual
search and then I have to carefully tell whether the search result is relevant
to my work or not (when they happen to share the same keyword). It's a time saver.

### Keyboard-centric UI
Although it's UI and all, you can still do most operations with keyboard shortcuts,
there are omni-search and stuff just like SublimeText, it's not perfect, in a way
it can't really get you to every single UI element, due to so many features in
PyCharm, but right now it's already very good.

### Find / Replace
Find and Replace is like feature that's already exist from dinosaur era. But in 
PyCharm they are powerful especially during refactoring. Suppose you have a big
codebase and you need to do whatever you need to do to some certain keywords, you
can do a project-wide search in PyCharm, the long list of result will came out,
and then, you can start editing, as you go along, you can scratch off the items
that you already edited via the Find window.

You can also put it in another way: PyCharm Find window can be used as check-list
for refactoring.

Not only that of course, if you change the content of the search result, the 
Find Window will be updated, say you removed the keyword from the content,
the search result will say 'INVALID', but the smart thing is, it will stay there,
and when you click it, it will still go to the correct place.

### Refactoring
This is a very nice thing to have, suppose I have this code:

    #!python
    print_file("/tmp/myfile.txt")
    zip_file("/tmp/myfile.txt")
    
I can put the caret under one of the string, and tell PyCharm I want to extract
those strings to be a variable / constant. and PyCharm will smartly do the rest
of the work, including guessing what variable name it should use (which you can
change later). A lot of things you can do in refactoring with PyCharm.

### Inspection
This is also another time saver, from basic error check to more complicated ones.
There are plugins in other software that does this, but in PyCharm it just feels
more solid and you can rely on it most of the time.

### Scratch
Scratch is like disposable files, you can use it for quick writing, be it a python
script (which you can als run/debug!) or anything else. The good thing is that
it's not automatically disposed, it is saved somewhere in your home directory,
and the creation is quite simple with a shortcut, there's no need to think
about filename or anything, but you can rename after you create, which is a very
nice thing.

### Remote Development
Remote Development is what takes me into PyCharm, and it's very good. I can still
use my python interpreter from my virtual machine, complete with all the python
libraries I have installed, I can run remote build/debug command with it, I can
run python console with it, or Django's manage.py with it. Almost anything.

It's not the perfect thing, but for now it serves all my needs.

### Small little details

__It remember your last selection on anything__

Say you are switching branch, a to b, now you want to switch back to a. During
Branch selection, PyCharm will automatically select the last place you have been,
in this case it's branch a. It works in almost everything, during search, navigation, 
etc.

__Keyboard shortcuts for faster coding__

Suppose you have this code:

    #!python
    def my_function(obj1

noticed I didn't finished the line, PyCharm have shortcuts to make this statement
completed, which is Ctrl+Shift+Enter. It will fill the rest with proper parentheses
and colon. It works everywhere, in any file type it supported. There are many
other keyboard shortcuts as well.

__Consistent Keyboard Shortcut__

I tend to keep everything fresh, I don't like customizing keyboard shortcuts to
my preference because I believe the developer had always better idea why certain
things are the way they are. So in PyCharm, the builtin keymap scheme is excellent.

In every tool window / feature you are in, you can always use the same keyboard 
shortcut for the same type of operation. Say you are in the editor, you can fold/unfold
with Ctrl+Plus and Ctrl+Minus, and when you are in the Find Window, you can do
the same with the search result using the same shortcuts.

All in all, I'm sold to PyCharm and I think I will continue to write some things
I find on it during my usage.

