title:Hacking FB, Twitter, Yahoo, dll dengan Firesheep
date:2011-02-23 16:12:16

Firesheep adalah plugin firefox yang bisa mencuri account Facebook, Twitter, Yahoo, dll. &#160;Anda cukup login di wifi terbuka seperti restoran/hotel/sekolah, jalankan Firesheep, dan semua Facebook/Twitter/Yahoo/dll jadi milik Anda. Modalnya hanya Firefox dan WinPcap.

Teknik yang digunakan relatif simple dan sebenarnya bukan hal baru, yaitu
<a href="http://en.wikipedia.org/wiki/Session_hijacking">
 HTTP Session Hijacking
</a>
. Idenya sederhana, Firesheep akan mengoleksi semua
<a href="http://en.wikipedia.org/wiki/HTTP_cookie">
 cookie
</a>
yang bisa diambil, lalu cookie ini akan digunakan sebagai pengenal untuk masuk ke website-website yang telah di-authenticate sebelumnya. Contohnya, jika saya login Facebook, mengetikkan username dan password saya, kemudian login sukses, maka Facebook akan membuat Cookie sebagai tanda pengenal saya. Cookie inilah yang akan dicuri oleh Firesheep.
<!--more-->
Pada tempat-tempat yang menyediakan wifi/hotspot terbuka, semua cookie yang aktif pada dasarnya tersedia dan bisa diambil. Menyedihkan kan?, dengan begitu kita bisa hack siapapun yang sedang aktif di area tersebut.

Cara menggunakan Firesheep relatif sederhana. Setelah instalasi, pertama-tama jalankan Firefox, lalu Firesheep akan muncul di sidebar. Setelah itu klik tombol Start Capturing. Maka Firesheep akan mulai menangkap cookie-cookie yang berterbangan di area wifi. Begitu dapat, Firesheep akan menampilkannya di Sidebar. Sebagai contoh, jika ada yang sedang login Facebook, maka Firesheep akan menampilkan Facebooknya di sidebar firefox kita, dan ketika kita meng-klik Facebook tersebut, kita secara otomatis sudah login sebagai orang yang memilik account Facebook tersebut!.

Silahkan lihat langkah-langkah penggunaan Firesheep ini, pertama kita jalankan Firefox, dan Firesheep muncul di sidebar:

![image](/img/wordpress/2011-02-firesheep1.png)

Lalu setelah meng-klik Start Capturing, semua orang yang sedang login Twitter, Facebook, Google Mail, Yahoo, dll akan tertangkap di Firesheep kita, dan akan muncul di sidebar Firefox:

![image](/img/wordpress/2011-02-firesheep2.png)

Itu saja, kita bisa memilih akan mencuri account siapa, tinggal klik icon-icon yang ada di Sidebar, lalu secara otomatis kita telah login sebagai mereka, kita bisa melakukan apapun, mengganti email, password, apapun:

![image](/img/wordpress/2011-02-firesheep3.png)

Kenapa Firesheep bisa mencuri data semudah itu?. Ada beberapa alasan, yang pertama adalah karena port yang digunakan layanan web sekarang masih relatif tidak aman, yaitu HTTP (80), yang mana tidak banyak enkripsi yang dilakukan oleh port ini. Alasan kedua adalah, banyak layanan web yang tidak melakukan autentikasi lanjutan setelah login. Cookie yang mereka simpan pada dasarnya "telanjang" tanpa perlindungan apapun, sehingga siapapun bisa mencurinya. Alasan ketiga adalah karena cookie ini dishare pada 1 wifi terbuka, yang secara otomatis akan memiliki public IP yang sama. Sehingga layanan web seperti Facebook dan Twitter akan menganggap siapapun user yang memiliki Cookie dan public IP yang sama adalah orang yang sama.

Saya pribadi mengatasinya dengan beberapa cara, yang paling mudah adalah: Jangan pernah login di tempat terbuka!. Kalau kita merasa account kita cukup penting, maka rawatlah dengan benar, cukup login di tempat-tempat yang bisa dipercaya, seperti rumah, warnet (jangan lupa periksa keylogger dan worm), atau tempat-tempat aman lainnya. Kemudian biasakan membuka halaman web seperti Facebook dan Twitter dengan port HTTPS, gunakan url seperti ini:
<blockquote>
 <strong>
  https://www.facebook.com
 </strong>
</blockquote>
Pada post selanjutnya saya akan bahas tentang fitur facebook yang bisa mengamankan account kita dari hacking. Juga ada software yang bisa melakukan enkripsi lanjutan sehingga data kita aman.&#160;Saya sendiri sudah aware dengan rilis pertama Firesheep sejak oktober 2010, namun karena beberapa hal, baru sempat mengulasnya sekarang. Mudah-mudahan dengan mengetahui tool seperti ini kita semakin aware untuk tidak terlalu aktif di wifi terbuka.
<a href="http://codebutler.github.com/firesheep/">
 Download Firesheep Disini
</a>
<a href="http://codebutler.com/firesheep">
 Lihat ulasan Firesheep
</a>