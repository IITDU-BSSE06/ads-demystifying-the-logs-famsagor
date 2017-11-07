#!/usr/bin/python

import sys

maximum=0
totalSales = 0
oldKey = None
pathName=""
fileName=""



for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(mapped_data) != 2:
        continue

    thisKey, fullPath = mapped_data

    if oldKey and oldKey != thisKey:
        oldKey = thisKey;
        if totalSales > maximum:
            maximum=totalSales
            fileName=thisKey
            pathName=fullPath
        totalSales = 0

    oldKey = thisKey
    totalSales += 1

print str(maximum)
