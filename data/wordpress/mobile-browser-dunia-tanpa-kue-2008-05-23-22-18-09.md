title:Mobile Browser : Dunia Tanpa Kue
date:2008-05-23 22:18:09
status:draft

<img src="http://kecebongsoft.files.wordpress.com/2008/05/best_cookie-20-copy.jpg" alt="" width="400" height="379" />

Yayaya.. Sekarang dunia sudah canggih, dan aku pasti dibilang gila karena pernah berfikir seperti apa yang akan kutulis sebentar lagi, bodo ah disebut gila :mrgreen: . Tapi serius aku dulu pernah berfikir seperti ini dan mencari solusinya, meskipun belum pernah implementasi. Apa yang sedang kita bicarakan?.<!--more-->

Setahun lalu, aku sempat berurusan dengan <a href="http://en.wikipedia.org/wiki/Web_browser">browser</a> bawaan ponsel dengan segala macam keterbatasannya. <a href="http://en.wikipedia.org/wiki/JavaScript">Javascript</a> yang terbatas lah, nggak bisa buka file <a href="http://id.wikipedia.org/wiki/GIF">GIF</a> lah, macem-macem. Salah satu masalah yang cukup menyita pikiran adalah : kebanyakan browser bawaan ponsel tidak mendukung <a href="http://en.wikipedia.org/wiki/HTTP_cookie">Cookie</a> (kue?) sebagai gudang untuk penyimpanan <a href="http://en.wikipedia.org/wiki/Session_(computer_science)">Session</a>. Kenapa aku mengurusi hal ini?, setahun yang lalu aku membuat sebuah website yang target platformnya adalah ponsel, dan tidak semua orang pakai ponsel canggih sehingga ini memaksaku untuk melawan segala keterbatasan yang dimiliki oleh browser ponsel low end, yaitu dengan cara mengakali segala macam keterbatasan tersebut tanpa harus melibatkan user.

Koneksi internet pada ponsel biasanya di-charge dalam hitungan sekian rupiah per sekian kilobytes (misal : Rp.5/kB), dan biasanya situs yang memang ditargetkan untuk ponsel filesizenya kecil, tujuannya untuk menekan biaya koneksi.  Sekarang kembali ke masalah cookies tadi, <a href="http://en.wikipedia.org/wiki/PHP">PHP</a> (server side script yang kugunakan saat itu) mendukung 2 jenis manajemen session : Cookies dan URL Embedding. Dan kebanyakan browser bawaan ponsel tidak mendukung cookies, sehingga semua informasi yang disimpan didalam session (seperti informasi login) akan hilang. Alternatifnya adalah menggunakan opsi kedua, yaitu URL Embedding, tekniknya adalah dengan "menempelkan" atribut ID dari session yang sedang digunakan kedalam setiap URL yang ada di halaman web kita, biasanya atribut ini diberi nama "SID" atau "PHPSESSID". Dengan menggunakan opsi ini, maka setiap URL yang ada di web kita akan memiliki atribut PHPSESSID, contoh :

<strong>"http://www.anu.com/index.php?page=news&amp;newsid=5&amp;PHPSESSID=X123098asd12871312987DASD"</strong>

Dari mana kode ajaib didalam PHPSESSID tersebut?. Kode tersebut adalah ID dari session yang sedang digunakan, yang dienkripsi mengunakan fungsi <a href="http://en.wikipedia.org/wiki/MD5">MD5</a> (enkripsi searah). Dengan kode ini, PHP akan mengetahui session mana yang sedang digunakan dan kita tetap bisa mengakses semua session didalamnya. Oke, masalah selesai, session sekarang kembali bisa digunakan untuk browser ponsel. Tapi masalah baru kemudian muncul, coba hitung berapa jumlah karakter kode dan nama atribut PHPSESSID, setidaknya kurang lebih 35 karakter (35 bytes), dan itu hanya untuk 1 buah URL!. Bayangkan jika dalam satu page kita memiliki 5 hingga 15 url : 15 x 35 = 525 bytes, atau kira2 setengah kilobytes. Sekarang anggap tarif koneksi GPRS adalah Rp. 5/kB, maka dalam satu page, web kita telah melahap Rp. 2,5 hanya untuk urusan session yang bahkan user pun tidak tahu apa itu session dan kenapa harus ada session. Dan lagi user tidak mungkin hanya membuka 1-2 page, mereka akan mengunjungi banyak page dan menghabiskan banyak sekali Rp. 2,5 yang sifatnya (sepertinya) sia-sia alias mubazir.

Dari sinilah ide aneh itu muncul, cookies sudah tidak mungkin dipergunakan, jadi sekarang targetnya adalah bagaimana "mencekik" teknik URL Embedding ini agar menghasilkan bytes yang kecil namun tetap bisa dipergunakan untuk menghandle session. <!--more-->Aku nggak akan membahas how-to-code-nya, tapi disini akan dipaparkan bagaimana merubah URL buruk rupa tadi :
<strong></strong>

<strong>"http://www.anu.com/index.php?page=news&amp;newsid=5&amp;PHPSESSID=X123098asd12871312987DASD"</strong>

Menjadi :

<strong>"http://www.anu.com/index.php?page=news&amp;newsid=5&amp;Z=15"</strong>

Apa itu Z=15? Itu adalah 35 bytes yang tadi dan sekarang "dicekik" menjadi 4 bytes. Disini kita akan bermain lempar-lemparan SessionID untuk mendapatkan hasil seperti diatas.

