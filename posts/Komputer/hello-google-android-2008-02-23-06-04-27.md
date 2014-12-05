title:Hello, Google Android!
date:2008-02-23 06:04:27

Huhu, telat ya reviewnya, Android udah keburu mo rilis. Oke, buat yang baru liat, Android adalah software stack untuk perangkat bergerak yang berisi sistem operasi. Beberapa fasilitas yang ditonjolkan seperti Application Framework, DVM yang optimized untuk perangkat bergerak, integrated browser (klo ini udah umum ya hehe), Optimized graphics (lewat Java yang bisa HW Accel menggunakan OpenGL). SQLite untuk DBMSnya, Bluetooth, EDGE, 3G, Wifi, Camera, GPS, kompas, accelerometer, banyak deh..
![image](/img/wordpress/2008-02-helloandroid1.png)
Sebelum perangkat benerannya keluar, emulator dan SDKnya udah nongol duluan. Belakangan ini lagi asik nyobain SDKnya. Berjalan diatas Linux Ubuntu Gutsy Tribe (Ubuntu 7.10) + Eclipse sebagai IDEnya (Integrated Development Environment).
<!--more-->
SDKnya sendiri memboyong 2 Skin dengan masing-masing 2 layout untuk tiap skinnya, proses integrasi ke eclipse cukup mudah, tinggal update package dan setting beberapa konfigurasi untuk emulatornya. Here's the sample of developing Android application in Eclipse:
<a href="http://kecebongsoft.files.wordpress.com/2008/02/helloandroid2.png" title="helloandroid2.png">
 ![image](/img/wordpress/2008-02-helloandroid2.thumbnail.png)
</a>
Proses developmentnya sebenarnya nggak berat, tapi pas tes running application, blew.. lemotnya nyaingin emulator J2ME. Padahal udah nyiapin 8GB swap partition. Tapi wajar aja sih, emulator kan bener2 bisa dibilang OS yang berjalan diatas OS. Well, awal-awal running mesti nunggu dia boot dulu, nggak lama sih, paling2 15 detik.
<a href="http://kecebongsoft.files.wordpress.com/2008/02/helloandroid3.png" title="helloandroid3.png">
 ![image](/img/wordpress/2008-02-helloandroid3.thumbnail.png)
</a>
Setelah boot, OS akan langsung ngeredirect ke aplikasi yang kita buat (lihat gambar pertama), dan klo klik tombol Home, maka akan muncul main menunya :
<a href="http://kecebongsoft.files.wordpress.com/2008/02/helloandroid4.png" title="helloandroid4.png">
 ![image](/img/wordpress/2008-02-helloandroid4.thumbnail.png)
</a>
Wokeh, menu-menu yang lain terlihat umum kecuali menu Maps, jadi langsung aja deh kita lihat apa isinya. Ternyata sama seperti Google Map (Hybrid View). Dan ini realtime.. huhuhu keren juga :
<a href="http://kecebongsoft.files.wordpress.com/2008/02/helloandroid5.png" title="helloandroid5.png">
 ![image](/img/wordpress/2008-02-helloandroid5.thumbnail.png)
</a>
Puas berjalan2 dengan Maps, sekarang kita tes integrated browsernya, ini ke Google :
<a href="http://kecebongsoft.files.wordpress.com/2008/02/helloandroid7.png" title="helloandroid7.png">
 ![image](/img/wordpress/2008-02-helloandroid7.thumbnail.png)
</a>
Setelah puas berkeliling dengan lingkungan OSnya, nemu satu lagi menu tambahan yang berguna banget buat development phase. yaitu Dev Settings. Disini kita bisa watch activity dan resource yang termakan oleh Android, setting berbagai macam konfigurasi software, dll.
<a href="http://kecebongsoft.files.wordpress.com/2008/02/helloandroid8.png" title="helloandroid8.png">
 ![image](/img/wordpress/2008-02-helloandroid8.thumbnail.png)
</a>
Well, masih banyak lagi item-item di android, seperti Demo App yang menampilkan demo animasi 3D dan aplikasi-aplikasi yang sudah berjalan di atas andoird (Alarm, Activity, dll). Kalau melirik SDKnya yang cukup mudah dipelajari, dukungan DBMS yang bagus, serta banyak feature lainnya, Android cukup kompetitif dari segi feature. Namun perlu juga direview handset aslinya nanti, apakah sebaik emulatornya atau tidak.

Bagi yang familiar dengan java, pasti sangat mudah untuk beradaptasi dengan Android SDK (karena juga menggunakan Java). Huhu, biar telat reviewnya, tapi nggak nyesal juga, mulai utak-atik SDKnya lagi nih, sapa tau bisa bikin game buat handset ini dan dijual ke Google.. hehe..
