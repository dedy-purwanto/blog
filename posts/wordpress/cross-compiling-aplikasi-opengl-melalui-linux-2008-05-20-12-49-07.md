title:Cross Compiling aplikasi OpenGL melalui Linux
date:2008-05-20 12:49:07
status:draft

Beberapa bulan yang lalu aku sempat melakukan <a href="http://en.wikipedia.org/wiki/Cross_compile">cross compiling</a> aplikasi <a href="http://en.wikipedia.org/wiki/Opengl">OpenGL</a> yang kubuat di environment linux kedalam platform windows xp, dan ternyata berhasil. Kenapa harus cross compiling, ini masalah legalitas, aku sering eksperimen bikin aplikasi/game menggunakan <a href="http://en.wikipedia.org/wiki/Directx">DirectX</a> di windows tanpa memperhatikan apakah OS atau aplikasi lainnya yang ada di windowsku adalah bajakan atau tidak. Tapi belakangan ini sering kepikiran juga untuk "melegalkan" semua perangkat yang kumiliki untuk tujuan pengembangan game. Mulai dari Graphics API yang menggunakan OpenGL, modeller yang menggunakan <a href="http://en.wikipedia.org/wiki/Blender_software">Blender</a>, image editor yang menggunakan <a href="http://en.wikipedia.org/wiki/GIMP">GIMP</a>, dan lain sebagainya, dan tentu saja dengan platform linux :-D<!--more-->

Sebenarnya untuk melakukan cross compiling ada berbagai macam cara, bisa disetting langsung dari <a href="http://en.wikipedia.org/wiki/Integrated_development_environment">IDE</a> seperti <a href="http://en.wikipedia.org/wiki/Codeblocks">CodeBlocks</a>, atau bisa dengan manual menggunakan <a href="http://en.wikipedia.org/wiki/Makefile">MakeFile</a>. Tapi kali ini aku belum bisa menjelaskan detailnya karena lagi di kelas lab komputer :-D . Tapi setidaknya ada hasil yang bisa dilihat dari cross compiling ini :
<img src="http://www.gamedevid.org/gallery/4806b48da8bb0.JPG" alt="" />
<img src="http://i247.photobucket.com/albums/gg153/kecebongsoft/tuing6.jpg" alt="" align="left" /><img src="http://i247.photobucket.com/albums/gg153/kecebongsoft/tuing7.jpg" alt="" />

Ini adalah game eksperimen dari hasil cross compiling tersebut, dengan compiler <a href="http://en.wikipedia.org/wiki/MinGW">MinGW</a> dan libray OpenGL, game ini bisa dimainkan di Linux dan Windows XP, namun aku belum menyediakan source dan binary linuxnya, jadi silahkan coba versi windowsnya aja dulu :
<a href="http://www.smka-smr.sch.id/cebong/tuingtuing.zip">Download ~500kB</a>

kontrol : kiri/kanan, atas(loncat), pageup/pagedown utk zoom in/out kamera

Untuk beberapa PC, ada satu hal yang mungkin terlihat janggal yaitu gerakan bola terlalu cepat. Ini karena OpenGL (atau kode yang kubuat?) belum cukup efektif untuk menghandle opsi <a href="http://en.wikipedia.org/wiki/Vsync">Vertical Synchronization</a> yang ada pada <a href="http://en.wikipedia.org/wiki/VGA">VGA</a>, sehingga gambar yang dihasilkan menjadi terlalu cepat. Dan perlu diingat jika ingin quit dari program diatas, jangan tekan tombol close ("X") yang ada di windownya, karena proses akan tetap berjalan meskipun windownya udah di quit. Tekan ESC untuk quit.

Yup, setidaknya aplikasi diatas cukup bisa untuk membuktikan bahwa pengembangan game juga bisa berjalan diatas linux, sebenarnya hal ini sudah ada cukup lama tapi mungkin belum sepopuler pengembangan game di windows. Detail how-to cross compilingnya menyusul deh :-D

<em>ps : maap nih buat server skul lagi-lagi numpang, beberapa minggu lagi udah mau sewa server sendiri sih, ditunggu aja :-D</em>

[digg=http://digg.com/programming/Cross_Compiling_aplikasi_OpenGL_melalui_Linux]