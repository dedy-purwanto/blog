from bs4 import BeautifulSoup
from slugify import slugify

doc = BeautifulSoup(open('tumblr_kecebongsoft.xml', 'r'))

ENCODINGS = [ 'utf8', 'gb18030', 'ascii' 'latin1', ]
def unicode(s):
    for encoding in ENCODINGS:
        try:
            s = s.encode(encoding)
            return s
        except:
            pass
    return u"CANt encode"

for item in doc.findAll('item'):
    date = item.find("wp:post_date").text
    title = item.find("title").text
    content = item.find("content:encoded").text

    if title is None or len(title) == 0:
        title = date

    f = open('tumblr/%s.md' % slugify(title), 'w')

    title = unicode(title)
    content = unicode(content)

    f.write("title:%s\ndate:%s\nstatus:draft\n\n%s" % (unicode(title), date, unicode(content)))


