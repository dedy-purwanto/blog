title:Relocating swap and undo files on VIM
date:2012-02-12 7:25:45
tags: komputer

Every time I have a new repository, I always need to redefine the stuff that I need to ignore, more precisely, vim-related files such as swap and undo files. These things although they are really useful, but also make my working directory a bit dirty, redefine the same thing to ignore on my repository is also tedious. 

It turns out I can relocate it on other folder, and at the same time, avoid filename collision. Using this configuration:

	:::javascript
	set dir=~/.vim/swaps//,/var/tmp//,/tmp//,.
	set undodir=~/.vim/undos//,/var/tmp//,/tmp//,.