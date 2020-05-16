import os
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from win10toast import ToastNotifier

import requests


def mail_reminder(rid):
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "2967322586"  # 用户名
    mail_pass = "ylrtzbaxjxikdgbi"  # 口令
    sender = '2967322586@qq.com'
    receivers = ['guaige1995@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText('Douyu.com/' + rid + ' is Living!', 'plain', 'utf-8')
    message['From'] = Header("Douyu Reminder", 'utf-8')
    message['To'] = Header("guaige1995", 'utf-8')
    subject = rid + 'Living!'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")


def monitor(rid):
    try:
        response = requests.get('https://www.douyu.com/{}'.format(rid)).text
        real_url = re.findall(r'live/({}[\d\w]*?)_'.format(rid), response)[0]
        mail_reminder(rid)
        cmd = "http://tx2play1.douyucdn.cn/live/" + real_url + ".flv"
        #toaster = ToastNotifier()
        #toaster.show_toast(u'开播啦', str(rid), duration=60)
        os.popen('ffplay -x 1280 -y 720 -i ' + cmd)
        exit(0)
    except IndexError:
        i = 0


rid = input("ID : ")
while 1:
    monitor(rid)
    time.sleep(1)
    print('\r未开播\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
#return "http://tx2play1.douyucdn.cn/live/" + real_url + ".flv"