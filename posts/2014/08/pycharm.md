slug: pycharm
title: Mencicipi PyCharm
date: 31-08-2014
tags: komputer

## _Jika vim adalah sebuah keyakinan, maka saya adalah pengikut yang paling sering ragu, tidak jarang saya melirik editor lain yang tampilannya lebih wah dan lebih nge-hype, dan kali ini saya tergoda untuk meninggalkan VIM dengan melirik PyCharm_

Saya sudah acapkali melihat bagaimana satu demi satu editor teks bermunculan dan mengambil perhatian banyak orang, seperti Sublime Text dan Atom, respons dari para usernya luar biasa heboh dan __life-changing__, saya sendiri sempat tergoda dan mencoba satu demi satu, Atom adalah salah satu yang paling gagal memberikan impresi bagus. Sublime Text, tidak terlalu bagus juga, kemudian sekitar 3 minggu yang lalu saya mulai melirik PyCharm, saya memang paling banyak berkutat dengan codebase python dan membutuhkan editor yang dukungan python-nya bagus. Sebagai orang yang terkadang merogoh kocek untuk membeli software legal, PyCharm yang dibanderol 1 juta rupiah terlihat menjanjikan untuk ukuran harga, jadi saya putuskan untuk mencoba versi trial nya selama 1 bulan.

** Impresi Pertama **

PyCharm adalah editor yang seringkali dielu-elukan di komunitas online yang saya ikutin, baik itu mailing-list, maupun news-aggregator seperti HN dan Reddit, setelah menginstall versi komersial dan mencoba selama beberapa jam, memang bagus sekali PyCharm ini, mulai dari code completion, code navigation, dsb. Berikut daftar fitur yang sangat saya sukai di PyCharm:

* Code completion: Pycharm bisa membaca dengan baik codebase python yang secara desain adalah weak-typing. Semua keyword yang diberikan sangat akurat
* Code navigation: Mulai dari jump-to-definition untuk class, member dan fungsi, mencari simbol tertentu, semua sangat cepat dan akurat
* Symbol explorer: Di sidebar ada sebuah panel yang menampilkan class members di file yang sedang dibuka, yang bisa auto-focus tergantung posisi kursor kita.
* Debugging: Mulai dari breakpoints hingga stacktrace ditampilkan dengan sangat rapi dan dengan fungsi-fungsi yang bagus
* Built-in terminal: Ini cukup umum sebenanrya, tapi salah satu yang saya suka di terminal PyCharm adalah multiple tabs.
* Django: Di versi komersial PyCharm mendukugn penuh Django mulai dari project, views, pembuatan modul dan app secara otomatis, hingga Django template tag.
* Refactoring: Terasa sangat mudah melakukan refactoring di PyCharm, IDE ini bisa mencari semua usage dan kita bisa melakukan preview terhadap perubahan yang akan dibuat.
* Shortcuts: Semua fitur memiliki shortcutnya masing-masing, sebagai programmer yang terbiasa dengan VIM, maka shortcut termasuk harga mati untuk saya.
* IdeaVim: Ini adalah plugin untuk menggunakan vim mode di PyCharm, dan menurut saya adalah vim plugin terbaik diantara semua vim plugin yang saya pernah pakai, termasuk yang ada di SublimeText.
* Git diff: Fitur ini sangat berguna dan tampilannya sangat nyaman, saat saya hendak commit atau ketika sedang melakukan conflict merge.
* VCS: Fitur ini digunakan untuk melihat outstanding changes, cukup berguna meskipun agak ambigu dengan git, karena sepertinya ada beberapa bagian seperti Ignore Files yang terpisah dengan git (ignore files belum tentu di ignore di git, ambigu).

** Kekurangan Pycharm **

