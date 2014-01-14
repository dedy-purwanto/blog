title:Konsep Abstraksi, untuk siapa/apa?
date:0000-00-00 00:00:00
status:draft


<blockquote> Abstraction is the process or result of generalization by reducing the information content of a concept or an observable phenomenon, typically in order to retain only information which is relevant for a particular purpose. For example, abstracting a leather soccer ball to a ball retains only the information on general ball attributes and behaviour. Similarly, abstracting an emotional state to happiness reduces the amount of information conveyed about the emotional state. Computer scientists use abstraction to understand and solve problems and communicate their solutions with the computer in some particular computer language.</blockquote>
Abstraksi adalah pengkapsulan sesuatu, serta menyediakan interfacenya kepada client untuk menyembunyikan kompleksitas didalamnya. Kenapa ada abstraksi?. Karena pekerjaan abstraksi adalah menterjemahkan perintah kita (yang diambil dari interface) kedalam beberapa jenis dialek/bahasa/cara secara berbeda-beda, tergantung dari apa yang abstraksi hadapi.

Contoh kasus : Seorang atasan ingin menyapa semua orang jepang, cina, dan rusia yang ada di kantornya, karena dia tidak menguasai beragam bahasa, maka dia menyuruh sekretarisnya untuk menyapa orang-orang tersebut.

Disini, atasan berstatus sebagai client, dan sekretaris adalah abstraksinya. Atasan yang memberikan perintah kepada sekretaris, bisa disebut seagai mengakses interface. Orang lain pun bisa menyuruh hal yang sama kepada sekretaris asalkan perintahnya pas. Si sekretaris, mengangguk dan menyembunyikan kompleksitas yang dia miliki : menyapa dalam berbagai bahasa dan dialek. Apa yang dia katakan tergantung dari siapa yang dia temui, apakah orang jepang, cina, atau rusia.

Apakah abstraksi sama dengan pengkapsulan class biasa?, tidak. Mungkin keduanya menyimpan kompleksitas secara general, tapi kompleksitas yang dimiliki abstraksi adalah melakukan beberapa cara untuk menyampaikan pesan yang sama, sedangkan kompleksitas yang dimiliki class biasa adalah susunan algoritma untuk menyelesaikan tugas-tugas berbeda. Namun begitu, tidak menutup kemungkinan didalam class biasa terdapat objek abstraksi.

Sekarang yang menjadi pertanyaan, seandainya sang sekretaris tidak terlalu fasih berbahasa rusia, sehingga orang rusia komplain kepada atas dengan alasan tidak mengerti apa yang dikatakan sekretaris, kemudian si atasan yang juga memiliki kemampuan berbahasa rusia memperbaiki percakapan yang dilakukan sekretaris dan orang rusia tersebut.

Ups, hal ini membuat si atasan mengetahui permasalahan internal/kompleksitas yang dimiliki oleh sekretaris, yaitu berbahasa rusia. Apakah kasus ini masih pantas disebut abstraksi? Sebenarnya untuk siapa/apa abstraksi itu dibuat? untuk menyederhanakan perintah/interface kepada sekretaris? atau untuk menyembunyikan kompleksitas yang dimiliki sekretaris kepada client (atasan)?.

Mari berhenti berandai-andai, didalam dunia programming, kita mengenal interface didalam abstraksi. Salah satu makna interface adalah membiarkan client memberikan perintah secara umum kemudian abstraksi akan melakukannya sesuai dengan hal yang dia hadapi.