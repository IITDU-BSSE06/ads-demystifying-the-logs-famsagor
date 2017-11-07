#!/usr/bin/python
import urlparse

import sys

for line in sys.stdin:
	dataSet = line.strip().split(" ")
	if len(dataSet) == 10:
		l0, l1 ,l2 ,l3 ,l4 ,l5 ,l6 ,l7 ,l8 ,l9= dataSet
		path = urlparse.urlparse(l6).path

		print "{0}\t{1}".format(l6,l6)
