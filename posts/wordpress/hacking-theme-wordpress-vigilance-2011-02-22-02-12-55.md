title:Hacking Theme Wordpress (Vigilance)
date:2011-02-22 02:12:55

(
<a href="http://kecebongsoft.wordpress.com/2011/02/22/hacking-vigilance-wordpress-theme/">
 English Version Here
</a>
) Beberapa hari yang lalu, saya lumayan nggak ada kerjaan sekita rjam 3 pagi, dan nyoba2 buat modifikasi theme wordpress. Saya orang yang cukup cepat bosan dengan theme wordpress, dan cukup nggak punya modal untuk apply buat premium account :D. Wordpress sendiri nggak memberikan fasilitas untuk mengubah banyak bagian dari theme kepada free user. Ini screenshot asli theme Vigilance yang saya pakai:

![image](/img/wordpress/2011-02-blogoriginal.jpg?w=300)
<!--more-->
Hanya untuk sedikit memperbaiki tampilan aja, saya coba ubah warna link dari defaultnya yang merah menjadi biru tua:

![image](/img/wordpress/2011-02-colorschemeori.jpg?w=300)

Yup, simple aja, cukup click color picker dan ganti warnanya. Tapi tunggu, tiba2 saya ingat setahun lalu sempat main-main dengan SB GDI dan nulis tentang
<a href="http://kecebongsoft.wordpress.com/2008/09/06/hacking-trick-css-injection/">
 CSS Injection
</a>
, saya tiba2 punya ide konyol untuk nge-hack theme Wordpress, konyol karena tentu saja harusnya layanan raksasa seperti Wordpress nggak akan bisa dibodohi dengan trik kecil seperti ini. Idenya adalah dengan melakukan injeksi kode CSS kedalam input field, persis sama seperti SQL Injection. Misalkan coder webnya menulis seperti ini:

	:::txt

echo &#8220;body{background-color: $color;}&#8221;;



Dimana variabel Color secara default harusnya adalah warna hexadecimal seperti #FFFFFF. Tapi seandainya tidak ada filterisasi, kita bisa meng-inject variable tersebut dengan tambahan lain. Misalkan variabel warna hexadecimalnya bisa diubah melalui text field seperti di bagian Theme Options pada theme Vigilance, maka kita bisa meng-injectnya dengan code seperti ini:

	:::txt

#FFFFFF;font-size:11px



Pada code diatas, saya meng-inject atribut tambahan yaitu font-size kedalam text-field. Dan ini bekerja karena ternyata tidak ada validasi sama sekali di Theme Options Wordpress!. Outputnya adalah seperti ini:

	:::txt

body{background-color: #FFFFFF;font-size:11px;}



Dan bukan hanya itu, saya bahkan bisa memasukan kelas CSS atau meng-overwrite existing class, lihat input saya ini:

	:::txt

#FFFFFF;} .footer, .date {display:none} {




Lihat kan? Dengan mudahnya kita bisa menghilangkan footer dan elemen lainnya pada theme kita dengan cara melakukan overwrite existing class. Pada code diatas saya juga menambahkan curly bracket dibagian akhir untuk menutup pola CSS. Outputnya akan jadi seperti ini:

	:::txt

body{background-color: #FFFFFF;} .footer, .date {display:none} {;}



Tanpa harus mendaftar ke account premium, saya bisa melakukan modifikasi CSS secara total!. Tapi kesenangan belum berakhir, saya juga bisa menyelipkan code HTML dan JS!. Lihat input saya berikut ini:

	:::txt

#FFFFFF;} &lt;/style&gt; &lt;b&gt;Hello World!&lt;/b&gt;&lt;script&gt;alert(&#8220;Hello World!&#8221;);&lt;/script&gt; &lt;style&gt; {



Pada input diatas, saya menutup tag CSS lalu melanjutkannya dengan tag HTML serta JS, lalu membuka kembali tag CSS untuk mencocokannya dengan pola output yang sudah ditulis oleh codernya. Kemungkinan modifikasi yang bisa kita lakukan hampir tak terbatas karena kita bisa menyelipkan HTML, artinya kita juga bisa menyelipkan elemen lain seperti flash, iframe, video, dan lain-lain.

Ini adalah modifikasi theme Vigilance yang saya buat:

	:::txt

Background Color:
 #ffffff;}&lt;/style&gt; &lt;link href='//fonts.googleapis.com/css?family=Cantarell:regular,italic,bold,bolditalic' rel='stylesheet' type='text/css' &gt; &lt;style&gt; body {&#160;&#160; font-family: 'Cantarell', serif;&#160;&#160; text-shadow: 2px 2px 2px #bbb; } &lt;/style&gt; &lt;style type='text/css' media='screen'&gt; {

linkColor:
 #3b72b5;} #title span{color:#3b72b5;} #description{float:none;width:100%;text-align:center;margin-top:-70px;margin-bottom:10px;} #nav, .author, .tags, .categories, #footer{display:none} .post-header{border:none;padding:0px}&#160; #content{width: 650px;} #sidebar{width: 250px;} .post .date{font-size:11px;text-align:right;} #sidebar a{font-size:12px;} {



Dan ini adalah screenshot dari modifikasi di Theme Options:

![image](/img/wordpress/2011-02-colorschemehacked.jpg?w=300)

Dalam modifikasi ini, saya mengubah default font menjadi Google Web Font, dan bahkan menambahkan font shadow. Saya juga mengubah banyak hal lain seperti title dan description blog saya, menghapus tag, kategori, footer, serta mengganti column width. Hasilnya blog saya menjadi lebih rapi :D

Ini adalah hasil dari input CSS injection yang saya buat:

![image](/img/wordpress/2011-02-bloghacked.jpg?w=300)

Begitulah, saya sengaja membiarkan blog saya seperti itu sekitar 2 hari. Sepertinya nggak ada admin Wordpress yang sadar. Entah apa mereka udah tau tentang bug in atau belum. Jadi saya menulis blog post dalam english sebagai proof of concept, juga membuar report ke Wordpress tentang masalah ini, saya juga udah mengembalikan konfigurasi awal theme saya menjadi yang default. Mudah-mudahan segera di-fix oleh pihak wordpress. Anda juga bisa mencobanya langsung dengan mengubah theme ke Vigilance dan mengaturnya di Theme Options :D
