title:Mereset root password (Linux)
date:2007-07-12 05:25:02
status:draft


<p class="main">Kmaren juga sempat pengalaman kelupaan password, buat yang punya LILO, coba deh pas booting pake parameter :</p>

<pre>linux init=/bin/sh</pre>
Parameter itu bakal ngeset bahwa booting akan menggunakan shell, kemudian setelah shellnya keluar, coba perintah ini:
<pre>vi /etc/passwd</pre>
Jika kolom kedua pada baris <strong>root</strong> (kolom dibatasi dengan karakter :) hanya berisikan karakter x, maka password yang kita gunakan bertipe shadow password, tutup vi, dan buka lagi dengan perintah ini:
<pre>vi /etc/shadow</pre>
Hapus kolom kedua pada baris <strong>root</strong>, kemudian save file tersebut. Coba deh di restart, and voila :-D.

Tapi terkadang ada juga kendala, beberapa distro seperti mandrake, dll, secara default mengeset owner file-file tersebut adalah root. Kalau sudah begitu, mungkin shell saja tidak cukup untuk mereset password (pada perintah VI akan muncul pesan yang berbunyi Read Only File). Kalau itu terjadi, coba pakai LiveCD Distro, untuk LiveCD, Ubuntu cukup bisa diandalkan, karena distro ini cukup banyak memiliki perbendaharaan device storage (IDE, SCSI), jadi buat yang pake hardisk SCSI gak perlu khawatir hardisknya gak ke-detect di ubuntu :-D.

Caranya sama dengan cara shell, hanya saja sekarang berbasis GUI, untuk ubuntu, disarankan booting dengan metode <em>live-expert</em>. Kemudian set password rootnya dan biarkan normal user untuk login, setelah itu kita bisa masuk melalui terminal (pada GNOME), dan ketikan perintah SU untuk login sebagai super user. Selebihnya sama seperti saat berhadapan dengan shell :-D.