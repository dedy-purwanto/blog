title:Mendapatkan nilai FPS
date:2007-11-12 06:33:55
status:draft

FPS atau frame per second adalah satuan yang dipakai untuk menyatakan banyak frame yang ada tiap detiknya. Dalam game, tinggi/rendahnya nilai FPS sangat penting demi kenyamanan memainkan game, jika ada game yang fps-nya dibawah 10fps berarti dalam 1 detik game tersebut menampilkan 10 urutan gambar, sehingga akan terlihat patah-patah.

Penting bagi programmer game untuk mendapatkan nilai fps dari game yang ia kembangkan, ini untuk mengukur performance sebuah game (terutama dari sisi grafis). Ada banyak cara mendapatkan nilai fps, salah satunya adalah dengan mencatat jumlah frame yang telah dirender di satu variabel, setelah satu detik jumlah tersebut disalin ke variabel lain kemudian variabel pertama direset :
[sourcecode language='cpp']
int GetFPS(){
	static int lasttick = 0; // mencatat waktu (milidetik)
	static int lastframerate = 0; // mencatat nilai fps terakhir
	static int framerate = 0; // mencatat jumlah fps sekarang

	if (GetTickCount() - lasttick >= 1000) // jika waktu sudah satu detik
	{
       	 	lastframerate = framerate; // salin jumlah fps ke variabel nilai fps terakhir
       	 	framerate = 0; // reset jumlah fps
        	lasttick = GetTickCount(); // reset waktu
	}

	framerate++; // tambah jumlah fps
	return lastframerate; // return nilai fps terakhir
}[/sourcecode]
Atribut static dipakai agar variabel-variabel tersebut menyimpan nilai terakhirnya meskipun proses telah keluar dari fungsi (terkecuali program di-destroy/tutup). Jumlah framerate kita increment setiap kali masuk fungsi, panggil fungsi diatas pada fungsi render yang ada di program kita.Sebagai catatan, kalau menggunakan CD3DApp (class tambahan dari DirectX9SDK), di class tersebut juga ada utility untuk menghitung fps. Mungkin masih banyak cara menghitung fps lainnya, cara diatas adalah salah satu yang general dan bisa dipakai diberbagai macam graphics lib (D3D, DDraw, OpenGL, dll).