

#sys.argv[1]で指定されたURLから必要なファイル(画像とかmp3とか)をダウンロードしつつ、任意のURLに遷移してまたダウンロードを行うコードです
#うまくnext_url_stringやpicture_url_stringし指定することで汎用的に使えると重います。
import sys, re, urllib, urllib2, time

url = urllib2.urlopen(sys.argv[1]).read()
time.sleep(20.0)
for i in range(1,153):
	j = i + 1
	next_url_string = '<span>152</span></div>.+?href="(.+?96196-%s)' % j
	next_url_pattern = re.compile(next_url_string)
	next_url_match = next_url_pattern.search(url)
	picture_url_string = '\.jpg.+?http.+?http.+?(http.+?\.jpg)'
	picture_url_pattern = re.compile(picture_url_string)
	picture_url_match = picture_url_pattern.search(url)

	if picture_url_match != None:
		jpg_string = ".../picture_file/%s.jpg" % i
		urllib.urlretrieve(picture_url_match.group(1), jpg_string)
		time.sleep(20.0)
	else:
		print "picture not match"

	if next_url_match != None:
		url = urllib2.urlopen(next_url_match.group(1)).read()
		time.sleep(20.0)
	else:
		print "url not match"