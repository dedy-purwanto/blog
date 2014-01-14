title:Merakit robot sendiri dengan Bioloid
date:2008-12-28 15:24:54

![image](/img/wordpress/2008-12-b1.jpg)
<a href="http://en.wikipedia.org/wiki/Robotis_Bioloid">
 Bioloid
</a>
adalah
<a href="http://en.wikipedia.org/wiki/Robot_kit">
 robot kit
</a>
yang terdiri dari beberapa part yang bisa kita rakit menjadi robot sesuka kita. Dan robot yang satu ini bukan mainan anak-anak umur 7 tahun, karena part-part yang disediakan cukup teknikal dan butuh pengetahuan yang cukup (tidak harus jenius). Dengan Bioloid, kita bisa merakit robot jenis apa saja, selama parts yang kita miliki mencukupi. Kemudian memprogram gerakan dan sifat robot tersebut menggunakan software yang telah disediakan.&#160; Contoh gerakan yang bisa diaplikasikan adalah transformasi, misalnya bentuk awalnya adalah mobil, kemudian bisa ditransformasi otomatis menjadi robot berdiri.&#160; Bisa terkoneksi langsung dengan PC/Laptop (USB/Wireless) ataupun dengan radio control. Bisa dipasangi kamera hingga laser panas. Kemudian juga ada detektor suara, cahaya, jarak, dsb. Pokoknya dijadiin apa aja bisa :roll:
<!--more-->
Bagaimana cara kerjanya?. Part utama yang menggerakan robot Bioloid adalah Dynamixel, yaitu sejenis R/C servo (dinamo), tapi berbeda dengan R/C servo biasa, Dyamixel bekerja dalam jaringan yang memiliki fungsi feedback. Dengan begitu, seluruh Dynamixel pada Bioloid bisa bekerja sama dengan saling mengirimkan feedback.

[image](/img/wordpress/2008-12-b2.jpg)

Sebagai contoh, untuk membuat tangan robot, maka diperlukan 3 poros, yaitu bahu, siku dan pergelangan tangan. Maka kita memerlukan 3 Dynamixel. Satu diletakan di bahu, di siku dan terakhir di pergelangan tangan. Kemudian untuk melakukan gerakan melambai (misalnya), maka ketiga Dynamixel ini saling berkomunikasi dalam melakukan setiap gerakan agar poros-poros tangan tersebut bisa mensimulasikan gerakan melambai. Simpel kan?. Banyaknya jumlah Dynamixel pada sebuah robot tergantung dari design kita. Anggap saja untuk sebuah tangan/kaki diperlukan 3 dynamixel, maka diperlukan sekitar 12 dynamixel (atau lebih) untuk membuat robot menyerupai manusia. Tapi itu semua kembali pada design yang kita miliki, karena dengan jumlah Dynamixel yang sedikitpun kita tetap bisa membuat robot yang diinginkan asalkan designnya tepat.

[image](/img/wordpress/2008-12-b31.jpg?w=300)

Part selanjutnya yang tidak kalah penting adalah CM-5, ini adalah part utama yang mengontrol semua Dynamixel. Karena ini adalah centralnya, jadi untuk satu robot biasanya hanya butuh 1 buah CM-5. Part ini bisa dibilang sebagai komputer kecil, dimana didalamnya terdapat berbagai macam instruksi yang menggerakan setiap Dynamixel. Kita tidak perlu memusingkan part ini, karena dia bekerja otomatis sesuai instruksi yang diberikan. Cukup meletakannya di robot kita dan menghubungkannya ke semua Dynamixel. CM-5 menerima instruksi dari PC / controller untuk kemudian memberikan perintah kepada Dynamixel untuk bergerak.

[image](/img/wordpress/2008-12-b4.jpg?w=249)

Kemudian komponen selanjutnya adalah software, Bioloid menyertakan software The Behaviour Control Programmer dan Three-Dimensional Motion Editor. Setelah kita merakit robot sesuai design kita, selanjutnya kita menghubungkannya dengan software tersebut untuk membuat gerakan-gerakan dan sifat-sifat robot. Sifat-sifat robot ini contohnya adalah, ketika detektor suara mendeteksi suara sekian dB, maka akan melakukan gerakan-gerakan tertentu, dan lain sebagainya. Kemudian software motion editor juga bisa digunakan untuk membuat gerakan kompleks bagi si robot, sebagai contoh adalah robot mobil yang berubah menjadi prajurit, atau sebaliknya.

