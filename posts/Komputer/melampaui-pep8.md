title: Melampaui PEP8
date: 2015/04/18

> Seorang programmer bercerita kepada temannya tentang kode yang dia tulis selama seminggu lebih, tentang seberapa kompleks dan canggihnya algoritma yang dia buat. Lalu dia membuka laptopnya dan menunjukan isi dari salah satu _source file_, temannya dengan antusias melirik dan mulai _scroll_ perlahan. Tidak ingin kalah "macho", dia dengan _pedenya_ bilang "Kurang spasi nih antara _classnya_.

Terasa mirisnya? Kalau masih belum jelas: Bayangkan kamu membuat roket yang akan diikutkan di kompetisi internasional, dan ketika mengharapkan kritik konstruktif dari temanmu, dia malah bilang: _"harusnya pintu roketnya warna hijau nih"_

Dalam komunitas Python, PEP8 dikenal sebagai sekumpulan "aturan" yang mendikte bagaimana sebaiknya kode Python kita ditulis, mulai dari maksimum jumlah karakter disetiap baris, jumlah spasi antara _class_, _function_ dan _imports_, sampai dengan gaya penulisan nama _class_ dan _variables_. Contoh sebagai berikut:

    #!python
    p=1 # Jelek
    p = 1 # Bagus
    
    cetak_dokumen( file,printer ) # Jelek
    cetak_dokumen(file, printer) # Bagus
    
Selama ini PEP8 sudah cukup bisa mengakomodir serta "mendamaikan" berbagai perseteruan dikomunitas Python, setiap kali ada perbedaan gaya penulisan kode antara programmer satu dan yang lain, kita selalu mengembalikannya ke PEP8. Banyak bahasa pemrograman lainnya yang tidak punya paduan resmi seperti PEP8 ini sehingga tidak ada kejelasan dan selalu ada perbedaan antara setiap programmer dan _codebase_, seperti:

    #!javascript
    function a(){
        alert("hello")
    }
    
    function b()
    {
        alert("hello")
    }
    
    function c(){ alert("hello"); }
    
    function d()
        alert("hello")
        
    function e()
        alert("hello")
        alert("world")
        
Tebak `alert` yang mana yang akan muncul duluan? __Yang terakhir!__ Yup, karena _function_ yang tidak punya _curly brackets_ hanya akan mengevaluasi 1 statement setelahnya, make `alert("world")` akan terhitung sebagai _global scope_ yang akan dieksekusi pertama kali.

Jadi kita sudah mengerti betapa _gawatnya_ dunia persilatan tanpa keberadaan PEP8, tidak hanya perbedaan gaya _coding_ yang bakal tergantung oleh _lead programmer_ atau proyeknya (syukur kalau programmernya waras), tapi penggunakan semantik python yang sangat baku ini juga membuat kita terhindar dari bencana seperti diatas.

_So far all is good_, PEP8 selalu ada untuk menyelamatkan dunia, tapi semakin hari semakin terasa ada yang _nggak beres_. PEP8 mulai digunakan sebagai tuntunan hukum terhadap semua kode Python. Ketika kita melihat sebuah kode Python, alih-alih mempelajari alur logika atau konsep-konsep Pythonic yang digunakan, kita malah menghitung jumlah karakter, spasi atau juga hal-hal sepele lainnya. 

Kenapa ini menjadi masalah penting? karena sindrom "mabuk PEP8" sudah membawa berbagai efek negatif seperti:

* Si programmer terlalu mementingkan gaya penulisan ketimbang konsep pythonic sebuah kode
* Mem PEP8-kan sebuah kode dianggap sesuatu yang produktif padahal tidak
* Kode python baik yang privat maupun yang _open source_ seringkali dihinggapi _patch_ dan _commit_ PEP8 _fix_ yang datang dari orang berbeda, sehingga menyulitkan _blaming_

