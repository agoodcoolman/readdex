# -*- coding: utf-8 -*-
import ssl

import requests
import smtplib

from email.mime.text import MIMEText
from email.header import Header

smtpObj = smtplib.SMTP()

def request() :

    url = "https://m.dianping.com/activity-util/disney/421";
    headers = {"Accept":"*/*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding":"gzip", "User-Agent" : "okhttp/3.12.2", "Content-Length": 157, "token": "01bc418993f9f2cc59afce1e9bb09943bb0394b233849187050d007762f91fe810427defe8c585fa596f30efff1a933619dc488f81b4c42551ba3fc06c7e5489"}
    data = {"lat":"","lng":"","appCityId":"16","locatedCityId":0,"dpId":"b86a7f3ac5f947e49a1ec22ea3ef4080a159829798738527584","page":0,"pageSize":10,"couponCategory":1}

    res = requests.post(url, data= data, headers = headers)
    print res.json()

def initEmail():
    context = ssl.create_default_context()
    # mail_host = "stmp.qq.com"  # 设置服务器
    # mail_user = "331381757"  # 用户名
    # mail_pass = "2jinmingkai"  # 口令
    # mail_host = "stmp.163.com"  # 设置服务器
    # mail_user = "agoodcoolman@163.com"  # 用户名
    # mail_pass = "1jinmingkai"  # 口令
    # smtpObj.connect(mail_host, 25)
    # smtpObj.login(mail_user,mail_pass)

    sender = "agoodcoolman@163.com"
    receivers = ["agoodcoolman@163.com"]

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("agoodcoolman@163.com", 'utf-8')
    message['To'] = Header("agoodcoolman@163.com", 'utf-8')




    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.163.com", "25")
        state = smtpObj.login("agoodcoolman@163.com", "1jinmingkai")
        if state[0] == 235:
            smtpObj.sendmail(sender, receivers, message.as_string())
            print "邮件发送成功"
        smtpObj.quit()
    except smtplib.SMTPException, e:
        print str(e)


def sendEmail() :
    sender = 'xiaokeai@qq.com'
    receivers = ['86613047@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print '发送成功！'

if __name__ == '__main__':
    # request();
    initEmail()
    # sendEmail()
