title:Google Chrome 10 dirilis, Javascript 64% lebih cepat
date:2011-02-23 14:23:20
status:draft

Versi Beta pertama dari <a href="http://kecebongsoft.wordpress.com/2008/09/03/review-google-chrome/">Google Chrome</a> 10 sudah dirilis minggu kemarin, versi baru ini membawa Javascript engine yang lebih cepat. Sejak <a href="http://kecebongsoft.wordpress.com/2008/09/03/review-google-chrome/">review pertama saya</a> tentang Google Chrome tahun lalu, Chrome sudah cukup cepat dan stabil, dan dalam bulan ini, Google telah merilis versi 9 dan 10 Beta.

Chrome versi 9 masih memakai mesin Javascript V8, namun untuk versi 10 beta, Chrome telah mengganti V8 dengan sebuah Javascript engine baru, dan hasil benchmark yang dilakukan oleh <a href="http://www.computerworld.com/s/article/9210299/Google_ups_speed_of_Chrome_10">Computerworld</a> menunjukan bahwa Chrome 10 punya mesin javascript yang 64% lebih cepat dari V8.

Chrome sendiri sudah melakukan berbagai optimisasi, dengan codename <a href="http://blog.chromium.org/2010/12/new-crankshaft-for-v8.html">Crankshaft</a>, yang sudah dirilis pada V8. Namun implementasinya baru "diselipkan" di Chrome 10 Beta.<!--more-->

Ide dasar Crankshaft adalah dengan melakukan optimisasi code yang sering di panggil, seperti async request (AJAX), dan Crankshaft tidak melakukan optimisasi pada code yang cukup jarang di eksekusi. Sehingga aplikasi web yang mempunyai banyak rutin berulang akan mendapatkan keuntungan yang besar dari Crankshaft ini.

Beberapa fitur lain yang ditambahkan pada Chrome 10 adalah hardware accelerated video, yang bisa mempercepat proses rendering video, beberapa perubahan tampilan pada browser option, sinkronisasi password otomatis, dan beberapa fitur tambahan pada sekuriti.

<a href="http://www.google.com/landing/chrome/beta/">Download Google Chrome 10 Beta disini</a>

&nbsp;