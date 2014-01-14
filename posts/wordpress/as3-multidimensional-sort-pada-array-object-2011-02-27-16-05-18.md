title:AS3: Multidimensional Sort pada Array Object.
date:2011-02-27 16:05:18
status:draft

Terkadang ada kondisi dimana kita mempunyai sebuah array yang isinya object, lalu kita ingin melakukan sorting array tersebut, yang parameternya adalah member object didalam array.

Contoh, jika saya punya object ini:

[sourcecode language="java"]
public class Murid
{
	public var nama:String;
	public var kelas:int;
	public var nilai:int;
	public function Murid(nNama:String,nKelas:String,nNilai:String)
	{
		nama = nNama;
		kelas = nKelas;
		nilai = nNilai;
	}
}
[/sourcecode]

<!--more-->

Kemudian, saya punya vector Murid seperti ini:

[sourcecode language="java"]
vecMurid = new Vector.&amp;lt;Murid&amp;gt;();
vecMurid.push(new Murid(3, 6, &amp;quot;Tio&amp;quot;));
vecMurid.push(new Murid(1, 5, &amp;quot;Andi&amp;quot;));
vecMurid.push(new Murid(2, 8, &amp;quot;Lina&amp;quot;));
vecMurid.push(new Murid(1, 10, &amp;quot;Dedi&amp;quot;));
vecMurid.push(new Murid(2, 7, &amp;quot;Melisa&amp;quot;));
[/sourcecode]

Sekarang, saya ingin mengurutkan daftar murid ini, mulai dari <strong>kelasnya yang terkecil</strong>, kemudian <strong>niainya yang terbesar</strong>, ini adalah output yang saya inginkan:
<blockquote>Kelas 1, Nilai 10, Dedi
Kelas 1, Nilai 5, Andi
Kelas 2, Nilai 8, Melisa
Kelas 2, Nilai 7, Lina
Kelas 3, Nilai 6, Tio</blockquote>
Inilah yang disebut multidimensional sort pada array yang berisikan object. Di ActionScript 3, kita bisa melakukan sorting ini dengan sangat mudah. <a href="http://livedocs.adobe.com/flash/9.0/ActionScriptLangRefV3/Array.html#sortOn()">AS3 memperkenalkan fungsi sortOn</a> yang parameternya bisa kita custom sedemikian rupa untuk melakukan pengurutan yang kompleks, sintaks generalnya adalah:

[sourcecode language="java"]
array.sortOn('names','options');
[/sourcecode]

Fungsi ini memungkinkan kita untuk mengurutkan sebuah array dengan berbagai parameter dan opsi. Misalkan saya ingin mengurutkan murid berdasarkan '<strong>kelas</strong>' dan '<strong>nilai</strong>', saya bisa memasukan ini:

[sourcecode language="java"]
sortOn(['kelas','nilai'],Array.DESCENDING);
[/sourcecode]

Parameter pertama diatas adalah daftar keys yang akan digunakan untuk melakukan sorting, sementara parameter kedua adalah mode sorting. Tapi, kode diatas tidak akan bekerja, karena variabel <strong>vecMurid</strong> yang kita pakai adalah <strong>vector</strong>, dan isinya bukan <strong>array set</strong>. Jadi untuk kasus ini, kita akan ubah sedikit fungsi sortingnya seperti ini:

[sourcecode language="java"]
public function sortMurid(vec:Vector.&amp;lt;Murid&amp;gt;):Vector.&amp;lt;Murid&amp;gt; {
	var arr:Array = new Array();
	var i:int;

	for (i = 0; i &amp;lt; vec.length; i++) {
		arr.push({kelas:vec[i].kelas,nilai:vec[i].nilai,o:vec[i]});
	}

	arr = arr.sortOn(['kelas','nilai'], [Array.NUMERIC, Array.NUMERIC | Array.DESCENDING]);

	var vec_output:Vector. = new Vector.();
	for (i = 0; i &amp;lt; arr_h.length; i++) {
		vec_output.push(arr['i']['o']);
	}
	return vec_output;
}
[/sourcecode]

Pada kode diatas, kita membuat fungsi yang returnnya adalah vector Murid, dan parameternya adalah vector Murid yang telah kita buat sebelumnya. Pertama-tama kita akan menyalin semua isi dari parameter pertama kedalam sebuah array, tapi tidak hanya sekedar menyalin, kita juga menambahkan 2 buah key yaitu '<strong>kelas</strong>' dan '<strong>nilai</strong>' kedalam array tersebut. Sehingga setiap membernya adalah sebuah set yang isinya '<strong>kelas</strong>', '<strong>nilai</strong>', dan '<strong>o</strong>', yaitu reference ke instance yang ada di setiap vector Murid.

Setelah itu, kita bisa langsung melakukan sorting dengan fungsi <strong>sortOn</strong>, parameter pertama adalah key set yang kita perlukan, yaitu '<strong>kelas</strong>' dan '<strong>nilai</strong>'. Parameter kedua adalah dua buah set opsi yang kita gunakan untuk melakukan sorting. Opsi pertama adalah '<em>Array.NUMERIC</em>', yang artinya key '<strong>kelas</strong>' adalah set numeric yang di set secara <em>Ascending</em>. Opsi kedua adalah '<em>Array.NUMERIC | Array.DESCENDING</em>', yang artinya key '<strong>nilai</strong>' adalah set numeric yang harus di urut secara <em>DESCENDING </em>(yang terbesar akan  muncul lebih dulu).

Setelah di urut, kita tinggal menyalin kembali array tersebut ke output, lalu di return ke fungsi.

And that's it :D