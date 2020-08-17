#!/bin/python
import socket
import os
import sys

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except Exception, e:
        print '[-] Error: ' + str(e) + ' for ' + str(ip) + ': ' + str(port)
#################VULN Checks#############################################    
def checkvuln(banner):
    f = open("/root/vuln_banner.txt",'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+} Server is Vulnerable: "+banner.strip('\n')
########################################################################
def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print '[-] ' + filename + ' does not exist.'
            exit(0)
        if not os.access(filename, os.R_OK):
            print '[-] ' + filename + ' access denied.'
            exit(0)
    else:
        print '[+] Usage: ' + str(sys.argv[0]) + \
        ' (vuln filename)'
        exit(0)
        portlist = [21,22,23,80,110,443]
        for x in range(1,254):
            ip = '10.200.110.'+str(x)
            for port in portlist:
                banner = retBanner(ip,port)
                if banner:
                    print '[+} '+ ip + ': ' + banner
                    checkvuln(banner, filename)
if __name__ == '__main__':
    main()


