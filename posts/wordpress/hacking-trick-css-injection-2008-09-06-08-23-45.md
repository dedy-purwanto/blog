title:Hacking Trick : CSS Injection
date:2008-09-06 08:23:45
status:draft

Sebelum saya ngebahas ini, <u>please note that this is just a learning material, and hacking is not a child's play</u>. When you broke a site, it's not cool or smart or genius, it's a crime. Buat saya pribadi hacking adalah proses pembelajaran (mencari bug, fixing code, optimizing) bagi si coder untuk meng-involve teknik/trik programming baru. 

Kali ini saya mau ngebahas gimana lubang pada application layer bisa dimanfaatkan buat ngemodifikasi style CSS (Cascading Style Sheet) pada sebuah elemen yang menggunakan tag DIV atau SPAN. Pada prakteknya nanti, kita bisa mengubah tampilan sebuah elemen dengan mengubah style CSS-nya lebih dari yang diperbolehkan oleh situs tersebut. Yang lebih menyeramkan lagi, kita bisa mengubah style tersebut sedemikian rupa hingga tampilan situs secara keseluruhan berubah (atau bisa disebut deface?).<!--more-->

<u><b>Index</b></u>
<ol>
<li><a href="#blogkonten1">Apaan tuh injection?</a></li>
<li><a href="#blogkonten2">Contoh dasar injection</a></li>
<li><a href="#blogkonten3">CSS injection</a></li>
<li><a href="#blogkonten4">Sampel kode</a></li>
<li><a href="#blogkonten5">Demo injection</a></li>
<li><a href="#blogkonten6">Dangerous CSS Injection</a></li>
<li><a href="#blogkonten7">Cara ngatasinnya?</a></li>
<li><a href="#blogkonten8">Kesimpulan</a></li>
</ol>

<b><a name="blogkonten1">Apaan tuh injection?</a></b>
Injection memiliki banyak arti. Dalam kasus ini injection bisa saya samakan dengan <a href="http://en.wikipedia.org/wiki/SQL_injection">SQL injection</a>, yaitu exploitasi sekuriti yang terjadi pada database layer. Tapi berhubung yang dibahas disini adalah CSS injection (yang tidak punya database layer), maka saya sebut saja application layer. Mungkin ada yang bertanya-tanya seperti ini:

<blockquote>
Kok application layer? kan CSS berhubungan dengan tampilan, jadi harusnya presentation layer dong..
</blockquote>

Ya iya sih, masa ya iya dong.. Ups. Maksud saya, memang CSS berhubungan langsung dengan presentation layer. Tapi pada prakteknya nanti, setiap stylesheet yang masuk akan diproses dulu pada application/business layer (in this case : PHP/ASP), untuk kemudian ditampilkan dalam bentuk CSS.

Bentuk eksploitasinya (secara dasar) adalah dengan memanfaatkan input yang salah/tidak seharusnya dari user, dan tidak dapat difilter dengan benar oleh application layer, sehingga input tersebut tidak dapat dieksekusi, or at least dieksekusi dengan cara yang tidak seharusnya. Saat melakukan hacking, si user memanfaatkan kelemahan ini untuk menginput data yang salah, menggunakan karakter single quote dan double quote. Dengan begitu user bisa bebas menambahkan kode internal apapun yang dia inginkan. Sebagai contoh pada SQL, saya bisa memasukan query tambahan seperti Update, Delete, Truncate, Insert, dsb. Dalam CSS, user bisa menambahkan elemen lain (selain default) seperti Color, Font-Family, Font-Size, Background, Width/Height, dsb.

<b><a name="blogkonten2">Contoh dasar injection</a></b>
Untuk injection versi SQL, contoh kasus sederhananya adalah seperti ini : Kita punya tabel yang menyimpan daftar username dan password (tabel user_data). Pada tabel tersebut terdapat kolom user (varchar) dan pwd (varchar) yang menyimpan informasi username dan password bagi tiap user. Anggap saja saya punya sebuah data pada tabel tersebut sebagai berikut:

