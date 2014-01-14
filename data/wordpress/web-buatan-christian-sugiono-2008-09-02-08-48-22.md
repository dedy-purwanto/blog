title:Web buatan Christian Sugiono?
date:2008-09-02 08:48:22
status:draft

Oke, sebelum mulai ngobrol, saya mau tekankan dulu kalau disini saya nggak ada niat buat mojokin siapapun. Yang saya mau tulis ini nggak lebih dari sekedar analisa seorang bocah 19 tahun belaka. Lagian lagi puasa gini ngga banget deh klo saya ngomong yang enggak-enggak :roll: 

Tanggal 9 Juni lalu, <a href="http://techno.okezone.com/index.php/ReadStory/2008/06/09/94/117128/christian-sugiono-dulu-gue-kerja-jadi-programmer">muncul berita</a> tentang <a href="http://id.wikipedia.org/wiki/Christian_Sugiono">Christian Sugiono</a>, itu tuh.. seleb yang dulu pernah kuliah IT di Jerman. Saya juga pernah nonton dia dan Roy Suryo satu frame bareng di acara Empat Mata (kebetulan saya penggemar Empat Mata :-p ). Well, beritanya sih nggak terlalu heboh (skandal, dll).. cuma nampilin sisi lain hidupnya dia aja. Bahwa dia diangkat jadi icon IT sekaligus brand ambassador HP Indonesia. Dia juga cerita bahwa dulu pas di Jerman dia pernah work as a programmer, bikin tim bareng temennya. Trus, saya sempat liat statementnya dia diberita tersebut, kurang lebih gini (langsung kopi paste) :<!--more-->
<blockquote><em>Menutup jumpa pers, Christian sempat memaparkan alamat website yang dibikin langsung olehnya sendiri. "Dulu gue sempat bikin website sendiri, masih aktif, di <a href="http://www.christian-sugiono.com/" target="_blank">www.christian-sugiono.com</a>," paparnya.</em></blockquote>
Bikin web sendiri? Nggak bisa dibilang luar biasa untuk ukuran mahasiswa IT, apalagi dia jebolan Jerman (nggak tau juga universitas mana tapi kayaknya sih keren wkwkwkwk). Saya penasaran aja gimana sih webnya. Jadi dibuka deh tuh www.christian-sugiono.com-nya, eh malah ke-redirect ke http://christian-sugiono.seleb.tv, well.. gpp juga sih sama aja.

Tapi wow :shock: , ini webnya keren juga. Udah kayak CMS terkenal macam Wordpress/Blogspot aja.. Ada category, post comment, macem-macem deh. Belum lagi URLnya pake <a href="http://en.wikipedia.org/wiki/Permalink">Permalink</a> pakai gaya Wordpress (<em>domain.com/tahun/bulan/hari/namaartikel</em>). Udah lumayan advanced tuh bisa bikin permalink gitu (pake mod rewrite, setting .htaccess dan bla bla bla). Jangan-jangan bikin engine sendiri? wuih keren juga.. atau pake framework kayak Zend Framework, CakePHP, dll?.. Nggak kalah keren, ngikutin perkembangan jaman dong namanya.

Saya nggak ngeragukan kemampuannya, tapi tetep aja penasaran masa iya dia yang bikin. Trus nggak sengaja saya baca <a href="http://christian-sugiono.seleb.tv/2008/08/21/bagi-yang-kurang-paham/">salah satu postingan dia</a> yang isinya :
<div class="post-content">
<blockquote>Setelah keluar di infotainment, ada beberapa orang yang tanya dan protes ke gue misalnya seperti ini :

<em>Statement Tian di infotainment tgl 21 agustus, mengatakan bahwa web ini http://christian-sugiono.seleb.tv/ yang buat Tian sendiri?Saya yakin tidak mungkin, karena:1. http://christian-sugiono.seleb.tv/ redirected to subdirectory dari http://www.seleb.tv/2. Dan website seleb.tv yang memiliki adalah sbg.:Registrant:
Sandika Digital Media PT
Jl. Panglima Polim Raya
101 Kebayoran Baru
Jakarta, Jakarta 12160</em>

Sampe di cari whoisnya segala loh uhuhuhe <img class="wp-smiley" src="http://christian-sugiono.seleb.tv/wp-includes/images/smilies/icon_razz.gif" alt="P" />

Yah, mungkin buat orang-orang diluar sana yang masih belum paham, <strong>website development dan designing</strong> dan hosting adalah 2 hal yang berbeda. <strong>Ini blog saya buat 100% sendiri</strong> dan di taruh di server milik seleb.tv sogak usah gw lanjutin lagi kan ?

Cheers.</blockquote>
</div>
Sip, bener. Development emang beda sama hosting... habis dari situ saya percaya deh dia yang bikin, dan ngga mau ngelanjutin penasarannya. Eh tapi kok masih kepikiran ya?. Ya udah lah.. saya cobain dulu buka source HTMLnya (klik kanan pilih view page source), wuih keren juga.. detail dan.. eh? ketemu ini :

[sourcecode lang='html']
<meta name="generator" content="WordPress 2.5.1" />
[/sourcecode]

Wordpress? Loh tapi tadi katanya bikin sendiri, lagian apa iya dia nggak bisa ngebedain antara nginstall CMS dan bikin sendiri. Hmm.. saya salah lihat kali. Tapi... ah percobaan terakhir deh.., ngebuktiin apa beneran wordpress atau bukan. Tes buka link ini : <a href="http://christian-sugiono.seleb.tv/wp-login.php">christian-sugiono.seleb.tv/wp-login.php</a> , eh ternyata ada!. Kalau yang pernah pakai wordpress, wp-admin adalah halaman administrasi CMS Wordpress, dan wp-login adalah halaman login untuk masuk ke wp-admin (wp singkatan dari Wordpress, cmiiw).

