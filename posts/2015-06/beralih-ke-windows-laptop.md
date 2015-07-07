title: Beralih ke windows laptop
date: 2015/06/07

Setelah berpindah perusahaan sekitar 4 bulan yang lalu, saya difasilitasi satu unit laptop Dell Lattiude E7440 dengan Windows 7. Saya cukup _galau_ merespon ini. Disatu sisi laptop yang diberikan sangat bagus spesifikasi dan build qualitynya (terutama layar IPS dan keyboardnya yang jauh lebih superior dibanding Macbook Air saya), tapi disisi lain saya sangat tidak terbiasa menggunakan OS Windows.

Alhasil beberapa bulan diawal saya seringkali menghabiskan waktu memncari pengaturan yang tepat agar bisa nyaman menggunakan laptop ini. Targetnya adalah harus tetap menggunakan linux sebagai platform utama. Ini saya capai dengan berbagai macam cara:

**1. Menginstall Ubuntu Desktop di Virtualbox**

Permasalahannya di VirtualBox adalah Ubuntu Desktop terasa sangat lambat, bahkan setelah di tweak maksimum (HW accell, full RAM, dsb). Untuk menggerakan jendela aplikasi saja sudah cukup lambat, terlebih lagi aplikasi yang saya sering gunakan (Gnome Terminal) cukup lambat rendering teksnya di VM ini, terpaksa opsi ini saya tinggalkan.

**2. Menginstall Ubuntu server di Virtualbox, lalu development melalui SSH**

Opsi kedua adalah ubuntu server yang dihubungkan melalui SSH, berikut cara-cara yang saya gunakan:

_2.1 Menggunakan full SSH untuk development_

Saya cukup bertahan lama dengan opsi ini, yaitu menggunakan ubuntu server lalu koneksi menggunakan aplikasi SSH seperti Putty dsb, lalu coding dilakukan menggunakan gabungan tmux dan vim (dan shell tentunya), permasalahnnya adalah:

* Putty tampilan dan fiturnya sangat minim
* Kitty, alternatif dari putty (dan aplikasi SSH lainnya) tidak memuaskan
* MobaXTerm, aplikasi SSH, cukup memuaskan tapi terasa bloated
* Tidak ada xserver sehingga fitur seperti clipboard sangat sulit (tidak konvensional)


_2.2 Coding di windows dan sisanya via SSH_

Berbagai permasalahan menggunakan SSH client saya coba minimalisir dengan coding menggunakan desktop text editor seperti SublimeText, namun permasalahan baru muncul:

* Repository harus dishare antara guest dan host. Samba, Unison, network drive, dan shared folder semuanya sangat lambat untuk repository besar. Perintah seperti `git status` atau yang lain yang harus menjalankan operasi I/O yang besar akan memakan waktu 10-15 kali lebih lama.
* Windows dan Linux memberlakukan filesystem dengan berbeda, seperti line-endings dan filemode, sehingga ketika repository dishare, commit behaviour bisa berbeda antara linux dan windows.


**3. Menginstall Ubuntu Desktop di VMWare Player**

Opsi terakhir ini cukup lucu karena selain kembali ke opsi pertama, saya kali ini menggunakan VMWare Player, yang saya nggak pernah coba sebelumnya. Dan saya cukup kaget, ternyata VmWare Player di windows bisa menjalankan Ubuntu Desktop dengan sangat cepat, bahkan hampir mirip seperti native installation. Akhirnya saya menggunakan opsi ini. Namun tetap ada masalah di awal-awal, seperti ketika saya menggunakan 3 monitor, terasa cukup lambat, jadi saya cuma menggunakan 2 monitor saja sekarang. Juga ketika laptop saya ditutup layarnya, sepertinya Ubuntu tetap berjalan sehingga laptop menjadi panas, solusinya adalah saya harus suspend vmnya secara manual.

Untuk saat ini, Ubuntu Desktop di VMWare adalah opsi yang sepertinya akan saya gunakan untuk waktu yang cukup panjang, ketika saya pikir untuk berpindah kembali ke MacOS mungkin akan lebih rugi karena tidak destroyable seperti sebuah VM, dan saya lebih prefer debian terutama package managementnya ketimbang OSX.
