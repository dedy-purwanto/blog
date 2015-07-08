title:Menunggangi Google Blog Search
date:2008-05-22 22:08:36

![image](http://i247.photobucket.com/albums/gg153/kecebongsoft/scr1.jpg)
Pernah melihat screenshoot disamping?. Bagi pengguna
<a href="http://www.wordpress.com">
 Wordpress
</a>
, ini adalah salah satu widget pada Dashboard page yang akan menampilkan blog apapun yang memiliki link ke blog kita, atau lebih dikenal dengan istilah
<a href="http://en.wikipedia.org/wiki/Trackback">
 Trackback URL
</a>
. Gambar disamping juga adalah salah satu tampilan Dashboard Wordpress.com yang baru saja dirombak beberapa bulan yang lalu, yang tentunya bikin kita makin cinta sama Wordpress :-D
<!--more-->
<p style="text-align:left;">
 Hmm.. okay, lupakan dulu soal tampilan Dashboard baru. Sudah lama aku penasaran tentang bagaimana Wordpress atau layanan blog lainnya "menjelajahi" internet untuk menemukan link penggunanya dicantumkan di blog lain. Apakah dengan
 <abbr title="koding manual">
  hardcode
 </abbr>
 ? atau menggunakan layanan "penjelajah" yang telah ada?. Dan berhubung screenshoot tersebut mengatakan bahwa Wordpress menggunakan
 <a href="http://blogsearch.google.com/">
  Google Blog Search
 </a>
 sebagai penjelajahnya, maka misteri terungkaplah sudah. Tapi tunggu dulu, bagi yang belum mengenal Google Blog Search, ini adalah layanan yang sudah cukup lama ada di Google namun masih berstatus
 <a href="http://en.wikipedia.org/wiki/Software_release_life_cycle#Beta">
  Beta
 </a>
 . Layanan ini berfungsi untuk mencari blog mana saja yang mencantumkan link ke blog yang kita miliki dalam rentang waktu tertentu, dengan banyak opsi dan pilihan pencarian, Google Blog Search menjadi sebuah penjelajah trackback yang benar-benar powerfull. Terlepas dari itu, aku heran Google suka sekali dengan embel-embel Beta, bahkan
 <a href="http://mail.google.com">
  Gmail
 </a>
 dulu sampai bertahun-tahun dipakai (dan penggunanya sudah jutaan orang) namun masih berstiker Beta.
</p>
<p style="text-align:left;">
 ![image](http://blogsearch.google.co.id/blogsearch/intl/id_ALL/images/g_bsrch_logo.gif)
 Disini aku nggak ngebahas gimana menggunakan Google Blog Search secara "langsung", dalam artian menggunakannya langsung dari website Google Blog Search. Disini kita akan nyobain gimana memanfaatkan layanan ini seperti yang dilakukan Wordpress, yaitu "menempelkan" Google Blog Search kedalam website yang kita miliki. Syaratnya? Simpel, satu web server, dan sedikit pengetahuan tentang
 <a href="http://en.wikipedia.org/wiki/Web_feed">
  Feed
 </a>
 dan
 <a href="http://en.wikipedia.org/wiki/Scripting">
  Server/Client Side Scripting
 </a>
 :-D . Tapi disini kita nggak akan membahas how-to-program-nya, karena cukup simpel dan caranya bervariasi, asalkan familiar dengan
 <a href="http://en.wikipedia.org/wiki/Web_programming">
  web programming
 </a>
 , maka tidak akan sulit. Kita akan ngebahas logicnya.
</p>
<p style="text-align:left;">
 ![image](http://i247.photobucket.com/albums/gg153/kecebongsoft/scr5.jpg)
</p>
<p style="text-align:left;">
 Pertama, masuk ke Google Blog Search kemudian ketik alamat blog kita dibagian keyword misalnya : "link:kecebongsoft.wordpress.com" kemudian klik Search dan tunggu resultnya. Secara default, dibagian "Published" akan terpilih opsi "Anytime" yang berarti akan menampilkan trackback pada waktu apapun, tapi jika tidak, maka klik terlebih dahulu opsi "Anytime".
</p>
<p style="text-align:left;">
 ![image](/img/wordpress/2008-05-scr3.jpg)
</p>
<p style="text-align:left;">
 Sekarang kita telah mendapatkan hasil dari pencarian Google Blog Search, sekarang tinggal menempelkannya ke website yang kita miliki. Caranya? yaitu dengan memanfaatkan Feed. Google Blog Search menggunakan 2 jenis Feed yaitu
 <a href="http://en.wikipedia.org/wiki/Atom_%28standard%29">
  Atom
 </a>
 dan
 <a href="http://en.wikipedia.org/wiki/RSS">
  RSS
 </a>
 , kali ini kita coba menggunakan RSS dulu, klik link RSS kemudian kita akan diberikan hasil pencarian dalam format RSS. Setelah mendapatkan RSSnya, kita tinggal membuat sebuah script (
 <a href="http://en.wikipedia.org/wiki/PHP">
  PHP
 </a>
 /
 <a href="http://en.wikipedia.org/wiki/JSP">
  JSP
 </a>
 /
 <a href="http://en.wikipedia.org/wiki/Javascript">
  JavaScript
 </a>
 /dll) yang membaca dan melakukan splitting-value ke RSS tersebut untuk akhirnya ditampilkan dalam bentuk terformat (tabel misalnya). Copy dan paste URL dari RSS tersebut dan selipkan didalam script yang kita miliki. Sebagai info, pada PHP v5 kita bisa menggunakan
 <a href="http://my.php.net/manual/en/book.libxml.php">
  XML object
 </a>
 yang telah disediakan untuk melakukan splitting RSS, atau kita bisa menggunakan library extend yang banyak tersebar di internet. Proses splitting RSS ini juga bisa dilakukan di Client Side Script seperti JavaScript. Inilah yang sepertinya dilakukan oleh Wordpress untuk menampilkan blog lain yang memiliki link ke blog kita.
</p>
<p style="text-align:left;">
 Tapi tunggu dulu, beberapa mungkin heran karena setelah beberapa hari/minggu, result Google Blog Search yang awalnya menampilkan link ke blog kita tiba-tiba menghilang, apa sebabnya?.
</p>
<p style="text-align:left;">
 Google Blog Search menggunakan feed di tiap blog untuk mencari link yang menuju ke blog kita. Sekarang bayangkan blog kita adalah blog ABC, dan ada sebuah blog (blog DEF) yang mencantumkan link blog kita didalam postingan terbarunya. Secara otomatis, postingan baru tersebut akan muncul pada list teratas didalam feed blog DEF, dan Google Blog Search akan mendapatkan 1 buah result yang mengarah ke blog ABC, yaitu blog DEF. Seiring dengan waktu, postingan blog DEF kian bertambah, dan postingan yang berisi link blog kita tersebut lama-kelamaan akan menempati urutan terbawah dalam feed blog DEF. Seperti yang kita tahu, feed blog memiliki entry yang dibatasi, biasanya hanya menampilkan 5-15 postingan terbaru. Postingan yang berisi link ke blog kita pada feed blog DEF lama-kelamaan akan menempati urutan terbawah dan pada akhirnya menghilang dari feed karena tenggelam oleh postingan-postingan baru. Itulah kenapa Google Blog Search tidak lagi menampilkannya didalam result.
</p>
![image](http://i247.photobucket.com/albums/gg153/kecebongsoft/scr4.jpg)
<p style="text-align:left;">
 Tapi, dengan sedikit trik dan pengetahuan tentang database dan Server Side Scripting, kita bisa mengakali situasi ini dengan cara membuat sebuah script yang menyimpan semua result Google Blog Search kedalam database kita secara permanen, dengan begini kita tidak perlu khawatir apakah Google Blog Search tidak akan menampilkan result-result lama kembali. Dan dengan cara ini juga kita bisa mendapatkan list lengkap hasil Google Blog Search dari waktu ke waktu. Logikanya cukup mudah, cukup baca RSS hasil pencarian Google Blog Search, split value RSSnya kemudian simpan ke database. Karena ini berhubungan dengan database, jadi kita tidak bisa menggunakan Client Side Scripting seperti Javascript.
</p>
<p style="text-align:left;">
 Dan terakhir, ada yang harus diperhatikan dalam menggunakan teknologi Google Blog Search mungkin tidak bisa sembarangan. Baca baik-baik Terms &amp; Condition, Disclaimer, FAQ, dan semua material hukum yang ada pada Google dan Google Blog Search untuk memastikan apa yang kita lakukan dengan Google Blog Search adalah legal dan jauh dari pelanggaran apapun. Happy coding!
</p>