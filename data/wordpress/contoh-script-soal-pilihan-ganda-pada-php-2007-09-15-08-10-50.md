title:Contoh script soal pilihan ganda pada PHP
date:2007-09-15 08:10:50

Kemarin, seorang teman menanyakan tentang hal ini. Dakuw juga sering berfikir kenapa tidak ada tutorial yang seperti ini, rata-rata tutorial tersebut lebih mengarah ke teknik-teknik pemrograman, bukan alur logika yang mengarah pada kasus-kasus spesifik seperti ini (CMIIW). Mungkin beberapa berpendapat, bahwa mereka harus membangun logika sendiri. Bagaimana kalau logikanya Pentium tidur seperti dakuw :-D (becanda deng).
<!--more-->
Just an opinion. Oke deh, disini kita akan mencoba membuat web sederhana yang menampilkan sejumlah soal dari sekian soal secara acak, dan setiap soal disertai dengan 4 pilihan (pilihan ganda). Setelah soal-soal tersebut dijawab oleh user, maka akan ditampilkan halaman yang mengecek jawaban tersebut benar/salah. Mudah kan?

Pertama, kita desain dulu databasenya, buka phpmyadmin atau MySQL Front atau apapun yang biasa dipakai untuk manajemen database MySQL. Tabel pertama adalah table soal, yang akan menyimpan soal-soal.
	:::txt
CREATE TABLE `soal` (
`id` int(99) NOT NULL AUTO_INCREMENT,
`soal` text NOT NULL,
PRIMARY KEY  (`id`)
);

ID adalah primary key dari tiap record, sedangkan field &#8220;soal&#8221; akan menyimpan text-text soal. Tabel &#8220;soal&#8221; sudah jadi, sekarang kita buat tabel jawaban.
	:::txt
CREATE TABLE `jawaban` (
`id` int(99) NOT NULL AUTO_INCREMENT,
`soal` int(99) NOT NULL,
`jawaban` text NOT NULL,
`benar` tinyint(1) NOT NULL,
PRIMARY KEY  (`id`)
);

Field &#8220;id&#8221;, adalah primary key dari tiap record. Field &#8220;soal&#8221; adalah foreign key yang menunjuk pada tabel soal. Misalkan pada sebuah record di tabel jawaban, terdapat nilai &#8220;3&#8221; pada field &#8220;soal&#8221;, maka itu berarti jawaban tersebut milik soal yang ber-id &#8220;3&#8221; pada tabel soal. Field &#8220;jawaban&#8221; adalah field yang menyimpan teks jawaban. Field &#8220;benar&#8221; adalah field yang menentukan jawaban tersebut benar atau tidak (karena peraturannya adalah pilihan berganda), mungkin saja ada banyak jawaban untuk satu soal, tapi hanya satu yang benar. Kita akan set 0 untuk tiap jawaban yang salah, dan 1 untuk jawaban yang benar.
Oke, tabel udah jadi, sekarang kita masuk ke script, perlu diingat struktur file disini dibuat sesederhana mungkin, tapi jangan diikuti untuk website sebenarnya yak :-D .

Ini script untuk menampilkan soal dan jawabannya, jangan khawatir tiap baris sudah diberi komentar penjelas kok :D. Klo di jelasin disini lagi justru berbelit-belit :-D, simpan dengan nama soal_view.php :
	:::txt
