title:Alternatif fungsi Empty() padaPHP
date:2007-09-14 21:58:24

Yang sering pake php, biasanya kan kalau bikin form yang banyak field-fieldnya, begitu di submit si programmer mesti cek satu-satu dulu apakah field-field tersebut sudah terisi atau belum. Mungkin sebagian ada yang pakai fungsi
<strong>
 isset
</strong>
. Tapi bagaimana seandainya variabel tersebut sudah di set tapi belum terisi? contoh, jika dalam kondisi
<strong>
 register_globals=off
</strong>
, kita biasa menangkap variabel form dengan fungsi
<em>
 $nama=$_POST[&#8217;nama&#8217;]
</em>
dst&#8230; Sehingga pada php variabel tersebut sudah berstatus diset, namun mungkin saja belum ada isinya.

Untuk mengatasi hal itu, sebagian programmer menggunakan fungsi
<strong>
 empty()
</strong>
, tapi kekurangan fungsi empty adalah dia hanya bisa menghandel satu parameter untuk setiap pemanggilan fungsi tersebut. Sehingga jika kita punya belasan atau bahkan puluhan field yang mesti dicek kosong atau tidak, akan menghasilkan listing yang cukup panjang.

Jadi sekarang kita buat aja fungsi sendiri, yang bisa mengecek variabel itu kosong atau tidak (meskipun sudah diset). Dan fungsi ini bisa dimasukan parameter tidak terbatas. ini listingnya :
	:::txt
function empties(){
for($i=0;$i &amp;lt; func_num_args() ;$i++){
$isi=func_get_arg($i);
echo "Parameter ke-$i : $isi";
if(empty($isi)){
echo "Variabel ini kosong!";
}
}
}
//Panggil fungsi empties()
empties("Dedi","Titin","Mamah","Papah","Uncu","Ketek","","Jefri","Suanah");


Selamat mencoba :D
