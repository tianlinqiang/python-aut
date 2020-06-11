#!/usr/bin/python
#coding=utf-8

import smtplib
import string

HOST = "smtp.qq.com"   #mail host 
SUBJECT = "Test email from Python" #mail project
TO = "tlq666forjob@163.com"
FROM = "1993123920@qq.com"
text = "TEXE  python "
BODY = string.join((
        "From: %s" % FROM,
        "TO: %s" % TO,
        "SUBJECT: %s" % SUBJECT,
        "",
        text
    ),"\r\n")

server = smtplib.SMTP()
server.connect(HOST,587)
server.starttls()
server.login("1993123920@qq.com","cdncsdfeksfawfanfafcakfbagfcafha")
server.sendmail(FROM,(TO),BODY)
server.quit()


