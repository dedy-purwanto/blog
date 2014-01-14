title:General functions in a class
date:0000-00-00 00:00:00
status:draft

 Dari dulu aku punya kebiasaan yang (mungkin) cukup aneh : semua fungsi general seperti string utility, advanced math functions, i/o functions dikapsulkan dalam sebuah kelas. Biasanya kelas ini aku beri nama CUtils. Kenapa aneh? setidaknya menurutku, aku sering melihat dan menemukan kode berisi kumpulan fungsi umum yang "telanjang", dalam artian tidak memiliki class, sehingga terlihat (agak) tidak terklasifikasi. Yang paling dekat dengan "tidak telanjang" adalah penggunaan prefix pada tiap nama fungsi.

Everyone has their own style, kenapa aku lebih suka mengkapsulkannya dalam class?. Aku sering membuat hand-made function yang memungkinkan namanya bisa bentrok dengan general function milikku. Kalau harus menggunakan prefix, aku sering membayangkan jika memiliki puluhan fungsi dan ingin mengganti prefixnya satu-persatu :roll::

Jadi? solusinya ya dengan merakit class CUtils tadi, selain itu kelebihannya juga aku bisa menyebarnya ke siapa aja yang mau pakai tanpa harus takut nama fungsi nya bentrok, atau prefixnya bentrok, sebab semuanya ada dalam kelas dan kalau bentrok tinggal ganti nama kelas.

Btw aku jadi ingat dulu pas pakai API Direct3D Extension, fungsi utility disana rata-rata pakai prefix yang mengerikan ketika di-spell, bahkan untuk yang bisa ngetik 11 jaripun harus memperhatikan casenya :D . Bayangkan jika itu diletakan didalam kelas, kita hanya perlu memberi nama instancenya dan bisa efisien ditiap kode. Tapi creatornya mungkin punya alasan tersendiri tidak memasukannya ke kelas dan hanya memberi prefix. Lagipula D3DX API tetap bisa dikapsulkan ke dalam class, cukup rakit satu kelas berisi shortcut function APInya dengan parameter dan return type yang sama, tapi sama yang mau bikin?. Lagian kok malah ngelantur kesini ya.. hehe..

Ada yang suka main kapsul-kapsulan juga?. Kebiasaan aneh nggak ya :D