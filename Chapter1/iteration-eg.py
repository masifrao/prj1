#!/bin/python
import time
ip = '10.255.150.'
portlist = [21,22,23,25,53,80,443,8080,8081]
for x in range(1,250):
    for port in portlist:
        print "[+} Checking  10.255.150."+str(x)+": "+str(port)

   ## print ip + str(x)
  ##      time.sleep(1)
