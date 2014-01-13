title:Indent / outdent like a GUI text editor with VIM 
date:2012-02-12 7:19:48

Or, precisely GVIM, or VIM will just do, I don't know, I think it should also work on VIM (tried it on SSH last time and it works).

So with this you can visual block lines of codes, and press TAB to indent it, and SHIFT+TAB to outdent it, just like what you usually do on GUI text editor like Gedit or others:

	:::javascript
	vnoremap <silent><S-TAB> <gv
	vnoremap <silent><TAB> >gv

So what does it do?, it simply indent/outdent a code on a visual mode (<strong>&lt;</strong>/<strong>&gt;</strong>). But by default, visual mode will go back to normal mode after indenting/outdenting, so what we need to do is to back to visual mode and reselect our last selection, this is done by <strong>gv</strong>.