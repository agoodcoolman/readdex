
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = 'agoodcoolman@gmail.com'
toaddr = '86613047@gmail.com'
text = 'test email message sent from Python code'
username = 'fromaddruser'
password = 'fromaddrpassword'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()


