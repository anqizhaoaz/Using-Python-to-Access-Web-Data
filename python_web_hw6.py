
## calling a JSON API

# The program will prompt for a location, contact a web service 
# and retrieve JSON for the web service and parse that data, 
# and retrieve the first place_id from the JSON. 
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.


## test data/sample execution

# cd desktop/machine/webpython
# python python_web_hw6.py
# Enter location: South Federal University 
# Retrieving http://...
# Retrieved 2101 characters
# Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok 

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        #print '==== Failure To Retrieve ===='
        #print data
        continue

    #print json.dumps(js, indent=4)

    #lat = js["results"][0]["geometry"]["location"]["lat"]
    #lng = js["results"][0]["geometry"]["location"]["lng"]
    #print 'lat',lat,'lng',lng
    id = js['results'][0]['place_id']
    print "Place id " + str(id)
