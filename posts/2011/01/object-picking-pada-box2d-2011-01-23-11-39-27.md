title:Object picking pada Box2D
date:2011-01-23 11:39:27

Beberapa minggu lalu saya sempat membuat fungsi sendiri untuk mouse picking di Box2D. Singkatnya, saya punya beberapa object di Box2D yang akan mentrigger respon berbeda ketika diklik oleh mouse. Kasus utamanya bukan tentang repson yang berbeda, tapi bagaimana caranya bisa mendapatkan posisi mouse di Box2D, sedangkan satuan yang digunakan berbeda, yaitu pixel (untuk stage), dan meter (untuk box2D). Di demo Box2D ada contoh mekanisme Mouse-picking. Yaitu dengan membuat sebuah object box2D super kecil yang kemudian akan diset auto drag, lalu sisanya hanya tinggal mentrigger pengecekan koordinat object tersebut didalam event MouseDown().

Rasanya solusi diatas terlalu repot, jadi saya buat solusi singkat aja, yaitu dengan melakukan konversi satuan dari pixel ke meter. Lihat kode dibawah:

	:::txt
public function b2Val(val:Number):Number {return val / UNIT_SCALE;}
public function mcGameDebug_Click(e:MouseEvent):void {
var mx:int = e.stageX -  mcGameDebug.x;
var my:int = e.stageY -  mcGameDebug.y;
var hit:Boolean;
for (var i:int = 0; i &amp;lt; shapes.length; i++) {
	var bd:b2Body = ballBody;
	hit = bd.GetFixtureList().TestPoint(new b2Vec2(b2Val(mx), b2Val(my)));
	if (hit) {
		// action goes here...
		break;
	}				
}
}


Simple sekali dua fungsi diatas, pertama ada event listener yang setiap kali di trigger, akan mengambil posisi mouse yang dipengaruhi oleh mcGameDebug (stage yang kita pakai untuk render semua debug data box2D). Lalu ada boolean hit yang menentukan apakah posisi mouse bersentuhan dengan ballBody (ballBody adalah global variabel, bisa apapun sesuai kebutuhan). Lalu ada TestPoint() untuk mengecek apakah posisi mouse "mengklik" ballBody. Dan jika ya, maka tinggal kita beri action spesifik. Disana juga ada fungsi b2Val yang akan melakukan konversi dari pixel ke meter.

And that's it, nggak perlu buat place holder kecil untuk mouse seperti demo Box2D :D