[image](/img/wordpress/2008-12-b5.jpg)

Ketiga part inilah yang menjadi kunci utama bioloid. Dengan PC/Laptop, kita nyalakan software yang telah disediakan, lalu hubungkan PC/Laptop kita dengan CM-5 yang ada pada bioloid menggunakan kabel USB yang telah disediakan, kemudian robot bioloid pun siap dioperasikan. Dengan cara kerja sebagai berikut : PC/Laptop mengirimkan instruksi ke CM-5, kemudian CM-5 menerima instruksi lalu memerintahkan Dynamixel untuk bergerak.

Kemudian part yang juga dikontrol oleh CM-5 adalah Sensor Module (AX-S1), part ini difungsikan untuk mendeteksi jarak, mendeteksi suara, dan sebagainya.

Part-part selanjutnya adalah frame, yaitu casing-casing kecil yang bisa ditempelkan dibagian-bagian tubuh si robot, kemudian sekrup, kabel, stiker, dan lain sebagainya.

[image](/img/wordpress/2008-12-b6.jpg?w=300)

Saya rasa Bioloid cocok untuk edukasi pelajar dalam mempelajari prinsip-prinsip robotika serta para hobbyst. Dengan parts dan software yang telah disediakan, kita bisa mendesain robot sesuka kita dan mengaplikasikan gerakan dan sifatnya.

Bioloid sendiri
<a href="http://www.robotis-shop-en.com/shop/step_submain.php?b_code=B20070914045814">
 terjual secara paketan dan terpisah
</a>
. Untuk paket, ada jenis Beginner (pemula) yang berisikan sebuah CM-5, 4 buah Dynamixel, 1 buah sensor module, baterai, power eksternal, CD, manual, dan part-part aksesoris lainnya. Kemudian paket lainnya adalah Comprehensive dan Expert, yang berisikan lebih banyak part dan bisa mengaplikasikan lebih banyak hal. Bioloid juga ada yang dijual terpisah, dimana kita bisa membeli dynamixel dan part-part lainnya sendiri-sendiri.

Harganya?. Untuk Bioloid yang paket Beginner, dijual seharga USD349. Kalau tinggal di Indonesia, mungkin totalnya akan jadi USD420 setelah ditambah ongkos kirim (DHL). Saya pribadi menilai harga ini tidak murah, dan tidak mahal. Tidak murah karena dengan harga tersebut part yang bisa didapatkan tidak banyak (hanya 4 dynamixel, mungkin karna memang Beginner Packet). Dan tidak mahal karena untuk kategori hobyist, harga segini cukup reasonable, dan kita sudah bisa membuat robot dengan mudah tanpa perlu otak super jenius. Bayangkan orang-orang yang membuat robot dari dasar :roll: .

Paket selanjutnya yaitu Comprehensive dijual seharga USD899 dan Expert dijual seharga USD2.999. Tapi saya rasa beginner kit juga sudah cukup untuk muasin hobi sebelum mulai ke tahap advanced.

[image](/img/wordpress/2008-12-b7.jpg?w=300)

Bagaimana? tertarik membuat robot sendiri?. Lihat juga contoh video-video transformasi robot Bioloid yang ada di Youtube. Contohnya
<a href="http://www.youtube.com/watch?v=zK8OjwMdn5I&amp;feature=rec-HM-r2">
 mobil truk yang berubah jadi robot prajurit
</a>
, dan
<a href="http://www.youtube.com/watch?v=aQe0WFJG1K4&amp;feature=related">
 juga ini
</a>
. Atau search saja dengan keyword "
<a href="http://images.google.co.id/images?hl=id&amp;q=bioloid&amp;um=1&amp;ie=UTF-8&amp;sa=N&amp;tab=wi">
 Bioloid
</a>
" di google, banyak sekali info dan video-video keren tentang bioloid. Bagi yang cowok biasanya pasti ngiler liat ginian, ayo nabung :roll:
<a href="http://www.robotis.com/">
 Website Bioloid
</a>