<blockquote>
<b>user</b> : admin
<b>pwd</b> : 123
</blockquote>

Kemudian saya ingin agar user tersebut bisa login pada halaman web yang saya punya. Maka saya gunakan kode berikut:

[sourcecode lang='php']
$form_user = $_POST['user'];
$form_pwd = $_POST['pwd'];

$query = "SELECT * FROM user_data WHERE user='". $form_user . "' AND pwd='". $form_pwd ."' ";
if(mysql_query($query)){ // hanya contoh, pada prakteknya tidak seperti ini
     echo "Login success.";
}else{
     echo "Login failed.";
}
[/sourcecode]

Variabel form_user dan form_pwd berasal dari form HTML dasar yang saya buat sebelumnya. Dengan begini saya sudah bisa login dengan mengisi <b>admin</b> pada kolom user dan <b>123</b> pada kolom password. Saat saya isi dengan data login yang ada, maka variabel $query akan menghasilkan:

<blockquote>
SELECT * FROM user_data WHERE user='admin' AND pwd='123'
</blockquote>

Dan login pun berhasil, query akan menghasilkan nilai true karena semua statement bisa dikerjakan (karena datanya sesuai dengan yang di database). Tapi kelemahan pada kode diatas bisa dimanfaatkan untuk menyisipkan query tambahan. Sebagai contoh, jika saya login dengan data ini:

<blockquote>
<b>Username</b> : test' or 'saya'='saya
<b>Password</b> : test' or 'saya='saya
</blockquote>

Maka variabel $query akan menghasilkan:

<blockquote>
SELECT * FROM user_data WHERE user='test' or 'saya'='saya' AND pwd='test' or 'saya='saya'
</blockquote>

Query diatas juga akan menghasilkan nilai true, karena semua statement bisa dikerjakan, meskipun datanya tidak sama dengan yang didatabase. Kenapa bisa begitu? Coba lihat urutan prosesnya sebagai berikut:

<blockquote>
$form_user = test' or 'saya'='saya
$form_pwd = test' or 'saya='saya
user = '$form_user'
user = '<b>test' or 'saya='saya</b>'
pwd = '$form_pwd'
pwd = '<b>test' or 'saya='saya</b>'
query = SELECT * FROM user_data WHERE user='test' or 'saya'='saya' AND pwd='test' or 'saya='saya'
</blockquote>

Dengan begini, saya bisa masuk login kehalaman web tersebut tanpa harus tahu data login siapapun. Saya bahkan bisa menjalankan perintah lain seperti Update, Drop, Truncate, dsb. Karena tidak ada yang error pada query diatas, hanya saja eksekusinya berjalan dengan tidak seharusnya (tidak sesuai rule aplikasi yang dibuat). Simple thought, but it's very dangerous :roll:

<b><a name="blogkonten3">CSS injection</a></b>
Nah, dari contoh SQL injection diatas, sebenarnya bisa kita aplikasikan ke tempat lain, yaitu CSS. Pernah browsing ke situs-situs yang punya form text dimana font/warna/fontsize-nya bisa dimodifikasi?. Terkadang ada saja lubang pada form tersebut yang bisa dimanfaatkan untuk menjalankan CSS injection. Metodenya kurang lebih sama yaitu menyisipkan kode tambahan dengan tanda pemisah, jika pada MySQL injection tanda pemisah tersebut berupa single quote dan double quote, maka pada CSS tanda pemisah tersebut adalah semicolon "<b>;</b>" (titik koma).

<b><a name="blogkonten4">Sampel kode</a></b>
Kasusnya seperti ini. Ada sebuah form (misalnya, form komentar) yang punya fasilitas untuk mengganti warna tulisan, atau mengganti tipe tulisan, atau juga mengganti besar tulisan. User bisa memilih warna/tipe/besar tulisan tersebut dengan memilih salah satu item pada dropdown yang disediakan. Misalkan untuk besar tulisan, entry-entry dropdown tersebut adalah "8px", "12px", dan "14px". Ini membuka celah bagi kita untuk mengganti value tersebut dan ada kemungkinan pada saat ditampilkan nanti, akan tampil sesuai dengan value yang kita ubah.