Kalau memang Christian Sugiono yang bikin web ini, berarti dengan kata lain dia pembuat tunggal <a href="http://wordpress.org/">Wordpress</a>? (Spt dia bilang tadi, 100% bikin sendiri). Ah mustahil, Wordpress kan open source project, bikinan kepala-kepala jenius dari macem-macem negara.

Jadi apa dong arti "<strong>Ini blog saya buat 100% sendiri</strong>" tadi?. Iseng-iseng lagi saya intip source HTMLnya, ketemu ini :

[sourcecode lang='html']
<link href="http://christian-sugiono.seleb.tv/wp-content/themes/christiansugiono/css/main-style.css" rel="stylesheet" type="text/css" />
[/sourcecode]

Hoo.. mungkin itu kali maksudnya. Dia yang 100% bikin themesnya. Well, bikin themes juga bukan kerjaan gampang, plus, theme blog dia lumayan keren :-D .

Jadi?. Saya nggak bisa bilang klo blog itu dia yang bikin sendiri, karena udah jelas keliatan itu mesin Wordpress, yang statusnya adalah open source project, dikerjakan oleh para programmer di berbagai belahan dunia.

Apa dia bo'ong?. Nggak tau deh, tapi yang bisa kita ambil hikmahnya disini, dunia teknologi itu nggak segede daun kelor, banyak banget yang kita nggak tahu dan riskan banget bikin statement yang kita sendiri nggak terlalu paham apa maksudnya. Bagi yang ngerasa heran "kenapa sih itu programmer-programmer pinter nggak mau bikin artikel?", klo saya boleh ngewakilin jawab (meskipun saya bukan programmer dan nggak pinter) "Mungkin karena mereka blum merasa yakin, bahkan setelah belajar bertahun-tahun, mereka nggak mau bikin statement sembarangan.".

Atau jangan-jangan web yang dibikin Christian Sugiono bukan web yang sekarang kali, tapi web yang dulu (sekarang udah nggak aktif &amp; diganti dengan WP). Well, saya nggak tahu. Tapi sepertinya nggak, soalnya postingan tadi dia bikin tanggal 21 Agustus (baru-baru aja), dan ada di blog WP-nya dia.

Sebenernya yang ginian udah umum, dan sebenernya nggak boleh. Mengklaim teknologi (Lisensi GPL) orang/kelompok lain atas nama kita pribadi. Coba deh liat kadang-kadang ada web yang jelas-jelas pakai CMS (Joomla, WP, dll), tapi copyright di footernya atas nama pribadi/instansi. Memang siapa yang bikin Joomla? WP?. 

Jadi yang bisa diambil hikmahnya : "Jangan ambil statement yang kita sendiri nggak paham", dan "Jangan melanggar hukum", Loh?. Yah bingung juga nyebutnya apa, pokoknya jangan main klaim-klaim sembarang gitu-gitu deh.

Saya sendiri bukan siapa-siapa, bikin web aja masih belepotan. Dan yang jelas sebelum ini saya nggak pernah protes/tanya ke dia tentang siapa pembuat web tersebut. Btw saya ngga iri lho yah, kali2 aja ada yang ngira saya iri ma Christian Sugiono gara2 dia cakep+seleb+pinter :lol: . Mending direnungkan lagi deh dengan kepala dingin. Yang dibuka disini adalah hal teknikal, bukan ledek-ledekan/menjatuhkan salah satu pihak :roll: 

Oh iya sapa tau masih ada yang blur, klo bikin web menurut versi saya : bikin desain sendiri (coret2 di photoshop/gimp/dll) trus bikin HTMLnya, trus desain + generate databasenya (klo memang pake database), trus bikin script server side/client sidenya dari nol (klo memang pakai server/client side script)... dsb..dsb.. Beda dengan nginstall CMS : sediain hosting + dbaccount, download CMS, ubah file config (klo di WP namanya wp-config.php), upload, install, jadi deh (biasanya nggak sampe 10 menitan). Cmiiw.

Lastly, kalau memang analisa saya salah, silahkan klarifikasi, via email atau langsung isi di box komen. Saya nggak bilang Christian Sugiono bo'ong loh ya (mungkin cuma kurang paham ato gimana), cuma web yang tadi emang keliatan beneran Wordpress, kecuali klo saya salah, abisnya ngantuk berat, lembur dari tadi jam sembilan malam ampe sekarang jam sembilan pagi hehehe.. :lol:


btw met puasa ya buat yang menjalankan. Maafin saya yang setiap hari adaaa aja bikin salah..


-<b>Updated</b>-
Akhirnya kasus ini dah case closed. Christian Sugiono udah datang langsung ke blog gw (lihat di kolom komentar) dan menjelaskan semuanya. Singkatnya, memang dialah yang membuat web di <a href="http://www.christian-sugiono.com">christian-sugiono.com</a>, tapi bukan yang sekarang, melainkan web yang dulu. Sekarang sudah diganti dengan WP karena pertimbangan kemudahan bagi admin untuk manajemen post, comments, dsb. Yang bersangkutan juga udah kasih beberapa sampel web yang dia buat seperti gallery di blognya saat ini, juga <a href="http://www.malesbanget.com">malesbanget.com</a> yang pernah dibuatnya dulu.

Lega deh gw nggak nebak-nebak lagi, gw juga udah ngga sangsi lagi dengan statement yang pernah dia kasih ke berita, dan gw juga salut bahwa profesi programmer yang super sibuk dengan research, bisa digabungkan dengan profesi aktor. Well.. I welcome you here Christian Sugiono, met bergabung di blogsphere wordpress dan gw senang klo lo mau ikut berbagi info IT disini :roll: