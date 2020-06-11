#coding=utf-8

import sys
import nmap

scan_row=[]
input_data = raw_input('Please input hosts and port:')
scan_row = input_data.split(" ")
if len(scan_row)!=2:
    print "Input errors,example \"127.0.0.1 80,443,22\""
    sys.exit(0)
hosts=scan_row[0]
port=scan_row[1]

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print ('Nmap not founf',sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit()

try:
    nm.scan(hosts=hosts,arguments=' -v -sS -p '+port)
except Exception,e:
    print "Scan erro:"+str(e)

for host in nm.all_hosts():
    print("------------------------------------------")
    print('Host : %s (%s)' % (host,nm[host].hostname()))
    print('State : %s' %nm[host].state())

    for proto in nm[host].all_protocols():
        print('---------------')
        print('Protocol : %s' %proto)

        lport = nm[host][proto].key()
        lport.sort()
        for port in lport:
            print('port : %s \tstate :%s' %(port,nm[host][proto][port]['state']))
