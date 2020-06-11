import paramiko


hostname = '159.138.21.11'
username = 'root'
password = 'tlq123@321'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()

ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr = ssh.exec_command('free -m')

print stdout.read()
ssh.close()
