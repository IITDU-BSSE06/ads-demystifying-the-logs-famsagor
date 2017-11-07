#!/usr/bin/python

import sys

maximum=0
totalSales = 0
oldKey = None
pathName=""
fileName=""


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, fullPath = data_mapped

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", totalSales
        oldKey = thisKey;
        if totalSales > maximum:
            maximum=totalSales
            fileName=thisKey
            pathName=fullPath
        totalSales = 0

    oldKey = thisKey
    totalSales += 1

print fileName+'\t'+ pathName
