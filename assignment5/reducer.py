#!/usr/bin/python

import sys

numberOfUniqueFiles=0
oldKey = None

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(mapped_data) != 2:
        continue

    thisKey, fullPath = mapped_data

    if oldKey and oldKey != thisKey:
        numberOfUniqueFiles= numberOfUniqueFiles + 1
        oldKey = thisKey;
        salesTotal = 0
    oldKey = thisKey

print str(numberOfUniqueFiles)
