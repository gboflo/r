#!/usr/bin/python
import sys
import time

if len(sys.argv) != 2:
    print("Usage: %s <duration in seconds>" % sys.argv[0])
    exit(1)
duration = float(sys.argv[1])

print "[{}]: '{}' sleeping for {} seconds ...".format(time.ctime(), sys.argv[0], duration)
time.sleep( duration )
print "[{}]: '{}' done sleeping for {} seconds".format(time.ctime(), sys.argv[0], duration)
