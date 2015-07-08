title: Google Account Switcher
date: 06-01-2014
tags: komputer

Saya sudah bertahun-tahun menggunakan email, bagi saya email adalah salah satu medium paling efektif untuk berkomunikasi. Sudah berbagai macam layanan email yang saya gunakan. Saya masih ingat email pertama saya ada di plasa.com, Yahoo!-nya indonesia di tahun 2000an dulu. Kemudian berpindah ke Yahoo!, Hotmail, dan banyak lagi, sampai akhirnya berhenti di Gmail.

Gmail bagi saya (dan banyak orang) adalah salah satu layanan email terbaik saat ini, dan untung saja kantor saya juga menggunakan Google Apps sehingga saya bisa menggunakan fitur multiple accounts-nya Google. Fitur ini memungkinkan kita untuk punya beberapa account Google dan berpindah account tanpa harus log-out.

Kantor saya menggunakan berbagai macam layanan Google selain GMail, dan account switcher ini terasa sekali manfaatnya karna saya bisa melihat inbox personal dan kantor tanpa harus menggunakan browser/session berbeda. Masalahnya adalah tidak semua layanan Google menyediakan fitur ini (secara jelas). 

Contohnya adalah Google Sites, tempat dimana kita bisa membuat halaman statik web. Ketika ingin memanage sebuah Site atas account yg lain, saya dihadapkan dengan sebuah login form yang pada dasarnya menyuruh saya logout.

Ternyata ada trik sederhana melakukan switch account disini tanpa harus logout. Pertama, di Gmail, URL yang ditampilkan memiliki `/u/0/` di satu account, dan memiliki `/u/1/` di account lainnya, yang kedua, di login url sites.google.com ada parameter  `authuser` yang sama dengan pola tersebut, kita hanya perlu menggantinya dari `0` ke `1`, maka halaman akan redirect ke  account yang sesuai..
