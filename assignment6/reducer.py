#!/usr/bin/python

import sys

totalHitOf2009 = 0
totalHitOf2010 = 0
totalHitOf2011 = 0

for line in sys.stdin:

	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	ip, rest = data_mapped
	 if string.find(rest, "2009") == 1
		totalHitOf2009 = totalHitOf2009 + 1
	else if string.find(rest, "2010") == 1
		totalHitOf2010 = totalHitOf2010 + 1
	else if string.find(rest, "2011") == 1
		totalHitOf2011 = totalHitOf2011 + 1
	
print str("2009	"+totalHitOf2009)
print str("2010	"+totalHitOf2010)
print str("2011	"+totalHitOf2011)