Saya adalah salah satu orang yang sempat mabuk PEP8, hingga beberapa waktu yang lalu saya mulai melihat beberapa tulisan dan topik tentang PEP8 bukanlah segalanya, dan membuat kode kita PEP8 _compliant_ tidak otomatis menjadikannya Pythonic, dan pada titik akhir saya menemukan video dari [Raymond Hettinger tentang Beyond PEP8](https://www.youtube.com/watch?v=wf-BqAjZb8M), sungguh membuka pengetahuan saya tentang menulis kode yang tidak hanya PEP8-kompatibel, tapi juga Pythonic.

Fokus utama dari video beliau adalah jangan sampai PEP8 membutakan pandangan kita terhadap _"gorilla in the code"_ atau "masalah yang lebih besar". Beliau membuka percakapan dengan memberikan contoh dari _Stroop effect_:

![Stroop effect](http://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Yellow_Red_Green.svg/220px-Yellow_Red_Green.svg.png)

Teorinya, lebih sulit untuk menyebutkan warna disetiap kata yang ada digambar tersebut. Warna disini adalah _"gorilla in the code"_ dan kata yang ada digambar tersebut adalah PEP-nya. Seringkali kita terlalu fokus pada kata sehingga tidak bisa menyebutkan warna dengan benar.

Beliau melanjutkan dengan memberi berbagai contoh dimana audiens seringkali tidak bisa melihat masalah utamanya dan lebih terfokus pada PEP8-nya. 

Yang lebih impresifnya lagi, beliau menunjukan sebuah kode python yang kira-kira ada 40-50 baris, kemudian beliau mulai mengubahnya menjadi kode yang pythonic, hingga akhirnya jadi kurang dari 10 baris saja, kode awalnya yang terlihat seperti kode python yang normal, ternyata lebih mirip seperti kode Java, lalu diubah menjadi pythonic.

Sayangnya topik yang beliau bawakan harus diakhiri secara terburu-buru karena waktu yang singkat, namun berikut adalah poin-poin penting yang bisa saya ambil:

* Context manager adalah fitur yang sangat _powerful_ di python yang seringkali kita lewatkan.
* _Class_ yang memiliki member `__len__` dan `__getitem__` secara otomatis akan dianggap sebagai _iterator_ sehingga kita bisa menggunakan _forloop_ terhadapnya.
* _Getter / setter_ harus menggunakan `property` dager adalah fitur yang sangat _powerful_ di python yang seringkali kita lewatkan.
* Gunakan _keyword argument_ untuk setiap parameter fungsi yang tujuannya implisit.
* Karena konsep python yang _dynamically typed_, gunakan nama variabel yang jelas.
* Gunakan `namedtuple` ketika memungkinkan, atau lebih tepatnya, gunakan semua _standard library_ kapanpun ketika memungkinkan.

Saya secara pribadi juga ingin berbagi beberapa konsep simpel yang sering saya gunakan seperti penggunaan nama variabel pendek ketika konteksnya jelas, atau ada penjelasnya seperti:

    #!python
    # Contoh 1
    for comment in comments:
        print comment.sender
    
    # Contoh 2
    for c in comments:
        print c.sender
        
Disini saya lebih memilih contoh 2 karena meskipun nama variabelnya hanya `c`, namun ada "penjelasnya" yaitu `comments`, sehingga kita bisa langsung mengerti tentang konteks si `c`. Poin lain adalah _throwaway variable_, yaitu variable yang biasanya diperlukan untuk _unpacking_ namun tidak punya tujuan khusus selain itu:

    #!python
    # Contoh 1
    name, birth = ('Dedi', 1988)
    print name
    
    # Contoh 2
    name, _ = ('Dedi', 1988)
    print name
    
Disini saya memilih contoh 2 karena setelah statement pertama, tahun lahir tidak digunakan dimanapun. Pada intinya adalah PEP8 bukan paduan atau "hukum" utama dalam pemrograman python, masih banyak konsep serta paduan lainnya yang harus dimasukan agar implementasi kita bisa disebuh pythonic.
