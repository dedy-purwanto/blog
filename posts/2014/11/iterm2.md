title: iTerm2 dan produktifitas
date: 11-01-2014

Saya salah satu pengguna berat keyboard shortcuts dan tiling windows untuk berbagai macam alasan, salah satunya adalah meningkatkan produktifitas. Sayangnya, karena resolusi layar yang hanya < 1080, tiling/window manager seperti [spectacle](http://spectacleapp.com) atau [slate](https://github.com/jigish/slate) tidak begitu berguna, tapi untuk terminal saya masih bisa mengatasinya dengan split panes. Sebagai pengguna berat terminal, saya selalu mengevaluasi terminal yang saya gunakan dalam hal kemudahan, performa, estetika dan ekstensibilitas.

Sekitar setahun yang lalu, ketika saya masih pakai Ubuntu, saya menggunakan tmux setiap harinya sebagai terminal multiplexer, dan memang sebagian besar waktu saya di depan komputer dihabiskan oleh terminal, baik itu coding, file/server management, dll. Pada saat itu tmux benar-benar terasa manfaat dan ekstensibilitasnya. Namun seiring waktu ada beberapa hal yang cukup membuat saya frustasi:

_Tampilan tab yang kurang menarik_: Seringkali saya merasa terganggu ketika menggunakan multiple tab di tmux, tampilan tabnya tidak estatik (well, ubuntu sendiri native tabnya juga tidak begitu bagus). Tidak seperti orang lain yang mengganggap estetika tools tidak terlalu penting, bagi saya ini memberikan efek kenyamanan ketika menggunakan tools tersebut.

_Degradasi performa_: Saya adalah pengguna berat split panes, dengan kebanyakan monitor wide-screens seperti sekarang, terminal dengan hanya satu pane membuat space menjadi mubazir. Masalahnya di tmux adalah ketika banyak pane yang dibuka dan berbagai verbose text mulai muncul, performanya mulai menurun, ini semakin buruk ketika saya menggunakan vim, saya harus mematikan beberapa config di vim hanya supaya terminal menjadi lebih cepat. Dan itupun masih dibawah harapan. Ini bukan murni salah tmux, dan dari hasil diskusi di stackexchange memang kesimpulannya [terminal emulator berjalan diatas OS seperti ubuntu tidak secepat terminal emulator yang lebih simple](http://unix.stackexchange.com/questions/41225/can-a-terminal-emulator-be-as-fast-as-tty-1-6).

_Clipboard yang buruk_: Ya, banyak sekali artikel tentang setting clipboard tmux di internet, tapi jarang saya temukan sebuah setting yang langsung bisa digunakan pertama kali menginstall tmux. Sulit membuat tmux harmonis dengan native clipboard tanpa menggunakan tools tertentu.

Berpindah ke iTerm2
------
Ketika mulai menggunakan OSX, saya mulai berpindah ke iTerm2, aplikasi terminal tersohor di OSX, sejauh ini iTerm2 sangat nyaman digunakan, dan berhasil menutupi semua kekurangan yang saya tulis diatas. Tampilan tab sudah diganti dengan native OSX tab, kemudian performa sudah jauh lebih baik karena split pane yang ada di iTerm2 adalah terminal yang benar-benar berbeda, bukan emulasi dengan operasi blit. Juga clipboard sudah jauh lebih baik disini, meskipun belum sempurna.

Salah satu fitur iTerm2 (dengan kontribusi oleh OSX) adalah ketika full screen, tab pane akan disembunyikan dan hanya akan muncul ketika kita menekan tombol command selama beberapa detik, berpindah antar tab bisa dilakukan tanpa harus memunculnya tab pane.

Fitur lainnya yang saya sangat suka di iTerm2 adalah kita bisa me-resize pane dengan mudah, tanpa shortcut, ini mungkin bertolak belakang dengan pola saya menggunakan komputer yang hampir selalu dengan shortcuts, namun dalam resize pane/windows bukan hal yang sering saya gunakan dan saya lebih suka tidak mengingat shortcuts yang jarang digunakan.

Sekedar sharing, di iTerm2 saya menggunakan theme [symck](http://color.smyck.org/), mengaktifkan dimming antar pane. Saya juga menambahkan shortcut command+(h/j/k/l) untuk berpindah antara split pane. Karena default shortcut untuk swith pane di iTerm2 sangat tidak nyaman.

