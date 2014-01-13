ack -o 'http://[./a-zA-Z0-9_]*.jpg*' wordpress.xml | cat >> wordpress_media_urls.txt
ack -o 'http://[./a-zA-Z0-9_]*.jpeg*' wordpress.xml | cat >> wordpress_media_urls.txt
ack -o 'http://[./a-zA-Z0-9_]*.gif*' wordpress.xml | cat >> wordpress_media_urls.txt
ack -o 'http://[./a-zA-Z0-9_]*.png*' wordpress.xml | cat >> wordpress_media_urls.txt
python wordpress_download_media.py
