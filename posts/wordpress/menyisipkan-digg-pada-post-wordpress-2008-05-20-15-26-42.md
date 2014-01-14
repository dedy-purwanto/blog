title:Menyisipkan Digg pada post Wordpress
date:2008-05-20 15:26:42

![image](http://i247.photobucket.com/albums/gg153/kecebongsoft/digg.jpg)
Tahu
<a href="http://www.digg.com/">
 Digg
</a>
? Ini adalah situs sosial dimana kita bisa mengirimkan link yang kita suka (berita/video/dll) dan link tersebut bisa divote oleh orang lain, vote yang tertinggi akan muncul dihalaman front-page Digg. Singkatnya, Digg adalah situs yang menampilkan link "terlaris" pilihan voter, layanan seperti ini sangat efektif dan berguna agar kita bisa memilih sebuah link yang benar-benar bagus, karena setiap link adalah murni pilihan voter.

Wordpress sendiri sebenarnya sudah dari tahun 2007 yang lalu telah membolehkan pemakainya untuk menyisipkan tombol Digg disetiap postingan yang dibuat, tapi mungkin masih jarang digunakan. Berikut ini cara menyisipkan Digg kedalam postingan kita :
<!--more-->
<ol>
 <li>
  Pertama kita harus memposting link-link yang akan kita "Digg", untuk itu kita harus melakukan registrasi dulu di website tersebut, registrasinya cukup mudah.
 </li>
 <li>
  Setelah registrasi, login lalu klik link "Submit New" yang ada di kanan atas.
 </li>
 <li>
  Masukan link yang ada pada postingan blog, misalnya : http://kecebongsoft.wordpress.com/2008/05/20/cross-compiling-aplikasi-opengl-melalui-linux/
 </li>
 <li>
  Isi kategori link dan lain sebagainya.
 </li>
 <li>
  Tunggu beberapa saat, kemudian biasanya Digg akan memverifikasi apakah link tersebut sudah ada atau belum, klik button "This is Original" yang ada dibagian bawah page.
 </li>
 <li>
  Setelah itu kita akan mendapatkan link postingan blog kita yang telah digenerate oleh Digg, misalkan : http://digg.com/programming/Cross_Compiling_aplikasi_OpenGL_melalui_Linux
 </li>
 <li>
  Edit postingan blog yang telah ada, yakni "Cross Compiling Aplikasi OpenGL Melalui Linux", sisipkan kode
  <strong>
   <code>
    [
   </code>
   <code>
    digg=http://digg.com/url_to/story_on_digg]
   </code>
  </strong>
  dimana urlnya adalah url yang telah digenerate oleh Digg tadi.
 </li>
 <li>
  Save, lalu lihat postingan yang telah diedit tadi, tombol Digg akan muncul dan visitor siap untuk memvoting postingan tersebut.
 </li>
</ol>
Selain Digg, layanan sosial lainnya seperti facebook juga memiliki fitur submit link seperti ini. Di Indonesia juga kalau tidak salah sudah ada situs-situs sosial yang mulai mengikuti jejak Digg :-D

[digg=http://digg.com/programming/Menyisipkan_Digg_pada_post_WordPress]
