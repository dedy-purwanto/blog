title:Mengenal Google Channel API - Part 1
date:2011-01-29 18:46:45

Di dalam
<a href="http://code.google.com/appengine/">
 Google Application Engine (GAE)
</a>
, dikenal sebuah service yg disebut
<a href="http://code.google.com/appengine/docs/python/channel/overview.html">
 Channel API
</a>
. Channel API memungkinkan kita untuk membuat koneksi yang lebih realtime antara aplikasi dan GAE server. Channel API membuat kita bisa mengirimkan pesan spesifik ke client tertentu. Contohnya, jika aplikasi kita sedang melayani 1000 client, maka kita bisa mengirimkan pesan yang hanya akan diterima oleh client tertentu. Aplikasi yang cocok menggunakan Channel API contohnya aplikasi chat, multiplayer game, dan aplikasi lainnya yang sifatnya kolaboratif.
<strong>
 Kenapa pakai Channel API?
</strong>
Kita pernah membuat aplikasi realtime yang simpel, contohnya chat. Dimana semua user berkumpul di satu chat server, lalu pesan chat akan terkirim ke semua user. Solusi yang paling simpel adalah menggunakan polling. Dimana client (AJAX) akan melakukan frequent request ke server untuk meminta data, lalu data yang didapat akan di download ke client. Jika ada 1000 user di chat server, dan polling dilakukan setiap 3 detik, maka tiap 3 detik server akan menghandle 3000 request, ini belum termasuk dengan post processing, seperti regex, text formatting, dll. Padahal dalam 3 detik tersebut data chat bisa saja sama dengan yang sebelumnya. Bayangkan berapa banyak resource server yang terpakai jika harus memakai solusi polling?.
<!--more-->
Berbeda dengan Channel API, server bisa mengatur kapan pesan chat harus dikirimkan. Jika tidak ada chat yang baru, server bisa idle sampai ada user yang mengirim pesan, kemudian baru pesan tersebut dikirimkan ke semua client. Jika ada 1000 orang di chat server, dan tidak ada yang mengirim pesan chat selama 5 menit, maka server tidak akan melakkukan apapun, kemudian jika ada yang mengirim pesan di menit ke enam, barulah server mengirimkan pesan tersebut ke semua client.

Kelebihan lainnya dari Channel API adalah, tersedianya "channel" unik untuk setiap client. Ini memungkinkan kita untuk mengirim pesan ke client tertentu. Pada kasus chat diatas, saya bisa mengirim private message ke user-user tertentu.
<strong>
 Implementasi sederhana Channel API
</strong>
Sebelum bergerak ke code, hakikat paling dasar Channel API adalah koneksi 2 arah. Ini berarti, Channel API hanya bisa mengirim pesan ke 1 client untuk setiap eksekusinya. Hingga saat ini Channel API masih terbilang muda dan belum punya fungsi built-in broadcast message.

Ada beberapa istilah penting di Channel API yang harus kita pahami:
<ol>
 <li>
  <strong>
   Server
  </strong>
  , adalah aplikasi yang kita host di GAE.
 </li>
 <li>
  <strong>
   Client
  </strong>
  , adalah browser. Jika di komputer ada dua browser/tab/window yang membuka aplikasi kita, maka akan terhitung sebagai 2 client.
 </li>
 <li>
  <strong>
   Channel
  </strong>
  , adalah "pipa" eksklusif yang disediakan bagi setiap client ke server. Jika kita buka aplikasi GAE dengan 2 browser, maka kita punya 2 channel. Sehingga jika aplikasi kita hanya mengirimkan pesan ke channel pertama, channel kedua tidak akan dapat, begitu juga sebaliknya.
 </li>
 <li>
  <strong>
   Client ID
  </strong>
  , adalah serangkaian kata kunci unik yang kita susun untuk membuat sebuah channel. Contohnya, kita bisa membuat sebuah channel berdasarkan username.
 </li>
 <li>
  <strong>
   Token
  </strong>
  , adalah hash dari Client ID, digunakan oleh client untuk melakukan koneksi dan listening ke server.
 </li>
 <li>
  <strong>
   Message
  </strong>
  , adalah isi dari setiap pesan yang dikirimkan dari atau untuk client/server.
 </li>
</ol>
Kita akan bahas lebih jelas tentang istilah-istilah diatas dibagian implementasi, mekanisme Channel API adalah sebagai berikut:
<ol>
 <li>
  Server membuat satu channel unik yang hanya boleh dipakai oleh 1 client. Contoh untuk aplikasi chat, kita akan buat channel berdasarkan username. Misalkan createChannel("dedi_purwanto");. "dedi_purwanto" adalah Client ID.
 </li>
 <li>
  Kemudian fungsi tersebut akan menghasilkan sebuah hash (misal: "abc123xyz"), yang kita sebut dengan Token. Token ini harus di pass ke javascript.
 </li>
 <li>
  Client (javascript) akan membuka koneksi Channel API ke server dengan menggunakan token yang sudah dikirimkan tadi. Ketika javascript membuka koneksi dengan token tadi, server akan mencocokan dengan semua Client ID yang terdaftar di server, jika ditemukan yang cocok (yaitu "dedi_purwanto"), maka koneksi javascript tadi adalah valid, dan client akan mulai melakukan listening ke server terhadap semua pesan yang masuk/keluar.
 </li>
 <li>
  Client dan server melakukan listening.
 </li>
</ol>
Well, sementara itu dulu untuk pengenalan channel API, dibagian selanjutnya akan dijelaskan tentang contoh code untuk koneksi dua arah, serta solusi untuk broadcast message, stay tuned :D
<a href="http://kecebongsoft.wordpress.com/2011/01/30/mengenal-google-channel-api-part-2">
 <em>
  (Bersambung di Part 2)
 </em>
</a>