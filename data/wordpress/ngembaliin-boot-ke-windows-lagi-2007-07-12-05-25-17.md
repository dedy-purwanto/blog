title:Ngembaliin boot ke windows lagi
date:2007-07-12 05:25:17
status:draft


<p class="main">Kemarin sempat nginstall Ubuntu 5.04, trus niatnya pengen di uninstal. Ya udah deh nekat aja pake PowerQuest PartitionMagic, delete &amp; secure erase partisi linuxnya, trus di reboot, eh baru ingat GRUB Boot Loadednya ada di MBR (Master Boot Record) dan masih di konfigurasi buat ngakses ke partisi linux!, jadi nongol error deh (soalnya partisi linuxnya udah kehapus T_T). Jadi bingung deh, dikira langsung otomatis balik booting ke windows. Masa mesti nginstall windows lagi?, padahal udah banyak plugin-plugin yang ku install (yang pasti bakal ilang klo windowsnya di reinstall).</p>
Ah, gak boleh reinstall windows, repot!. Coba buka-buka command line yang disediain boot CD-nya windows xp, gak taunya ada command <strong>FIXMBR</strong>, yang bisa ngefix master boot record yang invalid, hehehe, setelah pake command line itu, os-nya om bill gates ini akhirnya bisa nongol lagi :D.