#!/bin/bash
f = open('/root/vuln_banner.txt' , 'r')
for line in f.readlines():
    print  line.strip('\n')
