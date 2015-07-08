title:How to make a window in C++
date:2007-09-24 10:08:06

Tutorial n00b ini dahulu kala dakuw submit di GameDevID (Indonesia Game Developer) untuk berbagi pengetahuan seputar dasar-dasar win32 programming di lingkungan C++, nggak ada salahnya deh di submit juga di sini :-D. Silahkan ikutin sampai selesai, cocok untuk kamuw-kamuw yang baru belajar C++, lupakan dulu wizard! :-D
<!--more-->
Tutorial kali ini akan membahas tentang bagaimana cara membuat sebuah window di C++, disini kita akan menggunakan Microsoft Visual C++ 6.0 sebagai IDEnya (Integrated Development Environment). Selain VC++, kita juga bisa menggunakan IDE lainnya yang bisa didapatkan secara gratis di internet, seperti CodeBlocks dan DevC++. Sebelum memulai membuat game, kita tentu membutuhkan "ruang" untuk tampilan game itu sendiri. Ruang yang dimaksud disini adalah Window. Ada beberapa cara untuk membuat window di C++, yang paling mudah mungkin adalah dengan Wizard, namun Wizard dapat menimbulkan pemborosan resource karena memasukan file-file header yang mungkin tidak akan kita gunakan nantinya. Baiklah, langsung saja kita mulai dengan membuat project baru : Pertama-tama, buka program Microsoft Visual C++ 6.0, kemudian pilih menu File &gt; New (atau dengan menekan shortcut CTRL + N). Pada dialog New Project, pilihlah Win32 Application dan beri nama "Tutor1" (atau terserah), lihat gambar 1.0.
<a href="http://kecebongsoft.files.wordpress.com/2007/09/cpp_1.JPG">
 ![image](/img/wordpress/2007-09-cpp_1.thumbnail.JPG)
</a>
Kemudian akan muncul Win32 Application Wizard seperti gambar 1.1, pilih An Empty Project kemudian tekan tombol Finish.
<a href="http://kecebongsoft.files.wordpress.com/2007/09/cpp_21.JPG">
 ![image](/img/wordpress/2007-09-cpp_21.thumbnail.JPG)
</a>
Akan muncul report bahwa project Tutor1 telah berhasil dibuat, Sekarang klik tab FileView pada workspace window, expand (klik tanda plus) item
<strong>
 Tutor1 Files
</strong>
kemudian klik folder
<strong>
 Source Files
</strong>
(Gambar 1.2).
<a href="http://kecebongsoft.files.wordpress.com/2007/09/cpp_3.JPG">
 ![image](/img/wordpress/2007-09-cpp_3.thumbnail.JPG)
</a>
Setelah memilih folder Source Files, pilih menu File &gt; New (atau tekan shortcut CTRL + N) untuk membuat file baru. Pada window New File, pilih C++ Source File kemudian beri nama main.cpp, file ini akan dipanggil ketika project dijalankan, kita juga bisa menamakannya sesuai dengan nama project (mis : tutor1.cpp). Kemudian klik OK, akan muncul satu item baru pada folder Source Files, yaitu file main.cpp. Buka file tersebut dengan mengklik 2 kali item main.cpp. Kemudian ketik sintaks berikut :

	:::txt
#include 

LRESULT WINAPI MsgProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam){
	switch (msg){
	case WM_DESTROY:
		PostQuitMessage(0);
		return 0;
	case WM_PAINT:
		ValidateRect(hWnd,NULL);
		return 0;
	}
	return DefWindowProc(hWnd,msg,wParam,lParam);
}

