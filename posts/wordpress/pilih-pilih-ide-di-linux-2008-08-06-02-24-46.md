title:Pilih-pilih IDE di Linux
date:2008-08-06 02:24:46

Biasanya, saya menggunakan
<a href="http://www.adobe.com/products/dreamweaver/">
 Dreamweaver
</a>
di Windows untuk mengerjakan kode-kode client/server side. Ada beberapa hal vital bagi saya pribadi yang ada di Dreamweaver, yaitu
<em>
 code completion, site/project manager, intellisense
</em>
, dll yang rasanya susah ditemukan di software IDE (Integrated Development Environment) lainnya. Tapi beberapa hari yang lalu Windows yang saya gunakan terserang virus yang memakan hampir 80% resource prosesor dan RAM yang berakhir dengan melambatnya kinerja Windows.

Ini memaksa (bukan terpaksa, sih) saya untuk pindah ke Ubuntu Gutsy (Linux) tersayang (saya punya 2 OS) untuk mengerjakan kode-kode tersebut. IDE yang saya miliki cukup banyak, tapi hampir tidak ada yang memenuhi kebutuhan.

Yang pertama adalah
<a href="http://www.gnome.org/projects/gedit/">
 Gedit
</a>
. Eits tunggu dulu, Gedit yang saya punya bukan lagi Gedit polos bawaan Ubuntu. Gedit yang saya miliki sudah termodifikasi disana-sini dengan themes dan komponen-komponen tambahan, diantaranya adalah:
<em>
 file browser, symbol browser, class browser, color picker, custom theme
</em>
, dll. Tapi ada beberapa kekurangan seperti tidak adanya
<em>
 intellisense
</em>
dsb. Dengan sangat terpaksa saya singkirkan Gedit dan mencari IDE lain.

[image](/img/wordpress/2008-08-gedit.jpg?w=300)

Pilihan kedua adalah mengemulasikan Dreamweaver di platform Linux, biasanya ini bisa menggunakan emulator seperti
<a href="http://www.winehq.org/">
 Wine
</a>
atau
<a href="http://www.codeweavers.com/">
 CrossOver
</a>
, sayangnya kedua emulator tersebut tidak pernah berhasil menjalankan Dreamweaver di Ubuntu saya. Terpaksa emulator juga harus disingkirkan dan mencari IDE lain.
<!--more-->
Pilihan ketiga adalah
<a href="http://bluefish.openoffice.nl/">
 BlueFish
</a>
editor. Ini IDE yang cukup komplit, tapi perlu kerja ekstra untuk mendapatkan fitur-fitur yang diincar seperti
<em>
 code completion, intellisense, auto tooltip
</em>
, dll. Parahnya, secara default BlueFish tidak mendeteksi jenis dokumen untuk kemudian ditampilkan dalam format syntax highlighting yang sesuai. Dan banyak lagi nilai minus yang saya temukan di BlueFish, terpaksa IDE ini juga disingkirkan.

Pilihan selanjutnya adalah
<a href="http://anjuta.sourceforge.net/">
 Anjuta
</a>
IDE. Software ini memang cukup komplit, tapi tetap perlu kerja ekstra keras untuk menambahkan komponen dan fitur yang diinginkan. IDE ini juga terpaksa tidak masuk nominasi.

IDE selanjutnya adalah
<a href="http://quanta.kdewebdev.org/">
 QuantaPlus
</a>
. IDE ini sudah cukup lengkap dengan dengan berbagai fitur didalamnya, bahkan bisa dibilang menyaingi Dreamweaver dalam beberapa hal. Tapi sayangnya aplikasi ini menggunakan KDE sebagai environmentnya, sementara saya sendiri adalah pemakai setia GNOME, meskipun QuantaPlus tetap bisa berjalan diatas GNOME, tapi theme dan styles-nya masih inherit dari KDE. Saya terpaksa mencari IDE yang lain.

Yang terakhir dan baru dapat, adalah
<a href="http://www.activestate.com/Products/komodo_edit/">
 Komodo Edit
</a>
. IDE ini cukup komplit memenuhi kebutuhan saya seperti project manager, code completion, syntax highlighting yang sangat lengkap, intellisense, code folding, auto tooltip, dan banyak lagi. Software ini juga cukup ringan dan menggunakan GNOME sebagai environmentnya. Adapun nilai minus yang saya temukan sejauh ini adalah:
1. Tidak ada color picker. Bagi saya color picker adalah utility vital ketika kita sedang mengedit file stylesheet seperti CSS.
2. Tidak ada "designer mode", sehingga kita tidak bisa melihat live-preview dari sebuah file HTML layaknya pada Dreamweaver. (Ini bukan nilai minus karena saya bukan desainer :p)

[image](/img/wordpress/2008-08-komodoedit.jpg?w=300)

Sejauh ini, Komodo Edit-lah yang jadi pilihan saya untuk mengerjakan kode-kode client/server side seperti .js, .php, dll. Software yang free, light, komplit dan sampai sekarang masih terus dikembangkan. Salah satu nilai plus juga adalah software ini yang paling "mirip" environmentnya dengan Dreamweaver jika dibanding dengan software-software lain yang sudah saya sebut diatas (ini pendapat pribadi), jadi rasanya lebih nyaman aja.

Pastinya masih banyak lagi software IDE lainnya yang tersebar di Internet, seperti Zend Studio, dll. Lain waktu akan saya sempatkan lagi melakukan tes perbandingan software-software tersebut :-D
