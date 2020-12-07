#!/usr/bin/python
import sys
import time

if len(sys.argv) != 2:
    print("Usage: %s <duration in seconds>" % sys.argv[0])
    exit(1)
duration = float(sys.argv[1])


time.sleep(duration)
print(duration)
