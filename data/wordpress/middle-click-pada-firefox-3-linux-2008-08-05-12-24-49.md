title:Middle click pada Firefox 3 (Linux)
date:2008-08-05 12:24:49
status:draft

Pada Firefox 2 (Windows &amp; Linux) dan Firefox 3 (Windows), middle click biasanya digunakan untuk melakukan auto scrolling halaman dan membuka link pada tab baru. Di Firefox 3 versi Linux, middle click secara default tidak diset untuk melakukan hal yang sama. Untuk mengembalikannya, bisa dicoba cara berikut:

1. Pada address bar, ketik about:config
2. Akan muncul warning, klik tombol "I'll be careful, I Promise"
3. Cari item <strong>general.autoscroll</strong>, double klik item tersebut hingga Value-nya menjadi <strong>true</strong>
4. Cari item <strong>middlemouse.contentLoadURL</strong>, double klik item tersebut hingga Value-nya menjadi <strong>false</strong>

Firefox tidak perlu direstart, settingan baru tersebut bisa langsung dicoba. Happy hunting.