#coding=utf-8

import pexpect
import sys

child = pexpect.spawn('ssh root@159.138.21.11')
fout = file('mylog.txt','w')
child.logfile = fout
#child.logfile = sys.stdout


child.expect('#')
child.sendline('ls /')
child.expect('#')