Dari kasus tersebut, pertama kita contohkan form HTMLnya dulu:

[sourcecode lang='html']
<form method='post' action='komentar.php'>
     Komentar : <textarea name='komentar'></textarea><br />
     Besar Font :
     <select name='besar_font'>
          <option value='8px'>8 pixel</option>
          <option value='12px'>12 pixel</option>
          <option value='14px'>14 pixel</option>
     </select>
     <br />
     <input type='submit' value='Kirim' />
</form>
[/sourcecode]

Pada source tersebut, kita punya dua kolom yaitu Komentar dan Besar Font. Disitu terdapat option-option yang berisi value font size dalam pixel. Kita akan menampilkan komentar yang terkirim dengan besar font yang telah dipilih oleh si pengirim. Kode dasar untuk menampilkannya adalah sebagai berikut (dalam PHP) :

[sourcecode lang='php']
$komentar = $_POST['komentar'];
$besar_font = $_POST['besar_font'];

// Bagi yang heran kenapa saya tidak ngeblok karakter single/double quote, karena ini cuma demo CSS injection

echo "<div style='font-size:$besar_font'>$komentar</div>";
[/sourcecode]

Source diatas akan menampilkan komentar yang terkirim menggunakan elemen DIV (atau SPAN juga boleh). Saat user mengisi kolom komentar dengan kata "<b>tes aja</b>" dan kolom besar font dengan nilai "<b>12px</b>". Maka output yang dihasilkan adalah sebagai berikut:

Output HTML:
[sourcecode lang='html']
<div style='font-size:12px'>tes aja</div>
[/sourcecode]

Output web:
<blockquote>
<div style='font-size:12px'>tes aja</div>
</blockquote> 

Dengan begini user bisa memilih besar font yang dia suka, bisa juga ditambahkan dengan pilihan warna font dan tipe font. Tapi script PHP tersebut memiliki kelemahan yang bisa dimanfaatkan user untuk mengisi nilai yang salah, contoh:

<blockquote>
Komentar : tes aja
Besar Font : 12px;font-weight:bold;text-decoration:underline overline;
</blockquote>

Maka saat form tersebut dikirim, output yang dihasilkan adalah:

Output HTML:
[sourcecode lang='html']
<div style='font-size:12px;font-weight:bold;text-decoration:underline overline;'>tes aja</div>
[/sourcecode]

Output web:
<blockquote>
<div style='font-size:12px;font-weight:bold;text-decoration:underline overline;'>tes aja</div>
</blockquote>
 
Sebelum saya jelaskan kenapa user bisa mengisi dengan value tersebut padahal kolomnya berbentuk dropdown list, kita bahas dulu kenapa style CSS diatas bisa dieksekusi dan mengubah style elemen SPAN yang ada.

Syntax untuk tiap baris CSS dipisahkan oleh tanda semicolon, jika ada yang sering main dengan file stylesheet, pasti sering membuat kode seperti ini (contoh):

[sourcecode lang='css']
.classname{
     background-color:#000000;
     border:1px solid black;
     font-size:12px;
     /* dan seterusnya..... */
}
[/sourcecode]

Seperti yang kita <s>tonton (emang tipi??)</s> lihat, setiap baris dipisahkan dengan tanda semicolon. Jika kita ingin memasang class tersebut pada sebuah elemen HTML, maka cukup beri attribut "class" yang nge-assign nama class tersebut. Tapi jika style pada elemen HTML tidak menggunakan class, melainkan langsung didefinisikan di elemen tersebut, maka tiap style dipisahkan dengan tanda semicolon tanpa harus mengganti baris seperti pada file stylesheet. Karena itulah output form yang ada diatas tadi bisa dieksekusi meskipun terdapat beberapa sytle dalam satu baris. Lalu kenapa pada value yang pertama (12px) tidak disertakan atribut font size? Karena atribut font size adalah atribut default yang digunakan pada output (lihat kode PHP sebelumnya yang digunakan untuk output), jadi cukup kita isi nilainya saja (dalam pixel/point).

