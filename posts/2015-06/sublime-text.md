title: SublimeText
date: 2015/07/08

> Seseorang memperhatikan saya saat coding dari belakang, dilihatnya saya tidak menyentuh mouse sedikit pun. _"He is that guy"_ – mungkin itu batinnya. Memang saya sudah menggunakan vim selama bertahun-tahun, sampai akhirnya beberapa hari yang lalu saya mulai mencoba alternatif lain: SublimeText.

Ya ya, saya memang sangat telat, SublimeText sudah dipuja-puja sejak bertahun-tahun lalu. Belakangan ini saya ingin mencari alternatif text-editor selain vim berhubung saya juga sedang [berganti setup](/2015/06/beralih-ke-windows-laptop.html).

Menurut saya vim masih tetap editor yang sangat-sangat powerful, dan alasan saya menggunakakn vim adalah system modal editing-nya yang sangat intuitif, vim grammar yang bisa dibuat jadi apa saja, serta integrasi kuat dengan terminal sehingga bisa digunakan dimana-mana.

Tapi selama bertahun-tahun memakai vim, tidak sedikit keluhan saya seperti:

* _Code completion_: Mulai dari CTags hingga plugin YouCompleteMe, selalu saja ada kurangnya, dan setupnya juga tidak mudah.
* _Lag_: Ini bisa disebabkan banyak hal, mulai dari plugin, shell, color-scheme sampai file yang kita edit.
* _Inkonsistensi color-scheme_: Karena mengikuti shell, maka seringkali saya harus _berjibaku_ dengan pengaturan warna, hal yang sebenarnya bisa dilakukan dengan simple oleh editor lainnya.
* _UI yang terbatas oleh kapabilitas shell_: Ini pain-point yang paling tinggi, karena vim hidup didalam terminal, maka semua fitur dan plugin vim hanya bisa berjalan sejauh yang diperbolehkan oleh shell, contoh untuk mixed type-face, atau floating popup, atau UI lainnya yang tidak bisa dilakukan di shell.
* _Plugin yang terlalu pintar_: Seringkali plugin yang saya gunakan lebih banyak membuat asumsi sendiri (bahkan setelah di-costumize), sangat terasa tidak intuitif
* _Clipboard yang tidak konsisten_: Ini lebih kepada nature dari vim dan shell itu sendiri. Tapi tetap saja, harus recompile vim, lalu mengatur jenis clipboard dan memastikan kita menggunakan `:set paste` untuk beberapa jenis teks dan `:set nopaste` untuk teks lainnya, terasa terlalu micro-managing.

Kekurangan diatas juga bisa dibilang fitur di vim, karena sebagian darinya memungkinkan vim untuk melakukan hal-hal yang lain. Tentu saja saya akan masih tetap menggunakan vim, namun mungkin untuk saat ini saya ingin mencicipi text-editor yang sedang dielu-elukan: SublimeText.

Menurut saya SublimeText mencoba mengambil jalur tengah antara power-user (vim) dan ease-of-use untuk mengurangi learning curvenya. Contohnya fitur power-user di ST adalah shortcuts yang variatif untuk modifikasi teks, omni search, serta plugin yang banyak.

Sebagai orang baru di ST, saya merasa cukup nyaman menggunakan editor ini. Pastinya tetap saja ada hal-hal aneh yang terjadi seperti side-bar ST yang tiba-tiba tidak menampilkan apa-apa, dan bisa bagus dengan sendirinya setelah beberapa kali restart. Serta harus menginstall package manager melalui console ST yang saya rasa tidak intuitif.

Terlepas dari itu, ada beberapa hal yang saya cukup suka di ST seperti:

* _Omni search_: Untuk command (CTRL+Shift+P), file (CTRL+P), symbol (CTRL+R) dan lain sebagainya yang saya rasa jauh lebih intuitif ketimbang apapun yang pernah saya gunakan di vim. Contohnya plugin CTRL+P di vim, yang harus meng-index direktori serta hasil searchnya seringkali mengurutkan file yang ingin saya buka di paling ujung.
* _Package manager_: Vim punya Vundle untuk manajement pluginnya, cukup mudah, tapi di ST jauh lebih mudah karena kita tidak perlu meng-copy-paste repository ke file konfigurasi (.vimrc), cukup melalui omni-search saja.
* _GUI yang ekstensible_: Contohnya adalah plugin GitGutter, BracketsHighligter dan Anaconda yang bisa menggunakan gutter bar secara bersama-sama sehingga menambahkan informasi seperti change-list, scope serta error list. Di-vim ini mungkin saja tapi hasil yang ditampilkan biasanya tidak memuaskan atau tumpang-tindih. Juga ada plugin seperti MarkdownEditing yang mengubah tampilan file Markdown menjadi lebih readable saat editing (text-width nya lebih sempit, type-face nya berubah tergantung style, dll)
* _Sidebar_: Ya, di vim memang ada NERDTree dan sebagainya, tapi menurut saya sidebar di ST masih lebih intuitif, mungkin karena naturenya juga adalah desktop application sehingga bisa lebih _dipercantik_

Serta fitur-fitur lainnya seperti quick-view dan yang lain. Tapi ada juga yang saya masih harus menyesuaikan diri, seperti shortcut di ST yang jenisnya adalah chord ketimbang grammar di vim, sehingga contohnya untuk menseleksi teks didalam bracket, kita harus menggunakan CTRL+SHIFT+M, sementara di vim lebih make-sense dengan grammarnya `vi(` (select inside `(`). Saya juga kehilangan modal editing di vim dengan menggunakan sublime, fitur yang menurut saya paling besar di vim. Memang di ST ada plugin Vintage dan sejenisnya, tapi setelah dicoba hasilnya jauh beda dengan native vim, dan shortcut-nya pun seringkali bentrok dengan ST.

Sekarang saya masih akan menggunakan ST dan melihat apakah editor ini bisa membuat saya lebih produktif ketimbang vim. Pastinya saya masih akan sering menggunakan vim karena masih akan berurusan dengan text-editing di server.

Apakah Vim dan ST bisa dibanding-bandingkan? Menurut saya lebih banyak "tidaknya" ketimbang "ya". Karena nature vim sangat berbeda dibanding desktop text-editor, dengan modal editing, integrasi terminal dan sebagainya. Menurut saya sangat baik untuk menguasai keduanya sehingga kita bisa produktif baik di server maupun di desktop.
