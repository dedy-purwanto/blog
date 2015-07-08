title: Pemrograman Visual
date: 05/08/2012

Beberapa bulan lalu saya sering cerita via chat ama temen tentang tugas
kuliahnya di kampus \*tiiiit\*, beberapa kali dia mention  tentang tugas
mata kuliah Pemrograman Visual, setelah saya intip, cukup kaget karena
materinya tidak sesuai dengan judul mata kuliahnya. Kalau kalian lagi
ambil mata kuliah Pemrograman Visual dan diajarin VB atau Java, selamat,
kalian tersesat.

Belakangan ini saya mulai terusik lagi dengan judul mata kuliah Pemrograman Visual. 
Sekarang saya pengen bahasa singkat aja (karna kalau diulas semua sumpah panjang 
banget) tentang salahnya dimana dan apa yang membedakan antara 
Pemrograman Visual dan yang bukan.

Permasalahan utamanya adalah: Mata kuliah dengan judul Pemrograman 
Visual, tapi dengan materi bahasa pemrograman seperti Visual Basic dan
Java, digabungkan dengan software seperti Microsoft Visual Studio,
Eclipse dan NetBeans.

Bahasa-bahasa tersebut bukanlah bahasa pemrograman visual
----------------------------
Dalam desain bahasa pemrograman, ada satu bagian tentang studi semantik,
yaitu proses penterjemahan sebuah valid statement dari bahasa pemrograman 
menjadi sebuah computational model, ini terdiri dari banyak sekali parameter, 
salah satunya adalah struktur sintatik, dan dimensi. 

Jumlah dimensi inilah yang menentukan bahwa bahasa-bahasa seperti VB dan
teman-temannya adalah bukan bahasa pemrograman visual, melainkan *textual
programming language*. Apa saja dimensi textual programming language?

* Dimensi horizontal, adalah semantic sebagai legal linear string, yang
  membentuk sebuah statement menjadi computational model
* Dimensi vertikal, adalah line continuation, baris ke 2 di kode
  biasanya diartikan sebagai baris selanjutnya setelah baris pertama, atau
  jalankan baris kedua setelah baris pertama

Dimensi vertikal meskipun salah satu bagian utama, tapi bukan bagian dari
semantik melainkan spatial relationship, atau flow/blok selanjutnya setelah
blok pertama (baris pertama).

Apa itu Pemrograman Visual?
-----------------------------
VPL adalah bahasa pemrograman yang menggunakan banyak dimensi yang
visually expresive sebagai semantiknya. Expresi Visual bukan berarti
tombol-tombol di Microsoft Visual Basic untuk bikin textbox atau picture
box, tapi simbol-simbol yang menjelaskan tentang alur program, hubungan
antar entity, dan impact.

Didalam VPL, saya bisa secara visual mendeklarasikan A dan B, lalu
menggabungkan keduanya dengan sebuah operator matematika, lalu melihat dampaknya
secara langsung, semua dalam bentuk diagram/simbol.

Flowchart, UML Diagram, adalah contoh dari model sebuah VPL, dimensinya
adalah spatial relationship lewat penunjuk panah, atau time-based impact
seperti perubahan data sebelum dan sesudah.

Tapi kan, saya pakai Microsoft Visual Basic/Netbeans, bisa drag & drop, itu visual!
-----------------------------
Software yang dipakai untuk 'drag & drop' itu adalah development environment,
nggak boleh disamakan dengan bahasa pemrogramannya, development environment
adalah software yang ngasih kita shortcut untuk melakukan task-task yang
umum seperti manage project, bikin GUI (Form/Tombol/Textbox/dll), bikin
build, dll, tapi dibelakang layar mereka ngehasilin kode yang kurang lebih
sama dengan kalau kita ngetik di teks editor biasa. Tampilan GUI yang dibuat
di software ini juga di simpan ke file teks manifest biasa.

Ini yang namanya VPE (Visual Programming Environment), bahasa pemrograman
seperti Visual Basic dan Java punya Microsoft Visual Studio dan Netbeans
sebagai VPEnya, namun nggak diwajibkan harus pakai karena sifat textual
programming languagenya yang dengan semantik terbatas bisa dimanage
sebagai teks biasa dan bisa di compile terpisah.

Sedangkan VPE untuk untuk Visual Programming Language (VPL) lebih bersifat
sebagai sebuah keharusan karna VPL sendiri sangat ekspresif dan sulit
untuk bekerja dengan VPL (dengan simbol dan sebagainya) tanpa menggunakan
software yang mensupport untuk membuat visually expressive syntax.


Tadi katanya Textual Programming itu berbentuk teks dan VPL berbentuk simbol, Jadi maksudnya VPL itu nggak boleh ada teks sama sekali?
-----------------------------
Ini yang paling sering disalah artikan, TP dan VP itu yang membedakan adalah
semantik, bukan tentang teks atau tidak, VPL juga punya teks di beberapa
bagian sampai batas tertentu.

Lalu kenapa ada VPL? Salah satu main goalnya adalah untuk nge-improve
language design yang sekarang konvensional seperti textual programming
language, masalah dengan textual programming language adalah sifatnya
yang restriktif sekali, nggak banyak ekspresi yang bisa kita lakukan
karena dibatasi oleh struktur sintaks & parse tree bahasa pemrograman
yang bersangkutan, sementara VPL punya lebih sedikit aturan, sehingga
result yang dihasilkan bisa bermacam-macam karena objek dan spatial
relationshipnya yang nggak terlalu restriktif.

Lalu apa efek negatifnya belajar Pemrograman Visual dengan materi yang salah?
------------------------------
Banyak sekali, ibaratkan dengan ikut les bahasa Korea tapi yang diajarkan
adalah bahasa Jepang. VPL kebanyakan bukanlah general-purpose-language,
sedangkan yang diajarkan (contoh:Java), adalah general-purpose-language,
VPL lebih domain spesifik seperti untuk edukasi, hardware, dan multimedia
seperti audio analyzer atau animation. Sedangkan bahasa seperti Java
punya fungsi/domain yang luas sekali. Ditambah lagi biasanya materi yang
diajarkan adalah tentang "Visual" yang salah, yaitu gimana cara membuat
program berbasis GUI, gimana caranya supaya waktu tombol A ditekan, keluar
gambar kucing lagi pakai topi semangka, dll. Ini bukan visual programming,
mempelajari membuat program berbasis GUI nggak akan ngajarin kita tentang
visual programming, dan bisa jadi tersesat lebih jauh, contoh: mengesampingkan
materi yang lebih penting ketimbang belajar GUI, seperti programming language
paradigm.


Post ini cuma mau menekankan perbedaan mendasar dari textual-programming
language, dan VPL. Nggak ada contoh/screenshot karena pengennya dibahas
singkat aja tentang karakteristik utama masing2 jenis programming languagenya.

Untuk paper yang ngebahas tentang VPL cukup lengkap, ada disini:
http://www.cs.auckland.ac.nz/courses/compsci732s1c/archive/2005/lectures/WhatIsVP.pdf

