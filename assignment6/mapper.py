#!/usr/bin/python


import sys

for line in sys.stdin:
	dataSet = line.strip().split(" - - ")
	if len(dataSet) == 2:
		ip, rest = dataSet
print "{0}\t{1}".format(ip, rest)
