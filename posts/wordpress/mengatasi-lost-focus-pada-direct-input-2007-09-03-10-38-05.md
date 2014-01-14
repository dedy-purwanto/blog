title:Mengatasi lost focus pada Direct Input
date:2007-09-03 10:38:05
status:draft

Direct Input adalah salah satu bagian dari DirectX yang digunakan untuk memanajemen inputan user baik berupa keyboard, joystick, mouse, dan lain sebagainya. Belakangan ini dakuw lagi mencoba menggunakan direct input untuk memproses inputan keyboard. Inputan user tersebut diawasi dalam sebuah looping. Tapi muncul sebuah masalah...
<!--more-->Ketika program kita kehilangan fokus (user mengklik program lain atau menekan alt+tab), kemudian setelah program kita mendapatkan fokus kembali, direct input tidak lagi bekerja. Hmm.. Setelah usut punya usut, ternyata direct input gagal meng-acquire device ketika program kehilangan fokus. Di dokumentasi Software Development Kit (SDK) juga tidak menyertakan sample untuk menghandle direct input ketika program kehilangan fokus. Gimana ya caranya mengetahui direct input gagal di acquire?. Di contoh direct input pada dokumentasi SDK, ada sebuah komentar yang mengatakan bahwa dalam sebuah looping, kita bisa menangkap error yang dibuat oleh direct input, sehingga kita bisa tahu direct input kehilangan fokus atau tidak. Jadi dakuw mengikuti nasehat komentar tersebut, dan berhasil :-D. So here is the damn stuff :
<pre>
// hr adalah HRESULT
// lpdiDevice adalah LPDIRECTINPUTDEVICE8
hr=lpdiDevice-&gt;GetDeviceState(sizeof(buffer),(LPVOID)&amp;buffer);

if(FAILED(hr)){

 if(hr = DIERR_INPUTLOST){

 	hr=lpdiDevice-&gt;Acquire();

 }

}</pre>
Kode tersebut diletakan dibagian awal dari sebuah looping direct input. Anggaplah kita sedang membuat function looping untuk menangkap inputan keyboard, maka kode diatas diletakan dibagian awal function looping. Yang pernah punya masalah yang sama silahkan mencoba kode diatas :-D.