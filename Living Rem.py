import re
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

from pip._vendor import requests


def mail_reminder(sub, text):
    mail_host = "smtp.qq.com"
    mail_user = "see1deer"
    mail_pass = "vzsgdsjwydbndegh"
    sender = 'see1deer@qq.com'
    receivers = ['guaige1995@qq.com']
    message = MIMEText(text)
    message['From'] = Header('Guai_296', 'utf-8')
    message['To'] = Header('Guaige1995', 'utf-8')
    message['Subject'] = Header(sub, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("Sent")


header = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzI0MDM3MTI5NSIsImlhdCI6MTYwMjIwNTIxNSwiZXhwIjoxNjAyODEwMDE1fQ.ebEXWP-l7ZmEiQoCO5qtxG7SxeaLHZomAyzVbg011XQEGVzXq_ZRn5TV9kT6bwijQAKqND5iToCdTWqKwyVqBg"
}


year_month = time.strftime("%Y-%m-", time.localtime())
day = time.strftime("%d", time.localtime())
date = year_month + day
rid = '7189349'
while True:
    ret = requests.get(
                "https://www.bojianger.com/data/api/auth/anchor_detail_total.do?date=" + date + "&rid=" + rid
                    .format(rid, rid), headers=header)
    msg = ret.json()['data']['total_statistic']['living']
    if msg:
        mail_reminder('Living!', rid)
        print(rid + ' Living!\r')
        exit(0)
    print('\r' + rid + ' Waiting!\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
    time.sleep(1)