Meskipun banyak sekali fitur yang sangat menarik lainnya dari PyCharm, berangkat dari VIM, saya banyak sekali melakukan adaptasi dan akhirnya frustasi sendiri dengan PyCharm, mungkin bisa dibilang juga frustasi dengan konsep GUI dan IDE untuk pemrograman, berikut ketidak nyamanan saya ketika menggunakan PyCharm (dan juga IDE/GUI editor pada umumnya)

* Lambat: Ini alasan pertama yang paling mengganggu, meskipun membuka PyCharm hanya kurang dari 10 detik, tapi saya sudah sangat terbiasa sekali dengan membuka VIM yang hampir tidak ada jedanya.
* Project-oriented: Bisa dibilang mustahil untuk membuat file kosong di PyCharm, sementara saya seringkali membuat file kosong di VIM yang biasanya saya pakai untuk membuat script python/shell untuk testing pseudo-code. Di PyCharm semua file harus bernaung dibawah project, dan jika menggunakan VCS, maka harus memilih apakah file terbebut akan dimasukan ke VCS atau tidak.
* Tidak stabil: Ya, saat mencoba codebase django yang lumayan besar, saya hampir tidak bisa bekerja dengan Django template, sepertinya ada yang tidak beres dengan Django supportnya, saya sempat harus downgrade ke edisi komunitas yang tidak mensupport Django.
* Keychords: Hampir semua shortcuts di PyCharm menggunakan chord, seperti Ctrl+F1, atau ALT+F2, atau Super+B, dan tidak jarang mencakup 3-4 key, seperti CTRL+SHIFT+B. Berangkat dari vim yang menggunakan sequence dan leader key yang sangat nyaman digunakan, keychords menjadi alternatif yang sangat tidak nyaman.
* Feel: Menggunakan vim, saya menjadi akrab dengan terminal dan multiplexer. Di Pycharm, terminal seperti 2nd class citizen; keberadaannya hanya sebagai pendukung, dan terasa sekali bedanya ketika saya bisa membuka hingga belasan tabs dan splits di iTerm dan tmux dibandingkan saat menggunakan PyCharm
* Vim bindings: IdeaVim meskipun cukup bagus, tapi masih sangat terbatas, contohnya command umum seperti :tabo dan sejenisnya tidak bisa digunakan, visual select juga sering kali berperilaku tidak sesuai seperti saat di vim.
* Indentasi yang kaku: Vim bisa membaca nilai indentasi yang kita pakai pada file yang sedang kita buka, sementara di PyCharm sepertinya hanya ada 1 setting untuk indentasi dan semua file harus mengikuti standard tersebut, seringkali saya harus membuka file dengan indentasi yang kecil seperti HTML dan HAML, dan sangat sulit melakukan indentasi di PyCharm untuk file-file tersebut.
* Dukungan syntax highlighting: Di edisi komunitas, file-file yang sebenarnya cukup umum namun tidak didukung oleh edisi komunitas, akan dianggap sebagai file text biasa, contohnya HAML, benar-benar tidak ada support untuk file ini, bahkan syntax highlighting pun tidak ada, sementara di editor lain yang terbilang gratis, setidaknya ada syntax highlighting.

** Aftermath **

Akhirnya saya kembali ke vim, mengambil beberapa hal yang saya suka dari PyCharm dan meletakannya di vim, contohnya CTAGS, vim-jedi, TagBar, NERDTree dan beberapa plugin lainnya. Plugin-plugin ini memang ada yang tidak sebaik PyCharm, contohnya untuk code navigation, tapi tingkat ke-akurasiannya masih sangat bagus dan hanya melenceng di saat-saat tertentu, dan keuntungnya menggunakan vim sendiri adalah plugin-plugin ini terus diperbaharui dan alternatif selalu bermunculan.

PyCharm adalah editor yang sangat bagus dan akan saya rekomendasikan kepada siapapun yang baru mulai belajar Python ataupun yang sudah proffesional dan ingin lebih produktif (jika mereka lebih terbiasa dengan GUI). Untuk saya sendiri, saya akan masih tetap menjadi pemakai setia vim.
