#!/bin/python
# -*- coding: utf-8 -*-
import crypt
def testpass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptword = crypt.crypt(word, salt)
        if (cryptword == cryptPass):
            print '[+] Found Password: ' + word + "\n"
            return
    print '[-] Password not found: '
    return
def main():
    passfile = open('password.txt')
    for line in passfile.readlines():
        if ":" in line:
            user =line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[*] Cracking Password for: "+user
            testpass(cryptPass)
if __name__ == "__main__":
    main()
