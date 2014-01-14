title:Hacking Vigilance Wordpress Theme
date:2011-02-22 02:12:35
status:draft

(<a href="http://kecebongsoft.wordpress.com/2011/02/22/hacking-theme-wordpress-vigilance/">Versi Indonesia Disini</a>) Few days ago, I was quite bored at 3AM and decided to decorate my Wordpress theme. Ive been using Vigilance theme for a while and I think it is a good theme, except that there are stuff I dont really like, such as some colors and positioning. Unfortunately I cant change most part of the theme since I didnt apply for premium account. Here was the screenshot of my original Vigilance theme:

[caption id="attachment_928" align="alignnone" width="300" caption="Original Theme"]<a href="http://kecebongsoft.files.wordpress.com/2011/02/blogoriginal.jpg"><img class="size-medium wp-image-928" title="blogoriginal" src="http://kecebongsoft.files.wordpress.com/2011/02/blogoriginal.jpg?w=300" alt="" width="300" height="234" /></a>[/caption]

<!--more-->

In a free account, Vigilance only provides some features to change the colors of some elements. Better than doing nothing, I rather change the link color from default red to dark blue through these options:

[caption id="attachment_929" align="alignnone" width="300" caption="Original Color Scheme"]<a href="http://kecebongsoft.files.wordpress.com/2011/02/colorschemeori.jpg"><img class="size-medium wp-image-929" title="colorschemeori" src="http://kecebongsoft.files.wordpress.com/2011/02/colorschemeori.jpg?w=300" alt="" width="300" height="209" /></a>[/caption]

No big deal right? I just have to click the color picker and change the color value. But suddenly a random thought flows in my head, few years back I wrote an article about hacking a web page through CSS inputs. <a href="http://kecebongsoft.wordpress.com/2008/09/06/hacking-trick-css-injection/">This article was written in Bahasa Indonesia</a>. I have this stupid thought about trying this trick in Wordpress theme, I thought it was stupid because Wordpress is such as giant service and theres no way this kind of vulnerable exists in their system.

The idea is to inject CSS codes in the input field, followed by other codes as you wish. This is almost same as SQL Injection. If the coder wrote this:

[sourcecode language="html"]

echo body{background-color: $color;};

[/sourcecode]

Color variable by default suppose to be a hex color value such as #FFFFFF. But if theres no sanitation in the flow, we can actually inject the hex value. Suppose that the hex value can be modified through a text field like in the Vigilance theme options, then we can actually put this:

[sourcecode language="html"]

#FFFFFF;font-size:11px

[/sourcecode]

I am injecting an additional CSS attribute (font-size) into the text field. It will work since theres no validation! The output code will be like this:

[sourcecode language="html"]

body{background-color: #FFFFFF;font-size:11px;}

[/sourcecode]

No, its not just that, I can even add more CSS class or modify the existing one, look at my input:

[sourcecode language="html"]

#FFFFFF;} .footer, .date {display:none} {

[/sourcecode]

See? I can easily remove the footer and date field in my theme. And I also put an additional curly bracket at the end of the input, so the output will be like this:

[sourcecode language="html"]

body{background-color: #FFFFFF;} .footer, .date {display:none} {;}

[/sourcecode]

Without applying for premium account, I can modify my CSS theme without any limit. But the fun hasnt end yet, I can put HTML and JS code as well! Look at my input:

[sourcecode language="html"]

#FFFFFF;} &lt;/style&gt; &lt;b&gt;Hello World!&lt;/b&gt;&lt;script&gt;alert(Hello World!);&lt;/script&gt; &lt;style&gt; {

[/sourcecode]

There it is, I am injecting a HTML and a simple javascript code into my CSS input, and the list will infinitely goes on from this, you can almost add anything, name it, flash, iframe, videos, anything.

Here is the modification I made for my Vigilance theme:

[sourcecode language="html"]

Background Color:
 #ffffff;}&lt;/style&gt; &lt;link href='//fonts.googleapis.com/css?family=Cantarell:regular,italic,bold,bolditalic' rel='stylesheet' type='text/css' &gt; &lt;style&gt; body { font-family: 'Cantarell', serif; text-shadow: 2px 2px 2px #bbb; } &lt;/style&gt; &lt;style type='text/css' media='screen'&gt; {

linkColor:
 #3b72b5;} #title span{color:#3b72b5;} #description{float:none;width:100%;text-align:center;margin-top:-70px;margin-bottom:10px;} #nav, .author, .tags, .categories, #footer{display:none} .post-header{border:none;padding:0px} #content{width: 650px;} #sidebar{width: 250px;} .post .date{font-size:11px;text-align:right;} #sidebar a{font-size:12px;} {

[/sourcecode]

Here is the screenshot of my modification:

[caption id="attachment_930" align="alignnone" width="300" caption="Color Scheme Hacked"]<a href="http://kecebongsoft.files.wordpress.com/2011/02/colorschemehacked.jpg"><img class="size-medium wp-image-930" title="colorschemehacked" src="http://kecebongsoft.files.wordpress.com/2011/02/colorschemehacked.jpg?w=300" alt="" width="300" height="209" /></a>[/caption]

In this modification, I changed the default font to Google Web Font, and I even add the font shadow. Also, I changed many things in the theme such as the title and description placement, removing tags, categories and footer, changing the column width, etc.

Here is the result of my code:

[caption id="attachment_931" align="alignnone" width="300" caption="Vigilance Theme Hacked"]<a href="http://kecebongsoft.files.wordpress.com/2011/02/bloghacked.jpg"><img class="size-medium wp-image-931" title="bloghacked" src="http://kecebongsoft.files.wordpress.com/2011/02/bloghacked.jpg?w=300" alt="" width="300" height="234" /></a>[/caption]

Thats it, I leave it like that for almost 2 days. It seems like no Wordpress admin aware about my changes. I am not sure whether they knew about this vulnerable or not. So I am writing this post as well as a report to them, and I changed back my theme to the default one right before I wrote this blog post. Hopefully they will fix it, in case they haven't, you can try it on your own. Change your theme to Vigilance, and go to Theme Options, have fun :D