&lt;?
$db=mysql_connect("localhost","root","");
if($db)
{
if(mysql_select_db("tutorial_1"))
{
// Database selected
}
else
{
echo "Can&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;t select database!";
exit;
}
}
else
{
echo "Can&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;t Connect to MySQL Server!";
exit;
}
?&gt;
&lt;form method="post" action="soal_process.php"&gt;
&lt;?
// Inisialisasi variabel
$soal=array(); // Array yang digunakan untuk menyimpan "id" soal
$soal_max=3; // Jumlah soal yang akan ditampilkan
$nomor=1; // nomor urutan soal
// Kumpulkan nilai-nilai "id" yang ada pada tabel "soal", simpan ke array "soal"
$query=mysql_query("SELECT * FROM soal");
while($row=mysql_fetch_array($query))
{
$soal[]=$row[id];
}
// Yup, array "soal" sudah terisi, tinggal diacak dan di buang hingga isinya tinggal $soal_max
// fungsi array_rand, tidak mengacak isi dari array, melainkan hanya nomor urut dari array
// karena itu kita gunakan variabel $soal_urut, untuk menyimpan urutan soal yang sudah diacak
// MIS : sebelum diacak :
// isi array (0=&gt;"1",1=&gt;"2",2=&gt;"3",3=&gt;"4",4=&gt;"5") angka di sebelah kiri adalah nomor urut array
// dan yang disebelah kanan adalah isi dari array tersebut
// fungsi array_rand, hanya mengacak urutannya, bukan nilainya.
$soal_urut=array_rand($soal,$soal_max);
while($s=each($soal_urut))
{
// ambil nomor soal
$soal_nomor=$s["value"]; // ambil nomor urut array
$soal_nomor=$soal[$soal_nomor]; // ambil array dengan nomor urut $soal_nomor
// tampilkan soal
$query=mysql_query("SELECT * FROM soal WHERE id=".$soal_nomor);
$row=mysql_fetch_array($query);
echo "&lt;b&gt;$nomor. ".$row[soal]." ?&lt;/b&gt;";

// tampilkan pilihan ganda, dalam bentuk radio button
// value pada radio button kita set sesuai "id" dari jawaban tersebut
// jadi, nanti pada saat di proses, cukup kita cek apakah jawaban dengan "id"
// tersebut nilai "benar"nya 0 atau 1.
$query=mysql_query("SELECT * FROM jawaban WHERE soal=".$soal_nomor);
while($row=mysql_fetch_array($query))
{
$id=$row[id];
$jawab=$row[jawaban];
$benar=$row[benar];

// kita beri nama radio buttonnya jawab_$soal_nomor, kalau "id" soal yang sekarang
// adalah 10, maka radio buttonnya jadi jawab_10, dst.
echo "&lt;input type=\\"radio\\" name=\\"jawab_$soal_nomor\\" value=\\"$id\\"&gt;$jawab";
}
// Oh iya, disini juga kita buat string yang isinya array soal yang sudah diacak tadi
// tujuannya, untuk kita masukan ke hidden field, dan ikut di transfer bersama
// form, kemudian nanti di pecah lagi menjadi array pada soal_process.php
// string ini berguna untuk menyimpan urutan soal mana saja yang ditampilkan sekarang
$soal_nomor_send.=$soal_nomor . ",";

// Ini nomor urut soal, untuk tampilan saja
$nomor++;
}
// Karena string dari array soal yang kita kumpulkan tadi sudah selesai, namun
// karakter terakhirnya masih ada "koma" (mis : "5,3,2,1,"), jadi kita ilangin komanya dulu
$soal_nomor_send=substr($soal_nomor_send,0,strlen($soal_nomor_send)-1);

// yup, sekarang string dari array soal sudah jadi, tinggal di masukan ke hidden field
echo "&lt;input type=\\"hidden\\" name=\\"soal_nomor\\" value=\\"$soal_nomor_send\\"&gt;";
?&gt;
&lt;input type="submit" value="Jawab"&gt;
&lt;/form&gt;

Dan ini, adalah file untuk memproses jawaban, simpan dengan nama file soal_process.php :
	:::txt
&lt;?
$db=mysql_connect("localhost","root","");
if($db)
{
if(mysql_select_db("tutorial_1"))
{
// Database selected
}
else
{
echo "Can&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;t select database!";
exit;
}
}
else
{
echo "Can&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;t Connect to MySQL Server!";
exit;
}
?&gt;

&amp;lt;?
// Inisialisasi variabel
$user_jawab=array(); // Array yang digunakan untuk menyimpan jawaban user dari form tadi
$soal_urut=array(); // Array yang digunakan untuk menyimpan urutan soal dari form tadi (hidden field)
$nomor=1; // nomor urutan soal

$soal_urut=$_POST["soal_nomor"]; // Ambil hidden field dari form tadi
$soal_urut=explode(",",$soal_urut); // pecah menjadi array, pecah berdasarkan tanda ","

// Tampilkan soal-soal yang tadi
while($s=each($soal_urut))
{
$soal_nomor=$s["value"]; // ambil "id" soal

// tampilkan soal
$query=mysql_query("SELECT * FROM soal WHERE id=".$soal_nomor);
$row=mysql_fetch_array($query);
echo "&lt;b&gt;$nomor. ".$row[soal]." ?&lt;/b&gt;";

// tampilkan pilihan ganda
$query=mysql_query("SELECT * FROM jawaban WHERE soal=".$soal_nomor);
while($row=mysql_fetch_array($query))
{

$id=$row[id];
$jawab=$row[jawaban];
$benar=$row[benar];

// kita ambil "id" jawaban yang di submit user dari form tadi
$user_jawab=$_POST["jawab_$soal_nomor"];

// apakah "id" jawaban yang sedang ada di query ini sama dengan "id"/value pada radio button yang disubmit user?
if($user_jawab==$id){
if($benar==0){ // apakah salah jawaban si user?
$jawab_status="&lt;span style=&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;color:red;&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;&gt;&amp;lt;&amp;lt; Jawaban Anda&#195;&#162;&#239;&#191;&#189;&#194;&#166; Salah!&lt;/span&gt;";
}else{ // atau benar?
$jawab_status="&lt;span style=&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;color:blue;&#195;&#162;&#239;&#191;&#189;&#239;&#191;&#189;&gt;&amp;lt;&amp;lt; Jawaban Anda&#195;&#162;&#239;&#191;&#189;&#194;&#166; Benar!&lt;/span&gt;";
}
}
else // kalau "id"nya tidak sama
{
$jawab_status="";
}

// tampilkan radio buttonnya
echo "&lt;input type=\\"radio\\" name=\\"jawab_$soal_nomor\\" value=\\"$id\\"&gt;$jawab $jawab_status";
}
$nomor++; // nomor urut soal, hanya tampilan saja
}
?&gt;

Oke deh, selamat mencoba, don&#8217;t hestitate to reply klo ketemu bug :D
