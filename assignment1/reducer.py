#!/usr/bin/python

import sys

total = 0

for line in sys.stdin:

	mapped_data = line.strip().split("\t")
	if len(mapped_data) != 2:
		continue
	ipAddress, rest = mapped_data
	if ipAddress =='10.99.99.186':
		total=total+1
print str(total)
