import re
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

from pip._vendor import requests


def mail_reminder(rid, msg):
    mail_host = "smtp.qq.com"
    mail_user = "see1deer"
    mail_pass = "vzsgdsjwydbndegh"
    sender = 'see1deer@qq.com'
    receivers = ['guaige1995@qq.com']
    message = MIMEText(msg)
    message['From'] = Header('Guai_296', 'utf-8')
    message['To'] = Header('Guaige1995', 'utf-8')
    message['Subject'] = Header(rid, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("Sent")


def header():
    headers = {
        "Host": "playweb.douyucdn.cn",
        "Referer": "https://www.douyu.com/directory/myFollow",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "rid": "296059",
        "time": "1588665840664",
        "auth": "1bb36d3b719b111b6e5cd5c8f8d87a01",
    }
    return headers


rid = '7189349'
while True:
    ret = requests.post(
                "http://playweb.douyucdn.cn/lapi/live/hlsH5Preview/{}?rid={}&did=607b839e075721d60e19e5bc00011501"
                    .format(rid, rid), headers=header())
    msg = ret.json()['msg']
    if not msg == '房间未开播':
        mail_reminder(rid, msg)
        print(msg)
        exit(0)
    print('\r' + rid + ' ' + msg + '\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
    time.sleep(1)