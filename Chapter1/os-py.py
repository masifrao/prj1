#!/bin/python

import sys
import os

####################Handling with OS######################
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print '[-] ' + filename + ' does not exist.'
        exit(0)
    if not os.access(filename, os.R_OK):
        print '[-] ' + filename + ' access denied.'
        exit(0)
    print '[+] Reading Vulnerabilities From: ' + filename
    f = open(filename, 'r')
    for line in f.readlines():
        print line.strip('\n')
