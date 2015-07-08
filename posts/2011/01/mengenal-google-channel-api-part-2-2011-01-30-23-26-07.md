title:Mengenal Google Channel API - Part 2
date:2011-01-30 23:26:07
tags: komputer

Setelah mengenal konsep dasar dari
<a href="http://kecebongsoft.wordpress.com/2011/01/29/mengenal-google-channel-api-part-1/">
 Channel API
</a>
, saatnya kita membuat implementasi sederhana. Disini kita akan membuat sebuah aplikasi yang meng-init sebuah channel (hanya satu channel), dan mengirim token beserta client_id nya ke browser. Kemudian, di browser kita pasang satu tombol untuk mengirim pesan ke server, pesannya adalah nama kita, ketika pesan terkirim, server akan membalas dengan pesan yang lain (yaitu : "Hallo, [Nama]!"), lalu ditampilkan di browser.
<strong>
 Server Code (Python)
</strong>
Pertama  kita buat script (python) yang akan ditanam di server untuk menghandle setiap request. Lihat listing dibawah:

	:::txt
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import channel
from django.utils import simplejson
# Handler Utama
class MainPage(webapp.RequestHandler):
    def get(self):
        client_id = "mychannel" # Nama Channel
        token = channel.create_channel(client_id) # Buat channel dan ambil tokennya
        # Kirim client_id dan channel ke output
        output = template.render('index.html', {'token' : token, 'client_id' : client_id})
        self.response.out.write(output)

# Handler ketika client mengirim pesan
class MessageReceived(webapp.RequestHandler):
    def post(self):
        # Ambil client ID dan name
        client_id = self.request.get('client_id')
        name = self.request.get('name')
        # Format balasan dengan JSON
        reply = {
            'reply_message' : 'Hallo, ' + name + '!'
        }
        # Kirim balasan, parameternya (client_id, pesan)
        channel.send_message(client_id,simplejson.dumps(reply))

