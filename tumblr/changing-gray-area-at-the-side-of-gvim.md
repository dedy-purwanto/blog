title:Changing "gray area" at the side of GVIM
date:2011-10-16 20:15:00
status:draft

<p>
I've faced similar case for several times, when I maximized my GVIM, it shows gray
area at the bottom and right side of the screen. After some research, I found out
that GVIM window dimension is actualy based on columns and rows rather than pixels.
Therefore if your resolution is not matched with the total cols/rows
of GVIM window, it will show 'waste' area which is on gray.
</p>

<p>
Some people suggest to set the columns and rows to <i>8888</i> in their <i>vimrc</i>, which 
doesn't really work for me, so instead of trying to hack the size, I'll just hack
the color by customizing my theme's gtkrc. Let's replace the gray color into
something similar to GVIM background, so we wouldn't notice the difference.
</p>

<p>
I'm using Ubuntu 10.10 with Ambiance theme, so I updated my 
<i>/usr/share/themes/ambiance/gtk-2.0/gtkrc</i> by adding this entry (at anywhere, I prefered
in the middle):
</p>

<div class="gist">http://gist.github.com/1291857"></div>

<p>
That way, everytime I opened GVIM the grayed area will be changed to a darker color
which is matched with my GVIM background.
</p>