Sekarang gimana caranya user mengganti value dari kolom besar font tadi? padahal kolom tersebut bentuknya dropdown list. Cara pertama adalah dengan menyisipkan javascript pada address bar (atau dikenal dengan istilah <a href="http://en.wikipedia.org/wiki/Cross-site_scripting">XSS</a>), lalu mengeksekusinya dengan menekan enter. Cara kedua adalah memodifikasi form yang ada dengan membuat salinan halaman HTML tersebut ke komputer lokal, kemudian membukanya pada browser yang sama (tanpa menutup halaman asli) agar bisa "menumpang" session ID milik halaman aslinya.

Untuk cara pertama (javascript). Kita lihat pada form diatas, elemen dropdown diberi nama besar_font. Elemen ini akan kita ubah valuenya dengan menggunakan javascript. Sintaksnya adalah sebagai berikut:

[sourcecode='html']
javascript:document.forms[0].besar_font.options[0]=new Option("Modified 1","12px;font-weight:bold;text-decoration:underline overline",true,true);alert(document.forms[0].besar_font.value);
[/sourcecode]

Kode diatas akan meng-overwrite item pertama pada besar font, dimana judulnya adalah "Modified 1", isinya berupa style yang tertera diatas. 2 parameter selanjutnya (true,true) menandakan bahwa option itu akan langsung terpilih dan juga punya atribut defaultSelected. Hirarki kolom tersebut ada di document-&gt;forms[0]. Angka 0 (nol) digunakan sebagai index form, nol berarti form tersebut adalah form awal / paling pertama yang ada di dokumen HTML, jika ada satu form lain sebelum form tersebut, maka nol diganti menjadi 1 (satu), itu juga berlaku untuk options[0]. Disitu juga disertakan fungsi alert untuk memastikan apakah kode kita dieksekusi dengan sukses, jika alert tidak muncul, maka ada yang salah dengan kode pertama. Cara mengeksekusinya, hapus url pada address bar browser, lalu copy/paste kode javascript diatas dalam satu baris, kemudian tekan enter.

Cara kedua adalah dengan menyimpan salinan halaman HTML-nya ke komputer lokal. Ini jauh lebih mudah karena kita bisa mengganti elemen dropdown tersebut menjadi textarea/textfield, kemudian tinggal mengetik nilai yang kita inginkan, tanpa harus mengulang-ulang menggunakan javascript seperti cara pertama. Caranya cukup save as halaman HTMLnya, kemudian ubah elemen dropdown menjadi textfield kosong. Untuk mengeksekusinya, jangan tutup halaman aslinya, kemudian buka halaman salinannya pada browser yang sama. Kenapa harus begitu?, terkadang ada situs yang mengharuskan user login terlebih dahulu sebelum mengirimkan komentar. Saat user telah login, server menyimpan session ID si user dan menandainya dengan status login (pada browser yang sedang digunakan). Inilah yang kita manfaatkan agar kita bisa mengirimkan komentar tanpa login (karena halaman salinan statusnya adalah halaman offline). Kita juga perlu mengubah atribut "action" pada form dari "komentar.php" menjadi "namadomain.com/komentar.php", karena form tersebut akan dikirim ke server.

