title:Atom! Portal dan WML.
date:2008-02-15 08:14:33

Hari ini adalah hari pertama public beta testing untuk
<a href="http://beta.atom.web.id">
 Atom! Portal
</a>
. Sebagai informasi, Atom! Portal adalah mobile portal yang berisi konten-konten lokal seperti berita dan horoskop, serta komunitas mobile chat. Beberapa layanan lainnya akan segera menyusul seiring dengan waktu.

Jauh sebelum public beta testing ini dilakukan, bahkan beberapa waktu sebelum Atom! dibuat, tim dan saya pribadi sudah
<!--more-->
memiliki prasangka, bagaimana jika nanti orang-orang bertanya &#8220;Kenapa masih pakai WML/WAP?&#8221;. Sebagai informasi, WML (Wireless Markup Language) adalah salah satu format dokumen web yang kali pertama muncul untuk perangkat bergerak, dalam hal ini adalah ponsel. WML bisa dibilang sangat terbatas dari sisi kapabilitas. Format gambar yang hanya mendukung monokrom bitmap (WBMP), card deck system, dan banyak hal lainnya yang sangat terbatas. Hal ini memang sengaja dirancang untuk mengatasi minimnya performa perangkat mobile, kecilnya prosesor dan memori ponsel memaksa consortium untuk menerapkan standar-standar seperti diatas. Alasan lainnya adalah surfing menggunakan perangkat mobile masih mengutamakan teks sebagai konten utama. Tapi sekarang bukanlah seperti dulu, perangkat mobile sudah jauh berevolusi menjadi komputer bergerak, berbagai macam fitur multimedia sudah hampir bisa dianggap umum ada disetiap ponsel. Termasuk salah satunya adalah menampilkan dokumen web dalam format XHTML.
<b>
 Jadi kenapa masih pakai WML?
</b>
Well, meskipun semua perangkat sekarang sudah hampir mendukung XHTML, tapi tentu saja masih ada segelintir mereka-mereka yang masih menggunakan ponsel-ponsel &#8220;biasa&#8221;. Hal ini menjadi salah satu alasan kenapa Atom! masih menggunakan WML sebagai salah satu format dokumen webnya. Kemudian alasan kedua adalah, konten-konten di Atom! masih benar-benar teks. Terkecuali beberapa aksesoris untuk chat seperti emoticons.
<b>
 Jadi Atom! akan menggunakan WML terus-menerus?
</b>
Secara pribadi saya mengatakan tidak, Atom! adalah mobile content, formatnya tentu saja harus sebisa mungkin fleksibel. Kami sedari awal sudah memikirkan masa depan Atom!, bahwa portal ini akan terus berkembang dan kami tidak bisa terus-terusan menggunakan format dokumen WML dengan segala keterbatasannya. Karena itulah, portal ini dibangun dengan sedemikian rupa sehingga kedepannya bisa fleksibel, dalam artian bisa menyesuaikan dengan perangkatnya, jika hanya support WML, maka akan tampil WML, dan jika support XHTML, maka akan tampil XHTML.
<b>
 Bagaimana kami melakukannya?
</b>
Sistem Atom! adalah sistem yang memiliki beberapa sub-sistem. Tidak seperti website-website pada umumnya yang menggunakan metode struktural dan konvensional, kami me-encapsulate subsistem-subsistem Atom! serta menyembunyikan bagian internalnya. Mulai dari sisi data storage yang berisi kelas-kelas dan stored procedure. Business Layer yang juga dibagi beberapa subsistem dan modul, serta Presentation Layer yang sifatnya dinamis.
<b>
 Apakah ini sama dengan konsep template engine?
</b>
Definitely not, template engine memang memisahkan antara business layer dan presentation layer, namun business layer sendiri juga bisa berorientasikan objek dan juga bisa struktural. Atom! is fully object oriented. Semua bagian memiliki application programming interface masing-masing. Kami juga membangun &#8220;mini-smarty&#8221;. Sebuah penghubung antara output dari business layer dan format dokumen yang ada di presentation layer.
<b>
 Apakah Atom! telah mengimplementasikan &#8220;multi document format&#8221; ini?
</b>
Ya, namun untuk sekarang pada Atom! Portal, format dokumen yang kami tampilkan masih berupa WML. Namun proses translasi format dari WML ke XHTML relatif cukup mudah karena sistemnya sendiri sudah mendukung hal itu.
<b>
 Adakah contoh dari implementasi tersebut?
</b>
Yup, frontpage Atom! Portal (http://www.atom.web.id) adalah salah satu implementasi dari teknik yang kami gunakan. Ketika kita membukanya di perangkat yang hanya mendukung format dokumen WML, maka ia akan tampil sebagai format WML. Dan jika dibuka diperangkat yang mensupport XHTML, maka akan muncul dokumen XHTML.
<b>
 Bisa share sedikit tentang teknik pendeteksian perangkat mobile yg ada pada Atom! Portal?
</b>
Pengen juga bikin artikel tentang ini, tapi sayangnya ini adalah sistem internal Atom! Portal. Yang jelas nggak ada teknik deteksi browser disini ;) . Mudah-mudahan si bos besar mau berbaik hati mengizinkan anak buahnya nulis artikel tentang teknik ini, dan teknik-teknik lainnya :-p
<b>
 Sejauh apa kestabilan sistem Atom! Portal?
</b>
Ini adalah hal yang paling krusial, mungkin dari sis desain sistem sudah bisa dibilang lumayan, tapi tidak bisa dipungkiri bahwa Atom! Portal hampir tidak berbeda dengan sebuah telur, yang baru saja muncul dan benar-benar rentan akan serangan. Tentu kami sangat mengharapkan dukungan dari segala pihak untuk berpartisipasi mencoba dan menguji coba sistem ini. Karena pada akhirnya layanan ini akan dipergunakan oleh masyarakat luas :D
<b>
 Apa target-target selanjutnya dari Atom! Portal?
</b>
Untuk konten dan lain sebagainya, biarlah bos besar yang membahas :-p . Namun dari sisi internal sistem, tentu kami akan selalu berusaha meningkatkan peforma dan kestabilan sistem. Mengimplementasikan teknik-teknik yang benar dan memberikan hasil yang terbaik untuk user. Semoga ini didukung juga oleh user yang semakin bertambah setiap saat :D

Well, setelah menulis panjang lebar seperti ini, maka bisa ditarik kesimpulan, Atom! Portal bukanlah mobile content yang terfokus pada satu format dokumen saja. Sistem yang dimiliki cukup mendukung untuk membuat tampilan menjadi fleksibel. Tinggal tunggu versi XHTMLnya aja untuk dapat menikmati Atom! Portal yang lebih berwarna. Selamat mencoba Atom! Portal dan jangan lupa saran dan kritiknya :D .
