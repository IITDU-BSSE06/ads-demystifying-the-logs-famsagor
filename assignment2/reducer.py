#!/usr/bin/python

import sys

total = 0

for line in sys.stdin:
	mapped_data = line.strip().split("\t")
	if len(mapped_data) != 2:
		continue
	ip, rest = mapped_data
	if '/assets/js/the-associates.js' in rest:
		total=total+1

print str(total)