<b><a name="blogkonten5">Demo injection</a></b>
Disini saya sertakan form demo CSS Injection. Silahkan masuk ke <a href="http://apayach.com/files/cssinject/form.html">halaman ini</a> untuk membuka form HTML yang kita buat tadi. Untuk mengetes injection menggunakan javascript, copy paste kode javascript yang tadi ke address bar lalu tekan enter. Jika ada pesan yang menampilkan isi style CSS yang telah diubah, berarti kode berjalan dengan sukses. Jika tidak, berarti ada yang salah dengan kode pertama, ini bisa dikarenakan oleh kompatibilitas browser, ada beberapa browser yang punya fungsi sendiri untuk mengubah nilai pada dropdown. Saat ini saya menggunakan Firefox 3 (Linux) untuk mengetesnya. Jika kode berjalan sukses, maka item pertama pada dropdown besar font akan berubah menjadi "Modified 1". Untuk melihat hasilnya, klik tombol Kirim. Silahkan lihat-lihat referensi di internet tentang fungsi javascript untuk memodifikasi element SELECT/dropdown pada browser-browser spesifik

Untuk mengetes injection dengan cara kedua, save halaman form ke komputer lokal, kemudian ubah atribut action pada file form.html dari "komentar.php" menjadi "http://apayach.com/files/cssinjection/komentar.php". Kemudian tinggal mengganti elemen besar_font dari SELECT ke TEXTAREA atau textfield biasa agar memudahkan kita mengetik style CSSnya. Tidak perlu membukanya di browser yang sama karena halaman ini tidak membutuhkan login untuk mengirim komentar.

<b><a name="blogkonten6">Dangerous CSS Injection</a></b>
Contoh modifikasi stylesheet diatas hanyalah dasar dari CSS Injection. Bayangkan jika trik ini ada ditangan orang yang lihai bermain CSS. Sebagai contoh kita lihat kode CSS ini:

[sourcecode lang='html']
92px;color:#FF0000;font-weight:bold;background-color:black;text-align:center;width:1500px;height:1000px;position:absolute;left:0px;top:0px;
[/sourcecode]

Untuk mencobanya, gunakan stylesheet tersebut di halaman demo CSS injection yang tadi (tetap satu baris).  Biar cepat, coba pakai metode javascript saja. Isi kolom komentar lalu tekan kirim, kemudian lihat hasilnya.. saya tungguin ya..

*menunggu pembaca balik dari halaman demo CSS injection*

Dah balik? Kelihatan nggak hasilnya?. Mengerikan bukan :roll: . Style diatas mengganti besar font, warna font, background elemen (DIV), posisi teks, lebar dan tinggi elemen (DIV), posisi elemen DIV yang absolute (tidak bergantung pada elemen lain), serta posisi left dan top elemen (0px,0px).

Belum lagi kalau mau lebih seram, bisa pasang background berupa gambar, entah gambar apa saya nggak mau bilang ah :-p . That was scary..

<b><a name="blogkonten7">Cara ngatasinnya?</a></b>
Sekarang gimana cara ngatasin biar web kita nggak jadi korban CSS Injection, saya kopi paste lagi script untuk nampilin output tadi :

[sourcecode lang='php']
$komentar = $_POST['komentar'];
$besar_font = $_POST['besar_font'];

// Bagi yang heran kenapa saya tidak ngeblok karakter single/double quote, karena ini cuma demo CSS injection

echo "<div style='font-size:$besar_font'>$komentar</div>";
[/sourcecode]

Sekarang untuk input besar_font, kita hanya memerlukan value pertama, yaitu besar font dalam satuan pixel/point. Tiap style dipisahkan oleh tanda semicolon. Jadi untuk menangkap value pertama cukup mudah : ambil semua karakter sebelum tanda semicolon pertama muncul. Caranya? macam-macam, disini saya contohkan cara yang paling mudah (meskipun nggak bisa dibilang keren hahaha..).

Kita pecah variabel besar_font menjadi array, pembaginya adalah tanda semicolon. Kemudian, ambil entry pertama array tersebut, lalu overwrite variabel besar_font dengan entry tersebut. Berikut contoh kodenya:

[sourcecode lang='php']
$komentar = $_POST['komentar'];
$besar_font = $_POST['besar_font'];
    
