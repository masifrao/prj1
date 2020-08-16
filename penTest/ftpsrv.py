#!/bin/python
import sys
import time
port = 21
banner = 'Freefloat FTP Server'
print "[+] Checking on "+banner+" on Port " +str(port)
PortList=[21,22,23,22,80,443]
for port in PortList:
    print "checking on " +str(port)
    time.sleep(1)
