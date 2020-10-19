#!/usr/bin/python
import sys
import time

duration = 7
print("gimi")

print "[{}]: '{}' sleeping for {} seconds ...".format(time.ctime(), sys.argv[0], duration)
time.sleep( duration )
print "[{}]: '{}' done sleeping for {} seconds".format(time.ctime(), sys.argv[0], duration)
