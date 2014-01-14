title:Mendapatkan nilai FPS - Bagian 2
date:2007-11-13 08:27:42
status:draft

Setelah post sebelumnya membahas tentang bagaimana cara mendapatkan nilai FPS dengan mengambil nilai waktu menggunakan fungsi GetTickCount(), sekarang kita akan mencoba mengambil nilai fps yang lebih presisi, kali ini menggunakan fungsi QueryPerformanceCounter dan QueryPerformanceFrequency, funsi ini akan menghitung "tick" atau clock prosesor sehingga hasilnya lebih akurat dari GetTickCount. Aturan mainnya agak berbeda dari cara menghitung FPS yang sebelumnya, urutan adalah sebagai berikut

1. Ambil nilai frekuensi tick (f)
2. Ambil nilai waktu sekarang (w1)
3. Mulai Render
4. Hentikan Render
5. Ambil nilai waktu sekarang (w2)
6. delta waktu = w2-21
7. waktu render = delta waktu/frekuensi
8. fps = 1 / waktu render

Dari urutan diatas, maka kita buat satu fungsi untuk menghitung fps dengan lebih presisi :
[sourcecode lang='cpp']
void Looping()
{	
	static double rendertime;
	static double fps;
	static  __int64 w1,w2,freq;

	QueryPerformanceFrequency((LARGE_INTEGER *)&freq);
	QueryPerformanceCounter((LARGE_INTEGER *)&w1);
	
	/* Mulai rutinitas render disini */

	/* Hentikan rutinitas render disini */
	
	QueryPerformanceCounter((LARGE_INTEGER *)&w2);
	rendertime=(double)(w2-w1)/(double)(freq);
	fps=(double)(1)/(double)rendertime;	
}
[/sourcecode]

Pertama-tama kita melakukan casting terhadap variabel w1, w2 dan freq, karena tipenya adalah integer 64 dan parameter untuk fungsi QueryPerformanceFrequency/QueryPerformanceCounter adalah LARGE_INTEGER. Pada baris terakhir, kita cast hasil delta waktu menjadi double karena tipe dari rendertime dan fps adalah double.

Met mencoba ya :D