application = webapp.WSGIApplication(   [
                                        ('/msg',MessageReceived),
                                        ('/', MainPage)
                                        ],debug = True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

<!--more-->
Pada baris 1-5 seperti biasa kita import semua library yang diperlukan. Library yang krusial untuk Channel API adalah "channel" dan "simplejson". Kemudian di handler utama yaitu
<strong>
 MainPage
</strong>
, ada
<strong>
 client_id
</strong>
yang valuenya konstan. Karena alasan kesederhanaan code, kita akan biarkan valuenya untuk sementara konstan, nantinya akan dibahas kelemahan value yang konstan ini. Dibaris 11 kita mulai membuat channel dan fungsi
<strong>
 create_channel
</strong>
akan me-return
<strong>
 token
</strong>
. Dengan bermodal client_id dan token inilah, kita tampilkan output di browser.

Selanjutnya ada handler
<strong>
 MessageReceived
</strong>
. Sesuai dengan kasus diatas, dibrowser akan dipasang tombol yang ketika di klik, akan mengirim pesan ke server, handler inilah yang akan di-trigger ketika pesan tersebut diterima. Di handler ini juga kita bisa memilih apakah akan membalas pesan tersebut atau tidak, kita juga bisa menentukan pesan apa yang ingin kita kirimkan. Ini membuat kita bisa menghemat banyak resource.

Agar server bisa membalas pesan ke client, server harus memiliki client_id si pengirim, karenanya, setiap kali client mengirimkan pesan, harus disertai dengan client_id. Meskipun ada kasus-kasus dimana server tidak butuh client_id, seperti broadcast message. Kembali ke baris 20, client_id diambil dengan fungsi
<strong>
 get()
</strong>
, begitu juga dengan
<strong>
 nama
</strong>
(yang nantinya akan dibuat predefined di browser)

Di baris 23, kita mulai mengatur balasan yang diinginkan, disini dibuat satu array yang itemnya adalah '
<strong>
 reply_message
</strong>
'. Google App Engine sendiri menyarankan untuk membuat balasan dalam format
<strong>
 JSON
</strong>
, agar lebih terstruktur. Di baris 27, kita kirim pesan balasan ke client dengan fungsi
<strong>
 send_message
</strong>
. Parameter pertama adalah client_id, yang akan di ubah jadi hash (yang akan di match dengan token), dan parameter kedua adalah contentnya. Di parameter kedua, kita dump pesan '
<strong>
 reply
</strong>
' tadi kedalam format JSON dengan fungsi
<strong>
 dumps()
</strong>
.

Baris-baris selanjutnya menjelaskan tentang handler dan parameter lainnya yang sangat umum di GAE. That's it, script di sisi server sudah siap.
<strong>
 Client Code (HTML)
</strong>
Kemudian lihat di baris 13, baris tersebut berfungsi untuk menghasilkan output berdasarkan file template '
<strong>
 index.html
</strong>
'. Dengan begitu kita wajib menyiapkan sebuah file 'index.html', yang isinya sebagai berikut:

	:::txt
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Google Channel API - Simple&lt;/title&gt;
        &lt;script type="text/javascript" src="/_ah/channel/jsapi"&gt;&lt;/script&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;script type='text/javascript'&gt;
            var channel = new goog.appengine.Channel('{{ token }}');
            var socket = channel.open();

            socket.onopen = function() {
                alert("Channel connected!");
            }
            socket.onmessage = function(evt) {
                data = JSON.parse(evt.data);
                alert(data.reply_message);
            }

            function sendMsg(){
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/msg?client_id={{ client_id }}&amp;name=Dedy', true);
                xhr.send();
            }
        &lt;/script&gt;
        &lt;input type='button' value='Send my name to server' onclick='sendMsg()' /&gt;
    &lt;/body&gt;
&lt;/html&gt;


Di dalam file html ini, ada beberapa bagian yang menghandle Channel API. Pertama tentu saja kita harus meng-include library JS untuk channel API, ini dilakukan di baris ke-4. Kemudian di baris ke-8, kita mulai membuka channel dengan nilai token yang sudah di pass dari server (lihat MainPage handler di file python). Koneksi dibuka di baris ke -9. Kemudian di baris ke-11. Kita membuat sebuah event listener, yang mana akan di trigger ketika koneksi berhasil dibuka. Responnya adalah sebuah simpel alert.

Kemudian di baris 14, kita pasang event listener yang akan di-trigger ketika client mendapatkan message dari server. Di sini yang pertama kali kita lakukan adalah parsing data yang dikirim oleh server dengan fungsi
<strong>
 JSON.parse()
</strong>
. Kemudian kita akan tampilkan pesan yang isinya adalah 'reply_message', variabel ini sudah kita definisikan di handler MessageReceived pada file python tadi.

Dua listener sudah dibuat, sekarang kita buat fungsi
<strong>
 sendMsg()
</strong>
yang akan mengirim pesan ke server, isi pesan tersebut adalah channel_id milik kita (yang juga sudah di pass dari server melalui Mainpage handler), dan nama kita (karena alasan kesederhanaan code, jadi dibuat konstan '
<strong>
 Dedy
</strong>
'). Dua data ini akan dikirimkan ke server dan akan di handle oleh MessageReceived.

Baris selanjutnya adalah memasukan button untuk mentrigger fungsi sendMsg(). And that's it. Jalankan aplikasi ini di server lokal, ketika kita membukanya, maka akan muncul pesan "Channel connected!", kemudian ketika kita klik tombol yang tersedia, maka pesan berisi client_id dan nama akan terkirim, beberapa detik kemudian server akan membalas dengan pesan 'Hallo, Dedy!'.
<strong>
 Sekarang Apa?
</strong>
Kita sudah menyelesaikan satu implementasi sederhana dari Channel API, sekarang saatnya melakukan sedikit eksperimen. Coba buka aplikasi ini di beberapa browser atau tab yang berbeda, bisa 3 atau 5 tab. Lalu tekan tombol untuk mengirim pesan ke server. Pesan balasan mungkin tidak akan kita dapatkan di browser yang sama. Contoh jika saya menekan tombol di browser ke 3, pesan balasan dari server mungkin muncul di server ke 4. Kenapa bisa demikian?.

Channel API adalah salah satu implementasi dari konsep
<a href="http://en.wikipedia.org/wiki/Comet_(programming)">
 Comet
</a>
. Secara singkat, Comet adalah model aplikasi web yang secara frequent melakukan pushing data ke server tanpa partisipasi langsung dari user. Sebagai gambaran kasar, Channel API disisi client bisa melakukan Ajax Request (atau teknik lainnya) untuk mengirim data ke server secara berkali-kali dalam rentan waktu yang teratur (mungkin 2-3 detik sekali). Dari sini client bisa mengetahui apakah ada reply terbaru yang ditujukan untuknya, jika ya, maka reply akan di download, jika tidak, maka client tidak akan melakukan apa-apa. Konsep ini sama dengan konsep polling yang sempat kita bahas di Part 1, dengan salah satu pengecualian, yaitu jenis reply bisa variatif dan mekanisme polling yang dilakukan Channel API sangat kompleks untuk memberikan banyak keuntungan (performance, resource, dll)

Kembali ke masalah tadi, kenapa pesan yang diterima dari server muncul di tab ke-4 sedangkan tombol yang diklik berasal dari tab ke-3?. Alasannya ada 2 yaitu:
<ol>
 <li>
  Nama semua channel sama
 </li>
 <li>
  Perbedaan waktu trigger pada 5 tab yang dibuka
 </li>
</ol>
Alasan pertama membuka jawaban dari kemungkinan masalah yang akan terjadi jika kita menggunakan nama channel yang konstan (lihat paragraf ke 2). Ketika menggunakan nama channel yang sama, maka client kita hanya akan dianggap 1, meskipun sebenarnya yang dibuka adalah 5.

Alasan kedua, datang dari penjelasan singkat Channel API dan Comet tadi. Kita tahu bahwa polling yang dilakukan Channel API ditrigger tiap 2-3 detik. Ketika server membalas pesan, siapa yang akan menerima pesan ini akan tergantung dari secepat apa mereka melakukan polling. Dalam hal ini, dari semua tab, tab ke-4 adalah tab yang paling cepat melakukan polling setelah server mengirimkan pesan, sehingga tab ke-4 lah yang menerima balasan tersebut dan menampilkannya di browser. Inilah yang terjadi ketika kita menggunakan satu channel bersamaan.
<strong>
 Channel Eksklusif
</strong>
Solusinya adalah, membuat setiap channel menjadi ekslusif. Saya sempat tuliskan poin ini di Part 1. Bahwa meskipun usernya sama, tapi ketika dia membuka 5 tab bersamaan, 5 tab ini harus punya channel yang eksklusif, agar setiap pesan yang terkirim dan yang dibalas tidak 'nyasar' ke tempat lain.

Cara membuat channel yang ekslusif sangat simpel, kita tinggal memberi nama yang
<strong>
 unik
</strong>
di tiap channel, untuk memastikan bahwa tidak ada nama channel yang sama. Ini bisa dilakukan dengan berbagai macam cara. Kalau di aplikasi chat, kita mungkin bisa pakai username sebagai nama channel. Di kasus ini, kita akan pakai time signature, yang cukup bisa diandalkan untuk membuat nama channel yang unik.

Di setiap channel yang kita buat, kita akan tambah waktu pembuatan channel tersebut, ketika client membuat channel baru, kecil kemungkinan waktu pembuatannya sama. Lihat listing dibawah:

	:::txt
import datetime

# Handler Utama
class MainPage(webapp.RequestHandler):
    def get(self):
        client_id = "mychannel" + str(datetime.datetime.now()) # Nama Channel
        token = channel.create_channel(client_id) # Buat channel dan ambil tokennya
        # Kirim client_id dan channel ke output
        output = template.render('index.html', {'token' : token, 'client_id' : client_id})
        self.response.out.write(output)


Pertama kita import library '
<strong>
 datetime
</strong>
' untuk mengambil fungsi
<strong>
 now()
</strong>
, lalu dibagian inisialisasi client_id, kita tambahkan nama client dengan waktu pembuatan menggunakan fungsi
<strong>
 now()
</strong>
yang diubah jadi string dengan fungsi
<strong>
 str()
</strong>
. Dengan menambahkan fragment ini, kita bisa mendapatkan nama channel yang sangat unik, karena output waktu yang diberikan oleh fungsi now() mencakup hingga ke milli/micro second.

Sekarang buka lagi aplikasi kita dengan 5 (atau lebih) tab, tombol manapun yang kita klik, responnya akan konsisten di browser yang relevan. Ini karena tidak ada nama channel yang sama.

And that was it. Kita udah belajar tentang konsep dasar Channel API, bagaimana membuat koneksi, event listener, dan event handlernya, serta beberapa aturan penting seperti nama channel dan format reply (JSON).

Namun, sampai saat ini kita hanya bisa mengirim pesan ke satu client saja, bagaimana jika saya ingin mengirim pesan ke semua client atau lebih dari 1 client?. Hingga saat ini Channel API belum menyediakan fitur untuk mengirimkan pesan ke multiple channel, jadi kita harus membuatnya sendiri. Di part selanjutnya akan kita bahas tentang solusi dari masalah ini, yaitu broadcast messaging. Stay tuned :D

Untuk yang ingin mencoba source codenya, download file aplikasinya di
<a href="https://github.com/kecebongsoft/ChannelAPI_Simple">
 github ini
</a>
.
