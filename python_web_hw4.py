
## sample execution: XML

# cd desktop/machine/webpython
# python_web_hw4.py
# Enter location: http://python-data.dr-chuck.net/comments_42.xml
# Retrieving http://python-data.dr-chuck.net/comments_42.xml
# Retrieved 4204 characters
# Count: 50
# Sum: 2482


import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break
    print 'Retrieving', url
    
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    
    tree = ET.fromstring(data) #fromstring() parses XML from a string directly into an Element

    counts = tree.findall('.//comment/count')
    count = 0
    for i in counts:
        #print int(i.text)
        count+=1
    total = sum(int(number.text) for number in counts)
    print "Count: " + str(count)    
    print "Sum: " + str(total)
