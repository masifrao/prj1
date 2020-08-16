#!/bin/python
import socket

##############Read Function##########################
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except Exception, e:
        #xxreturn
        print "[-] Error: " + str(e) + " for " + str(ip)
####################
def checkvuln(banner):
    f = open("/root/vuln_banner.txt",'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+} Server is Vulnerable: "+banner.strip('\n')

#    if 'Ubuntu-4ubuntu' in banner:
#        print '[+] SSH server is Vulnerable: '
####################
def main():
    ip1 = '10.200.100.11'
    port1 = 22
    ip2 = '10.200.101.11'
    portlist = [21,22,23,80,443]
    for x in range(1,4):
        ip = '10.200.100.'+str(x)
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print '[+] ' + ip + ': '+ str(port) + banner
                checkvuln(banner)

    #banner1 = retBanner(ip1, port1)
    #if banner1:
    #    print '[+] ' + ip1 + ': ' + banner1
    #    checkvuln(banner1) 
    #banner2 = retBanner(ip2, port1)

    #if banner2:
    #    print '[+] ' + ip2 + ': ' + banner2
    #    checkvuln(banner2)
if __name__ == '__main__':
    main()
