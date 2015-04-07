title: Berpindah server
date: 2015-04-07

Beberapa minggu terakhir ini saya sedang gencar-gencarnya mencari server
pribadi yg baru, karna berbagai alasan saya sudah tidak berminat lagi
berlangganan di shared hosting WebFaction. Kriteria saya adalah:

* Akses penuh (sudo, instalasi software, dll).
* Punya cukup RAM.
* Letaknya di Asia Pacific / US, untuk mengurangi latency.
* Akan dipakai untuk project pribadi yang skalanya kecil.
* Murah semurah-murahnya VPS.

Saat ini saya berlangganan WebFaction seharga $9.5/bulan dengan
fasilitas:

* SSH
* 512MB Application memory
* Database (MySQL, Postgres), RAM terpisah

Sewaktu saya hanya sekedar membuat aplikasi Django tanpa perlu software
lain seperti Memcached, Reddis, atau RabbitMQ, WebFaction serasa cukup,
dan pada waktu itu saya juga belum mengetahui alternatif lainnya (selain
EC2), sehingga saya bertahan disana selama hampir 2 tahun, meskipun
begitu banyak sekali hal-hal yg membuat saya frustasi dalam mengelola
personal project di WebFaction:

* Setup yang tidak standar ketika memerlukan software seperti yg disebut
  diatas.
* Application memory yang cepat habis, 3 Django application dengan
  traffic yang sangat kecil sudah memakan lebih dari 512MB sehingga
  beberapa harus di-kill paksa oleh WF.
* _Stuck_ dengan Apache dan konfigurasi yg sudah disediakan, jika ingin
  menggunakan yg lain, harus melewati sederet kompilasi dan membuat
  custom port application yang terlalu rumit untuk ukuran personal.

Seiring waktu saya juga menemukan beberapa opsi lain seperti:

* Hetzner: Dedicated i7 + 32GB RAM seharga $53/bulan, murah tapi
  letaknya di Jerman, dan masih terasa terlalu mahal, dan ada setup fee
  yg juga mahal.
* SoYouStart dari OVH: Dedicated i7 + 32GB RAM seharga $49/bulan, murah
  tapi setup fee nya juga mahal, dan katanya setupnya juga memakan
  waktu.
* EC2: Fleksible, tapi kalau sudah dihitung perbulan tetap saja mahal,
  dan untuk yg medium, RAMnya masih terhitung sangat kecil dengan harga
  yang sudah lumayan mahal (sekitar $30-50 untuk 2-4GB).
* Sederet opsi VPS dan PaaS: Linode, DigitalOcean, Heroku, GAE, dll

Dari semua opsi tersebut, saya memutuskan untuk mencari VPS ketimbang
PaaS karena tidak mau dibatasi oleh platform. Permasalahannya adalah
semua VPS yang saya dapati selalu mencharge kelipatan $10 untuk upgrade
memory, dan paket terkecil selalu terasa terlalu kecil RAM-nya
(rata-rata dari 1GB).

Entah kenapa, tapi karena berbagai alasan (yang saya dapati di
internet), memang beginilah keadaannya sekarang, server-grade RAM masih
menjadi barang mahal, setidaknya itu menurut saya. VPS $40/bulan untuk 
4GB RAM menurut saya masih terlalu mahal, terlebih lagi 4GB seperti
bukan apa-apa.

Akhirnya saya berencana mensiasati permasalah RAM dengan swap partition,
karna toh aplikasi yang saya jalankan tidak akan besar load nya,
sekarang targetnya adalah: Cari VPS termurah dengan RAM yg masih masuk
akal, dan cari yang SSD agar performa swap-nya lebih baik.

Setelah survei, DigitalOcean sepertinya yang paling cocok, plus saya
pernah mencoba layanan ini sebelumnya dan memang cukup simpel, saya
mengambil paket yang paling rendah, $5/bulan dengan 512MB RAM dan 20GB SSD. 
Kemudian saya membuat swapfile sebesar 8GB, sisanya (12GB) lebih dari
cukup untuk OS, software dan file-file project saya.

Setelah menginstall semua software dan menjalankan berbagai service
seperti nginx, reddis, rabbitmq, gunicorn, dan lain-lain, 512MB+8GB swap masih
terasa cukup lancar, total sejauh ini yang terpakai semua adalah sekitar
600-750MB. Ada momen-momen dimana terasa lambatnya menggunakan swapfile,
seperti ketika menginstall software atau memory-sensitive task lainnya,
tapi selebihnya perbedaannya cukup kecil, web yang saya host di server
tersebut bisa dijalankan dengan cukup lancar (dengan traffic yang kecil).

Pada akhirnya saya rasa ini adalah pilihan yang paling tepat, plus
DigitalOcean memungkinkan kita untuk melakukan resize instance (menambah
RAM) jika diperlukan tanpa harus men-setup semua dari awal. Dulunya saya
merasa risih sekali jika harus membayar $10 atau lebih untuk sebuah
server pribadi yang bisa dipakai sewaktu-waktu untuk personal projects,
tapi sekarang sudah jauh lebih lega karena langganannya hanya $5/bulan
dan saya bisa dapat memory yang lebih dari cukup.
