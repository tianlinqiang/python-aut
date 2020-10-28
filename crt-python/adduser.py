# $language = "Python"
# $interface = "1.0"

def main():
    A=['10.17.8.126']
    for ipadr in A:
        crt.Screen.Send("ssh root@"+ipadr+"\n")
        crt.Screen.WaitForStrings("Are you sure you want to continue connecting (yes/no)?",3000)
        crt.Screen.Send("yes\n")
        crt.Screen.WaitForString("~]$")
        crt.Screen.Send("sudo su -\n")
        crt.Screen.WaitForString("~]#")
        crt.Screen.Send("wget -P /tmp/ http://10.17.10.100:9000/update-zabbix-agent4.4.10.sh \n")
        crt.Screen.WaitForString("~]#")
        crt.Screen.Send("bash /tmp/update-zabbix-agent4.4.10.sh \n")
        crt.Screen.WaitForString("~]#")
        crt.Screen.Send("exit \n")
        crt.Screen.WaitForString("~]$")
        crt.Screen.Send("exit \n")
        crt.Dialog.MessageBox(ipadr+'添加用户成功!')
        crt.Screen.WaitForString("ubuntu@k8s-master:~$ ")
main()

