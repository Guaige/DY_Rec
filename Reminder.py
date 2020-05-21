import os
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
from win10toast import ToastNotifier

import requests


def douyu_mail_reminder(rid):
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "2703507130"  # 用户名
    mail_pass = "slyjcbzsrtaudeed"  # 口令
    sender = 'guaisend@qq.com'
    receivers = ['guaige1995@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText('Douyu.com/' + rid + ' is Living!', 'plain', 'utf-8')
    message['From'] = Header("Douyu Reminder", 'utf-8')
    message['To'] = Header("guaige1995", 'utf-8')
    subject = rid + '\tLiving!'
    message['Subject'] = Header(subject, 'utf-8')
    ret_smtp = smtplib.SMTP(mail_host)
    ret_smtp.ehlo()
    ret_smtp.starttls()
    ret_smtp.connect(mail_host, 587)  # 25 为 SMTP 端口号
    ret_smtp.login(mail_user, mail_pass)
    ret_smtp.sendmail(sender, receivers, message.as_string())
    ret_smtp.close()
    print("邮件发送成功")


def monitor(rid):
    try:
        response = requests.get('https://www.douyu.com/{}'.format(rid)).text
        real_url = re.findall(r'live/({}[\d\w]*?)_'.format(rid), response)[0]
        douyu_mail_reminder(rid)
        cmd = "http://tx2play1.douyucdn.cn/live/" + real_url + ".flv"
        #toaster = ToastNotifier()
        #toaster.show_toast(u'开播啦', str(rid), duration=60)
        os.popen('ffplay -x 1280 -y 720 -i ' + cmd)
        exit(0)
    except IndexError:
        #print(IndexError)
        IndexError


rid = input("ID : ")
while 1:
    monitor(rid)
    time.sleep(1)
    print('\r未开播\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
#return "http://tx2play1.douyucdn.cn/live/" + real_url + ".flv"