$besar_font = explode(";",$besar_font); // pecah menjadi array
$besar_font = $besar_font[0]; // ambil nilai array yang pertama saja

echo "<div style='font-size:$besar_font'>$komentar</div>";
[/sourcecode]

Dengan begitu, style-style selanjutnya yang ada pada semicolon setelah style pertama tidak akan dieksekusi. Tapi, kode diatas masih memiliki kelemahan, karena saya masih bisa mengubah nilai pertama dengan bebas. Dalam contoh ini adalah besar font, saya masih bisa mengubah besar font menjadi 80px, 92px, atau 100px (tidak masuk dalam daftar dropdown list). Untuk mengatasinya, kita buat array yang menyimpan besar font apa saja yang diperbolehkan, kemudian kita cek apakah besar font yang dimasukan user ada dalam daftar besar font yang kita perbolehkan ada atau tidak. Jika ada, maka aman. Jika tidak ada, maka kita ubah besar font yang dimasukan user menjadi besar font pertama yang ada di daftar kita. Berikut contoh sourcenya:

[sourcecode lang='php']
$komentar = $_POST['komentar'];
$besar_font = $_POST['besar_font'];
    
$font_size_allowed = array("8px","12px","14px"); // daftar besar font yang diperbolehkan
$besar_font = explode(";",$besar_font); // pecah menjadi array
$besar_font = $besar_font[0]; // ambil nilai array yang pertama saja

// jika $besar_font ada di daftar font_size_allowed, maka aman. Jika tidak, set nilai $besar_font ke nilai pertama yang ada di $font_size_allowed[0]
$besar_font = in_array($besar_font, $font_size_allowed)? $besar_font : $font_size_allowed[0];

echo "<div style='font-size:$besar_font'>$komentar</div>";
[/sourcecode]

Sekarang silahkan masuk ke <a href="http://apayach.com/files/cssinject/secure/form.html">halaman ini</a> dan tes apakah CSS injection masih berhasil atau enggak. Dengan begini, form HTML kita jadi lebih aman dari CSS Injection. Ada banyak cara lagi untuk mencegah CSS Injection. Kalau mau bermain aman, maka pertimbangkan lagi ketika ingin menggunakan form yang bisa di customize (warna, font, dll). Apakah memang perlu? Contohnya seperti situs berita, rasanya user tidak perlu diberi fasilitas untuk mengubah warna/size font. 

Untuk yang menggunakan CMS seperti Joomla, MD-Pro, VBulletin, Drupal, dsb. Sebaiknya rutin melakukan update CMS-nya, begitu juga bagi yang menggunakan plugin-plugin tambahan seperti shoutbox, guestbook, dsb. Better safe than sorry :roll:


<b><a name="blogkonten8">Kesimpulan</a></b>
CSS injection memang bisa mengubah style elemen bahkan jika dibuat sedemikian rupa, bisa mengubah keseluruhan halaman web. Tapi sebenarnya ini tidak terlalu berbahaya bagi sistem, karena sejauh ini tidak membahayakan database dan application layer. Hanya saja output yang dihasilkan bisa terlihat menyeramkan. Tapi admin bisa dengan mudah menghapus entry yang memiliki CSS injection di database, dan web pun kembali terlihat cantik.

Well, hacking bukan barang mainan, bukan untuk keren-kerenan biar keliatan pinter atau hebat. Kalau kita ngerusak web orang lain, then it's a crime, dan itu dilarang, sama sekali nggak keren dan buat saya malah keliatan seperti sok pinter dan sok pamer. Saya pribadi ngelarang dan nggak mau pembaca blog ini mempraktekan apa yang saya tulis untuk membantai situs yang dibencinya. Yang saya tulis disini sekedar sharing teknik pemrograman saja, buat yang suka eksperimen juga buat administrator web. Have fun with CSS injection :roll: , <i>*ngeloyor ke warung buat sahur...*</i>