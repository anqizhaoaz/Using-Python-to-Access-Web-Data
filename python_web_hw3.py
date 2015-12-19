
# https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

while count>0:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	# Retrieve all of the anchor tags
	tags = soup('a')
	
	print "Retrieving: " + url

	list=[]
	for tag in tags:
		#print tag.get('href', None)
		list.append(tag.get('href', None))

	url = list[position-1]
	count-=1

print "Last Url: " + url

