#!/usr/bin/python

import sys

for line in sys.stdin:
    dataSet = line.strip().split("]")
    if (len(dataSet) >1):
        hitIPData = data[0]
print hitIPData 
