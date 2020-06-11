import pexpect
import sys

ip = "159.138.21.11"
user = "root"
passwd = "tlq123@321"
target_file = "/var/log/nginx/access.log"

child = pexpect.spawn('/usr/bin/ssh',[user+'@'+ip])
fout = file('mylog.txt','w')
child.logfile = fout

try:
#    child.expect('(?i)tlq123@321')
#    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /var/log/nginx/access.tar.gz '+target_file)

    child.expect('#')
    print child.before
#    child.sendline('exit')
    fout.close()
except EOF:
    print "expect EOF"
except TIMEOUT:
    print "expect TIMEOUT"
child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/var/log/nginx/access.tar.gz','/home/ubuntu'])
fout = file('mylog.txt','a')
child.logfile = fout

try:
#    child.expect('(?i)tlq123@321')
#    child.sendline(passwd)
    child.expect(expect.EOF)
except EOF:
    print "expect.EOF"
except TIMEOUT:
    print "except TIMEOUT"
