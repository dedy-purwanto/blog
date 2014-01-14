title:Konversi vektor screen ke world pada orthogonal projection 
date:2008-09-28 02:21:08
status:draft

Banyak yang bingung mencari nilai vektor (x, y) pada 3D world yang berasal dari vektor screen. Biasanya teknik ini disebut picking. Kali ini kita akan melakukan konversi vektor screen ke vektor 3D world, tapi dalam orthogonal projection, yang berarti posisi y axis kamera sama nilainya dengan posisi y axis poros kamera. Disini kita menggunakan OpenGL dan <a href="http://glfw.sourceforge.net/">GLFW </a> sebagai frameworknya.

Banyak sekali teknik picking yang sudah ada, saya nggak akan ngebahas banyak tentang matematika untuk mendapatkan nilai vektornya, karena OpenGL sendiri punya sebuah library bernama GLU, kita akan menggunakan fungsi <a href="http://www.opengl.org/documentation/specs/man_pages/hardcopy/GL/html/glu/unproject.html">gluUnProject()</a> milik GLU untuk melakukan konversi koordinat window ke koordinat objek.

[sourcecode language='cpp']
GLdouble posx,posy,posz; // variabel untuk menyimpan hasil konversi
int mx,my; // variabel untuk menyimpan koordinat mouse

// ambil koordinat mouse dengan GLFW, bisa juga menggunakan lib lain (SDL, etc)
glfwGetMousePos(&mx,&my); 

glLoadIdentity(); // reset matrix
GLdouble modelMatrix[16];
glGetDoublev(GL_MODELVIEW_MATRIX,modelMatrix);
GLdouble projMatrix[16];
glGetDoublev(GL_PROJECTION_MATRIX,projMatrix);
int viewport[4];
glGetIntegerv(GL_VIEWPORT,viewport);
gluUnProject(mx,my,0,modelMatrix,projMatrix,viewport,&posx,&posy,&posz);

posx*=(zoom * 10); // hasil konversi dikalikan dengan (zoom * 10)	
posy*=(zoom * 10);

posy*=-1; // karena arah y axis pada 3D world umumnya berbeda dengan y axis pada 2D (orthogonal), jadi kita kalikan dengan -1

std::cout << posx << ", " << posy << "\n"; // print output konversi
[/sourcecode]

Disini pertama-tama kita ambil dulu koordinat mouse, kemudian ambil setting model view matrix,projection matrix, dan viewport yang sudah di set sebelumnya, setelah itu gunakan gluUnProject untuk melakukan konversi (silahkan lihat manual gluUnProject pada website OGL).

Variabel zoom adalah distance antara posisi Z kamera dengan posisi Z poros kamera, kita kalikan dengan 10 karena nilai konversi sebelumnya adalah nilai floating point yang sangat kecil. Terakhir mengalikan posy dengan -1 untuk menormalkan posisi y axisnya sesuai dengan 3D world.

Banyak sekali implementasi teknik picking yang tersebar di internet. Teknik diatas adalah salah satu yang paling simpel :roll: . 