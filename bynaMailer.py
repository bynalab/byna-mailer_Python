#!/usr/bin/python

import smtplib


emails = open("config/b-lead/emails.txt", "r")
bynaServer = open("config/serverinfo.txt", "r")
bynaMSG = open("config/b-message/fm.txt", "r")

byna = bynaServer.readline()
host = bynaServer.readline().replace('\n','')
user = bynaServer.readline().replace('\n','')
password = bynaServer.readline().replace('\n','')

server = smtplib.SMTP(host,25)
server.starttls()
server.login(user, password)

message = bynaMSG.read()

for email in emails:  
    server.sendmail(user, email, message),      
print "Successfully sent email!"