Konsep dasarnya adalah, pada saat halaman pertama kali dibuka, kita men-generate sebuah SessionID, kemudian menyimpannya kedalam database, setelah itu membuat sebuah rutin yang akan <strong>selalu</strong> mengeset SessionID selanjutnya sesuai dengan yang telah tersimpan didatabase. Simpel kan?. Dan ternyata untuk melakukannya kita sudah tidak membutuhkan lagi cookies dan URL embedding, variabel Z=15 adalah ID dari recordset session yang ada didalam database.

Oke, pertama-tama adalah sesi first time user membuka website. Pada saat itu, kita nyalakan session dengan fungsi <a href="http://my.php.net/manual/en/function.session-start.php">session_start()</a>. Pada saat session ini dijalankan, maka PHP akan men-generate sebuah SessionID baru, SessionID inilah yang akan kita simpan untuk dipergunakan selanjutnya, caranya adalah dengan menyimpannya kedalam database dan mengambil IDnya untuk digunakan sebagai referensi. Ini adalah kode "kotor"nya :

[sourcecode language='php']
session_start(); // Start session
$saved_session = session_id(); // Get SessionID
mysql_query("INSERT INTO tbl_session (sessid) VALUES ('$saved_session')");
$sess_id = mysql_result(mysql_query("SELECT id FROM tbl_session ORDER BY id DESC LIMIT 0,1"),0);
[/sourcecode]

Yup, kita telah mendapatkan SessionID dan menyimpannya kedalam database. ID dari SessionID telah tersimpan di variabel $sess_id. Setelah mendapatkan SessionID ini, maka kita tinggal membuat sebuah rutin yang akan selalu terpanggil setiap kali halaman web dibuka, rutin ini akan meng-assign SessionID ke session yang telah kita buat sebelumnya, berikut kodenya :

[sourcecode language='php']
session_id($sess_id); // set session id to $sess_id
[/sourcecode]

Sekarang semua link yang kita buat tinggal ditempelkan atribut yang isinya adalah nilai dari variabel $sess_id tadi. Untuk menghemat bytes, kita buat saja variabel "z" pada URL yang berguna untuk menyimpan nilai dari variabel $sess_id, contoh :

[sourcecode language='php']
echo "<a href='$PHP_SELF?page=news&z=$sess_id'>Home</a>";
[/sourcecode]

Dan kita juga harus memastikan apakah user membuka halaman ini untuk pertama kali atau bukan, caranya dengan mengecek apakah variabel "z" ada pada URL atau tidak, jika ada maka kita assign SessionID ke variabel "z", jika tidak maka kita generate SessionID baru kedalam database. Contoh :

[sourcecode language='php']
session_start(); // Start session
if(empty($_GET['z'])){
    $saved_session = session_id(); // Get SessionID
    mysql_query("INSERT INTO tbl_session (sessid) VALUES ('$saved_session')");
    $sess_id = mysql_result(mysql_query("SELECT id FROM tbl_session ORDER BY id DESC LIMIT 0,1"));
}else{
    $sess_id = $_GET['z']; // Get SessionID
}
session_id($sess_id);
[/sourcecode]

Simpel kan?. Dengan seupil kode ini kita bisa melangsingkan filesize web page. Tapi ada banyak hal yang harus diperhatikan, pertama adalah setiap recordset yang menyimpan sessionid harus diberi informasi mengenai siapa pengaksesnya, kapan mulai mengakses, dll, ini untuk menghindari serangan-serangan yang dapat dengan mudah dilakukan hanya dengan menuliskan sembarang ID didalam atribut "z" pada URL. Kita juga harus memberi "umur" untuk setiap recordset, dalam artian jika session tersebut tidak dipergunakan dalam jangka waktu tertentu (setengah jam misalnya) maka akan otomatis tidak dapat digunakan, dan siapapun yang mencoba menggunakan SessionID tersebut akan dialihkan ke SessionID yang baru.

Database untuk menyimpan session ini juga lama-kelamaan akan menjadi besar dan ID yang tersimpan akan semakin banyak jumlah bytesnya, untuk menghindari hal ini, maka cukup buat rutin yang secara otomatis menghapus setiap ID yang tidak dipergunakan agar entry tersebut bisa digunakan untuk SessionID yang baru. Atau bisa juga dengan cara mengupdate recordset SessionID yang sifatnya tidak aktif menjadi aktif, kemudian mengupdate nilai SessionIDnya ke yang terbaru.

Itulah secuil ide aneh yang tidak sempat aku coba dulu, tapi secara logika masih mungkin untuk diimplementasikan. Kekurangannya mungkin dari sisi sekuriti belum teruji, mungkin masih bisa di"akalin" orang iseng dengan memanfaatkan proxy site atau yang lainnya. Ide ini juga sempat aku posting di beberapa forum PHP programming luar dan lokal. Hasilnya? dari sekian forum hanya 1 yang menjawab, sisanya diam tak memberi jawaban apapun :-( . Mungkin memang benar ini ide aneh.. hehehe..

Tapi seiring perkembangan mobile device, browser yang dimiliki oleh perangkat-perangkat tersebut pasti akan berkembang dan menyaingi browser desktop dalam hal kapabilitas maupun fitur. Dan ide diatas sudah siap untuk dikubur :mrgreen:

[digg=http://digg.com/programming/Mobile_Browser_Dunia_Tanpa_Kue]