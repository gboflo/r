#!/usr/bin/python
import sys
import time

duration = 10

print "[{}]: '{}' sleeping for {} seconds ...".format(time.ctime(), sys.argv[0], duration)
time.sleep( duration )
print "[{}]: '{}' done sleeping for {} seconds".format(time.ctime(), sys.argv[0], duration)
