#!/usr/bin/python

import sys

totalNumberOfGET = 0

for line in sys.stdin:

	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	ip, rest = data_mapped
	 if string.find(rest, "GET") == 1
		totalNumberOfGET = totalNumberOfGET + 1
	
print str(t"GET	"+totalNumberOfGET)