INT WINAPI WinMain(HINSTANCE hInst, HINSTANCE, LPSTR, INT){
	WNDCLASSEX wc={ sizeof(WNDCLASSEX), CS_CLASSDC, MsgProc, 0L, 0L,
					GetModuleHandle(NULL), NULL, NULL, CreateSolidBrush(RGB(0,0,255)), NULL,
					"Tutor1",NULL};
	
	RegisterClassEx(&amp;amp;wc);

	HWND hWnd=CreateWindow("Tutor1","Latihan Pertama",
							WS_OVERLAPPEDWINDOW, 100,100,300,300,
							GetDesktopWindow(),NULL,wc.hInstance,NULL);

	ShowWindow(hWnd,SW_SHOWDEFAULT);
	UpdateWindow(hWnd);

	MSG msg;
	while(GetMessage(&amp;amp;msg, NULL, 0, 0)){
		TranslateMessage(&amp;amp;msg);
		DispatchMessage(&amp;amp;msg);
	}


	UnregisterClass("Tutor1", wc.hInstance);
	return 0;

}

Baris pertama (include) berfungsi untuk memasukan file header windows.h kedalam project kita, file windows.h berisi fungsi-fungsi yang dipergunakan untuk memanajemen window (mengubah, membuat, menutup, dll). Fungsi MsgProc adalah sebuah event handler yang akan mengatur pesan-pesan yang keluar masuk pada program kita. Pada dasarnya window itu berbasis pesan (yang dikirim oleh system), ketika program ditutup, tampilan di update dan sebagainya, sebagian besar di perintah melalui pesan. Pada umumnya fungsi MsgProc hanya berbentuk seperti diatas (jarang diubah). Seperti yang ada di kode, ada case WM_DESTROY yang menghandle proses ketika window akan ditutup, kemudian ada case WM_PAINT yang menghandle ketika tampilan window diubah, dsb. Fungsi MsgProc adalah mutlak harus dimasukan setiap membuat window, karena fungsi inilah yang menghandle semua pesan yang keluar masuk program kita. Di baris selanjutnya ada fungsi WinMain, yaitu fungsi yang dipangil pertama kali ketika program dijalankan (berlaku untuk Win32 Application). Tidak banyak yang saya jelaskan di fungsi ini karena parameternya kebanyakan tidak berubah. Pertama-tama fungsi ini akan membuat sebuah class window dengan nama class Tutor1, fungsi CreateSolidBrush akan mengisi window kita dengan warna biru (RGB 0,0,255). Kemudian fungsi RegisterClassEx akan meregistrasi kelas kita kedalam sistem. Setelah class terdaftar, kita bisa membuat window dengan fungsi CreateWindow, parameter pertama ("Tutor1") adalah sesuai dengan nama class, kemudian parameter kedua adalah caption window. Kita juga bisa mengisi posisi left,top, lebar serta tinggi window (100,100,300,300). Yup, class sudah terdaftar dan window sudah dibuat, sekarang kita tinggal menampilkannya dengan fungsi ShowWindow dan UpdateWindow. Tapi selanjutnya kita akan menemui kode While..., kenapa harus pakai perulangan While?. Jika Anda melihat pada baris terakhir, return 0 adalah akhir dari fungsi utama atau dengan kata lain akhir dari program, jika kita tidak "menahan" proses agar tidak mencapai "return 0", maka program akan langsung ditutup ketika dijalankan. Karena itulah kita membutuhkan kode perulangan (while). Semua pesan masuk akan di translate dan di dispatch, jika pesannnya adalah WM_DESTROY, barulah program akan ditutup. Sekarang jalankan program kita dengan menekan tombol F5, maka akan muncul tampilan seperti gambar 1.3 :
<a href="http://kecebongsoft.files.wordpress.com/2007/09/cpp_4.JPG" title="">
 ![image](/img/wordpress/2007-09-cpp_4.thumbnail.JPG)
</a>
Sekarang window kita telah berhasil dijalankan!. Untuk lebih mengerti tentang sintaks-sintaks diatas, cobalah untuk mengubah beberapa parameter yang tertera dan lihat hasilnya dengan menekan tombol F5. Teruslah berlatih dan mencari referensi di internet untuk mengasah kemampuan.
