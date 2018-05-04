import smtplib
import ConfigParser
import subprocess

configParser = ConfigParser.RawConfigParser()   
configFilePath = r'mail.config'
configParser.read(configFilePath)

username = configParser.get('mail_config', 'username')
password = configParser.get('mail_config', 'password')
msg = configParser.get('mail_config', 'msg')
subject = configParser.get('mail_config', 'subject')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()


#Next, log in to the server
server.login(username, password)

message = 'Subject: {}\n\n{}'.format(subject, msg)

task = subprocess.Popen("mosquitto_sub -h 'server' -u 'user' -P 'password' -t 'topic'", shell=True, stdout=subprocess.PIPE)
while task.poll() is None:
	data = task.stdout.readline()
	print data

	server.sendmail(username, username,message)
