title:Hacking Vigilance Wordpress Theme
date:2011-02-22 02:12:35
tags: komputer

(
<a href="http://kecebongsoft.wordpress.com/2011/02/22/hacking-theme-wordpress-vigilance/">
 Versi Indonesia Disini
</a>
) Few days ago, I was quite bored at 3AM and decided to decorate my Wordpress theme. I&#8217;ve been using Vigilance theme for a while and I think it is a good theme, except that there are stuff I don&#8217;t really like, such as some colors and positioning. Unfortunately I can&#8217;t change most part of the theme since I didn&#8217;t apply for premium account. Here was the screenshot of my original Vigilance theme:

![image](/img/wordpress/2011-02-blogoriginal.jpg?w=300)
<!--more-->
In a free account, Vigilance only provides some features to change the colors of some elements. Better than doing nothing, I rather change the link color from default red to dark blue through these options:

![image](/img/wordpress/2011-02-colorschemeori.jpg?w=300)

No big deal right? I just have to click the color picker and change the color value. But suddenly a random thought flows in my head, few years back I wrote an article about hacking a web page through CSS inputs.
<a href="http://kecebongsoft.wordpress.com/2008/09/06/hacking-trick-css-injection/">
 This article was written in Bahasa Indonesia
</a>
. I have this stupid thought about trying this trick in Wordpress theme, I thought it was stupid because Wordpress is such as giant service and there&#8217;s no way this kind of vulnerable exists in their system.

The idea is to inject CSS codes in the input field, followed by other codes as you wish. This is almost same as SQL Injection. If the coder wrote this:

	:::txt

echo &#8220;body{background-color: $color;}&#8221;;



Color variable by default suppose to be a hex color value such as #FFFFFF. But if there&#8217;s no sanitation in the flow, we can actually inject the hex value. Suppose that the hex value can be modified through a text field like in the Vigilance theme options, then we can actually put this:

	:::txt

#FFFFFF;font-size:11px



I am injecting an additional CSS attribute (font-size) into the text field. It will work since there&#8217;s no validation! The output code will be like this:

	:::txt

body{background-color: #FFFFFF;font-size:11px;}



No, it&#8217;s not just that, I can even add more CSS class or modify the existing one, look at my input:

	:::txt

#FFFFFF;} .footer, .date {display:none} {



See? I can easily remove the footer and date field in my theme. And I also put an additional curly bracket at the end of the input, so the output will be like this:

	:::txt

body{background-color: #FFFFFF;} .footer, .date {display:none} {;}



Without applying for premium account, I can modify my CSS theme without any limit. But the fun hasn&#8217;t end yet, I can put HTML and JS code as well! Look at my input:

	:::txt

#FFFFFF;} &lt;/style&gt; &lt;b&gt;Hello World!&lt;/b&gt;&lt;script&gt;alert(&#8220;Hello World!&#8221;);&lt;/script&gt; &lt;style&gt; {



There it is, I am injecting a HTML and a simple javascript code into my CSS input, and the list will infinitely goes on from this, you can almost add anything, name it, flash, iframe, videos, anything.

Here is the modification I made for my Vigilance theme:

	:::txt

Background Color:
 #ffffff;}&lt;/style&gt; &lt;link href='//fonts.googleapis.com/css?family=Cantarell:regular,italic,bold,bolditalic' rel='stylesheet' type='text/css' &gt; &lt;style&gt; body {&#160;&#160; font-family: 'Cantarell', serif;&#160;&#160; text-shadow: 2px 2px 2px #bbb; } &lt;/style&gt; &lt;style type='text/css' media='screen'&gt; {

linkColor:
 #3b72b5;} #title span{color:#3b72b5;} #description{float:none;width:100%;text-align:center;margin-top:-70px;margin-bottom:10px;} #nav, .author, .tags, .categories, #footer{display:none} .post-header{border:none;padding:0px}&#160; #content{width: 650px;} #sidebar{width: 250px;} .post .date{font-size:11px;text-align:right;} #sidebar a{font-size:12px;} {



Here is the screenshot of my modification:

![image](/img/wordpress/2011-02-colorschemehacked.jpg?w=300)

In this modification, I changed the default font to Google Web Font, and I even add the font shadow. Also, I changed many things in the theme such as the title and description placement, removing tags, categories and footer, changing the column width, etc.

Here is the result of my code:

![image](/img/wordpress/2011-02-bloghacked.jpg?w=300)

That&#8217;s it, I leave it like that for almost 2 days. It seems like no Wordpress admin aware about my changes. I am not sure whether they knew about this vulnerable or not. So I am writing this post as well as a report to them, and I changed back my theme to the default one right before I wrote this blog post. Hopefully they will fix it, in case they haven't, you can try it on your own. Change your theme to Vigilance, and go to Theme Options, have fun :D
