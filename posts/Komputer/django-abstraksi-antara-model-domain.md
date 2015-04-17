title: Django: Abstraksi model dan domain
date: 2015/04/17

> _"Web framework for perfectionsist with deadline"_ adalah slogan dari Django, web framework berbasis Python. Slogan ini biasanya benar; sangat mudah dan cepat membuat website dengan Django, tapi belakangan ini saya merasa, seringkali ketika websitenya mulai kompleks, mulai rumit untuk menambahkan atau mengubah kode yang menggunakan Django atau framework pada umumnya

Saya mulai kenal dan menggunakan Django sejak 2011. Berangkat dari PHP, Python dan Django benar-benar membuat saya _enjoy_ sebagai programmer, sintaks yang simpel serta mudahnya berinteraksi dengan database memungkinkan saya untuk membuat website dengan cepat dan mudah. Contohnya seperti:

    #!python
    class Comment(models.Model):
        name = models.CharField(max_length=255)
        comment = models.TextField()
        posted = models.DateTimeField(auto_now_add=True)
    
    class CommentForm(forms.Model):
        class Meta:
            model = Comment

    class CommentListView(ListView):
        model = Comment
            
    {% for comment in comments %}
        {{ comment.name|truncatewords:"3" }}
        {{ comment.comment }}
        {{ comment.posted|date:"d m Y" }}
    {% endfor %}

Kode diatas adalah contoh deklarasi tabel (model), form, view dan template rendering di Django. Mudah dan simpel. Jika digabungkan dengan Django admin, maka kita bisa membuat sebuah website dengan sangat cepat. Membuat berbagai macam tabel dan halaman dalam sehari. Kita juga bisa melakukan query seperti ini di Django:

    #!python
    Comment.objects.filter(name='dedi')
    Comment.objects.filter(name__contains='edi')
    Comment.objects.filter(posted__gte=datetime(2014, 1, 1))
    
Contoh query diatas bisa kita gunakan di view Django untuk melakukan filtering sesuai dengan logika bisnis, misaklan ada fitru untuk mencari komentar berdasarkan nama pengirim, atau berdasarkan tanggal.

Semua lancar dan mudah, sampai ketika website kita mulai menjadi semakin besar dengan fitur yang bermacam-macam, contohnya saja, ketika kita menambahkan fitur moderasi, sehingga tabel Comment punya satu field baru:

    #!python
    class Comment(...):
        ....
        moderated = models.BooleanField(default=False)
        
Dampaknya adalah, semua kode kita yang melakukan query ke tabel Comment harus menambahkan parameter `moderated=True` agar hanya komentar yang sudah dimoderasi yang ditampilkan. Jika kita memiliki 10 views dan template yang mengakses model Comment, maka kita harus menggantinya di 10 tempat tersebut.

Anggaplah beberapa bulan kemudian kita menambahkan satu fitur lagi, yaitu mengurutkan komentar berdasarkan jumlah like:

    #!python
    class Comment(...):
        ...
        likes = models.IntegerField(default=0)
        
Sekarang kita harus mengganti semua kode yang menggunakan Comment agar melakukan `order_by('likes')`. Bagaimana jika kita ingin agar bisa menyembunyikan komentar tertentu?

    #!python
    class Comment(...):
        ...
        hidden = models.BooleanField(default=False)
        
Dan lagi-lagi kita harus mengganti semua kode kita yang menggunakan Comment. Tapi tak masalah, karena yang membuat website adalah kita sendiri, maka semua perubahan ini sangat mudah dilakukan, karena kita tahu persis logika, alur serta struktur datanya. Jadi cukup ubah file yang bersangkutan satu persatu, dan masalah selesai.

Lalu bagaimana jika kita sedang membangun banyak website secara bersamaan? apakah masih bisa ingat karakter _codebase_ setiap website secara persis?

Lalu bagaimana jika ada orang baru yang membatu kita mengembangkan _codebase_-nya? Ketika dia membuat fitur atau perubahan baru di sebuah halaman komentar, apakah dia tahu bahwa ada _field_ `moderated`, `hidden` dan `likes` yang harus digunakan untuk setiap query?.

Lalu bagaimana jika kita mengganti nama field dari `moderated` ke `_is_moderated`? Juga ketika kita sudah tidak menyentuh kode nya selama berbulan-bulan, apakah akan masih ingat semua _constraint_ ini?

Inilah masalah yang seringkali ditemukan di _codebase_ Django yang skalanya _mid-size_, karena dibuai oleh berbagai komponen dan library yang disediakan, kita seringkali langsung menggunakannya tanpa berfikir bagaimana nantinya _codebase_ kita akan berevolusi. 

Belakangan ini saya sedang mencari cara untuk mengurangi resiko seperti diatas dengan cara membuat abstraksi antara database dan domain yang sedang dikerjakan, di contoh diatas domainnya adalah website yang menampilkan komentar. Ada dua materi menarik yang saya temukan sejauh ini, dimana saya sedang mencoba menggabungkan keduanya dan melihat apakah cocok untuk digunakan sebagai salah satu pola mengembangkan _codebase_ Django yang sekiranya akan kita seriusi. Pertama adalah [Higher level query API](http://www.dabapps.com/blog/higher-level-query-api-django-orm/) dan yang kedua adalah [The end of MVC](https://www.youtube.com/watch?v=yvjmAYmYOj0) oleh Alex Gaynor.

Semoga setelah mencoba kedua metode ini, saya bisa menuliskan hasilnya disini dan bisa digunakan untuk memperbaiki cara saya menggunakan web framework pada umumnya.
