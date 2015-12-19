

## sample data
import re

x = open('regex_sum_42.txt', 'r') 
count=0
for line in x:
	line = line.rstrip()
	y = re.findall('[0-9]+', line)
	for item in y:
		item = int(item)
		count = count + item	

print count #597873

## actual data
import re

x = open('regex_sum_201060.txt', 'r') 
count=0
for line in x:
	line = line.rstrip()
	y = re.findall('[0-9]+', line)
	for item in y:
		item = int(item)
		count = count + item

print count	#311623
