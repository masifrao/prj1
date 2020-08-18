#!/bin/python
import socket

socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("10.200.100.11",80))
    print s.recv(1024)
except Exception, e:
    print "[ - ] Error = " + str(e)

