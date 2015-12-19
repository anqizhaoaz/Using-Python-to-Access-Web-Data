
## sample execution: JSON

# $ python solution.py 
# Enter location: http://python-data.dr-chuck.net/comments_42.json
# Retrieving http://python-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2482

# cd desktop/machine/webpython
# python python_web_hw5.py

import urllib
import json

while True:
  url = raw_input('Enter location: ')
  if len(url) < 1 : break
  print 'Retrieving', url
  #read url link

  uh = urllib.urlopen(url)
  data = uh.read()
  #open url
  print 'Retrieved',len(data),'characters'

  try:
    js = json.loads(data) #parsing values from JSON
    print 'User count: ', len(js)

  except:
    js = None

  count=0
  sum=0
  for item in js["comments"]:
      sum+=(item["count"])
      count+=1
  print "Count: " + str(count)
  print "Sum: " + str(sum)

