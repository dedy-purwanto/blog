title: Server Murah Meriah
slug: server-murah-meriah
date: 2015-04-09
tags: komputer

Ini adalah perkembangan dari tes server [murah meriah di Digital
Ocean](/2015/04/berpindah-server.html), pada dasarnya saya ingin 
memiliki server yang bisa dipakai untuk hal-hal pribadi 
(web development, blog, dll) yang sifatnya sangat ringan, bisa 
dihapus sewaktu-waktu, ekperimental dan harus bisa
"diapa2in" stacknya tanpa harus terpaku oleh provider. Kriterianya:

* Biaya perbulan harus semurah mungkin
* Linux 
* Full access (VPS atau dedicated)

Setelah survei akhirnya saya memilih DigitalOcean VPS dengan paket
$5/bulan (1 core, 512MB RAM, 20GB SSD) yang kemudian 8GBnya saya jadikan swap.

Setelah beberapa hari dijalankan dan di load test menggunakan Siege,
ternyata cukup tahan juga untuk skala pribadi, berikut service yang
sedang saya jalankan:

* Nginx (3 reverse proxy dan 1 static website)
* RabbitMQ
* Reddis
* Supervisor
* Postgres
* Gunicorn (Jumlah 3 website: Sentry, Gunnery dan 1 project pribadi)
* Beberapa daemon seperti Celery, dll.

Berikut adalah monitoring server selama 24 jam terakhir:

![NewRelic](/img/newrelic-do.png)

Tentu saja ada performa yang harus dikorbankan tapi untuk skala pribadi
performanya terasa lebih dari cukup, jika saya punya project eksperimen
yang nantinya harus diseriuskan, saya cukup jalankan VPS terpisah dengan
spesifikasi lebih tinggi. Keuntungannya menggunakan VPS kecil + swap ini
ketimbang PaaS atau shared hosting seperti Webfaction adalah untuk
menjalankan beberapa aplikasi / service, kita tidak harus terpaku pada
limit memory yang diberikan, jika tidak cukup, kita bisa tambahkan
sendiri melalui swap. Untuk skala pribadi ini berguna sekali karena
performa bukan prioritas, yang lebih ditekankan adalah fleksibilitas
dalam melakukan berbagai hal tanpa harus ada restriksi (terutama RAM).

Seringkali saya terhalang untuk hosting project pribadi di server yang
dulu karena terpaku pada RAM dan fleksibilitas (dulu saya pakai shared
hosting), dan harganya pun lebih mahal, dimulai dari $10 dan
kelipatannya untuk setiap penambahan RAM 512MB/1GB. Dengan paket $5 dari
DO yang saya tambahkan swap ini, saya bisa setup berbagai macam hal,
resikonya adalah:

* Server saya akan semaput jika loadnya sedikit lebih tinggi.
* Performa untuk memory-sensitive operation akan sedikit lambat karena
  sebagian besar akan menyentuh swap.

Resiko diatas secara pribadi bisa diterima karena tidak ada data dan
sistem penting yang ada di server, semua yang ada di server
(konfigurasi, project dan data) juga ada duplikatnya di GitHub,
Bitbucket atau S3.

Dengan begini saya punya fleksibilitas untuk meletakkan software seperti
web pribadi, jenkins, git server, chat server atau apapun juga karena 
saya punya full access ke server, dan harganya termasuk sangat murah
sehingga tidak jadi beban kalaupun servernya tidak saya sentuh
berbulan-bulan :)
