title:Flash di Opera (Ubuntu Gutsy)
date:2008-02-04 04:03:30

![image](/img/wordpress/2008-02-opera_icon_02.jpg)
Salah satu masalah kemarin setelah nginstal Gutsy Tribe (Ubuntu 7.10) adalah opera yang nggak bisa memainkan file swf (shockwave flash), parah banget soalnya aku suka nonton
<strike>
 hentai dan miyabi
</strike>
4 mata di youtube. Tapi tunggu dulu, kenapa aku pakai Opera? secara udah bertahun-tahun pakai firefox. Alasannya nggak lain karena aku pake KDE dan font interface firefox gedenya
<strike>
 seanjrit-anjrit
</strike>
segaban-gaban klo di KDE, udah dicoba ubek-ubek konfigurasi tapi tetep aja :-( .

Well, kalau nginstal opera di gutsy dengan perintah apt-get install opera, untuk yang sekarang kita akan dikasih versi 9.25 (versi terbaru yang stabil), kemudian kalau mo pasang flash player, harus nginstall manual. ada beberapa cara :
<!--more-->
<strong>
 Cara 1 :
</strong>
- Pertama download dulu flash playernya di
<a href="http://www.adobe.com/shockwave/download/download.cgi?P1_Prod_Version=ShockwaveFlash">
 website Adobe
</a>
, pilih yang paket tar.gz
- Ekstrak ke direktori (desktop contohnya)
- Kopi file libflashplayer.so yang ada di folder ekstrak ke folder /usr/lib/opera/plugins
- Restart opera, tes dengan membuka
<a href="http://www.adobe.com/shockwave/welcome/">
 halaman ini
</a>
<strong>
 Cara 2 :
</strong>
- Melalui konsol, masuk ke direktori hasi ekstrak flash player tadi
- Login sebagai root, masukan perintah ./flashplayer-installer
- Pas ditanya install destination, masukan /usr/lib/opera
- Restart opera, tes dengan membuka
<a href="http://www.adobe.com/shockwave/welcome/">
 halaman ini
</a>
Nggak bisa juga?, coba pake hard way, ikutin
<a href="http://ubuntuforums.org/showthread.php?t=413040">
 tutorial dari forum ubuntu
</a>
. Dan coba restart opera lalu test apakah flashnya berjalan atau enggak.

Masih nggak bisa juga? pastiin dulu option plugin di opera nyala, tekan F12 ato pilih menu Tools -&gt; Quick Preferences -&gt; Enable Plugin.

Kalau masih nggak bisa, pakai cara terakhir, install opera 9.5 (yang&#160; sekarang masih beta) nggak ada resikonya sih karena sejauh ini aku juga makai nggak ada masalah :p , its run very stable and fast.
<a href="http://www.opera.com/download/?ver=9.50b">
 Download Opera 9.5 Beta disini
</a>
. Untunglah paketnya debian jadi installnya nggak ribet. And let's say hello to Opera!.
