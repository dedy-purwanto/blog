title:META Rerfresh - Merefresh dokumen dalam hitungan mundur.
date:2007-07-12 05:23:18

<p class="main">
 Bagi yang pernah pakai javascript, ada satu fungsi yang disebut navigate("") atau document.href untuk memindahkan halaman ke url yang kita inginkan, atau pada php dikenal dengan fungsi header("location : http://&#8230;"). Tapi javascript belum tentu kompak dengan semua browser, dan kita belum tentu selalu memakai PHP.
</p>
Dari kasus tersebut, kita bisa menggunakan fungsi bawaan dari HTML, yaitu META Refresh. Ialah
<a href="http://en.wikipedia.org/wiki/Meta_element">
 elemen HTTP META
</a>
yang dipakai untuk merefresh/mengganti alamat dokumen dalam hitungan mundur yang bisa kita atur (dalam satuan detik). Sintaksnya adalah sebagai berikut :

Untuk refresh dalam 10 detik :
<pre>&lt;meta http-equiv="refresh" content="10"&gt;</pre>
Untuk mengganti alamat dokumen dalam 10 detik :
<pre>&lt;meta http-equiv="refresh" content="10;url=http://kecebong.madpage.com/blog/"&gt;</pre>
Dan tentu saja dimasukan di bagian &lt;head&gt;&#8230;&lt;/head&gt;, jadi scriptnya seperti ini :
<pre>&lt;head&gt;
&lt;title&gt;Websiteku&lt;/title&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"&gt;
&lt;meta http-equiv="refresh" content="10;url=http://kecebong.madpage.com/blog/"&gt;
&lt;/head&gt;</pre>
Dibanding pakai javascript/php, META Refresh jauh lebih fleksibel karena merupakan bawaan HTML dan cross browser. Ada yang mo coba? coba? coba?.
