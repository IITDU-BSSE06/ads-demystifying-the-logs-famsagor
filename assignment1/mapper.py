usr/bin/python


import sys

for line in sys.stdin:
	dataSet = line.strip().split(" - - ")
	if len(dataSet) == 2:
		ipAddress, rest = dataSet
		print "{0}\t{1}".format(ipAddress, rest)
