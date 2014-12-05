title:Cara posting source code di Wordpress
date:2007-09-16 07:10:37

Yang pakai wordpress.com dan sering posting source code, pasti kesulitan karena nggak seperti
<abbr title="Content Management System">
 CMS
</abbr>
Wordpress yang bisa ditambahin plugin untuk nampilin source code terformat. Mesti encode tag-tag, bikin line numbers, dan yang paling mengerikan mungkin bikin
<abbr title="Pewarnaan sintaks berdasarkan tipenya">
 sintaks highlighting!
</abbr>
. Tapi sebenernya ada cara mudah kok
<!--more-->
, contoh untuk nampilin source kode
<abbr title="Pretext Hyper Processor">
 PHP
</abbr>
seperti ini :
	:::txt
$nama="Dedi Purwanto";
echo "Selamat datang, $nama";

caranya :
<blockquote>
 <strong>
  	:::txt
 </strong>
 <strong>
  $nama="Dedi Purwanto";
 </strong>
 <strong>
  echo "Selamat datang, $nama";
 </strong>
 <strong>
  
 </strong>
</blockquote>
Untuk sintaks highlighting yang lainnya, cukup ganti atribut language dengan sintaks yang diinginkan, berikut adalah sintaks highlighting yang didukung wordpress.com :
<ul>
 <li>
  cpp
 </li>
 <li>
  csharp
 </li>
 <li>
  css
 </li>
 <li>
  delphi
 </li>
 <li>
  java
 </li>
 <li>
  jscript
 </li>
 <li>
  php
 </li>
 <li>
  python
 </li>
 <li>
  ruby
 </li>
 <li>
  sql
 </li>
 <li>
  vb
 </li>
 <li>
  xml
 </li>
</ul>
Nggak perlu convert tag menjadi HTML Entities, karena kode diatas secara otomatis akan mengubah tag-tag kita menjadi html entities. Sebagai catatan, jangan copy paste sintaks diatas karena tanda single quotenya adalah special character.
