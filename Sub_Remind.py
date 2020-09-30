import re
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

from pip._vendor import requests


def mail_reminder(rid, msg):
    mail_host = "smtp.qq.com"
    mail_user = "2967322586"
    mail_pass = "vzsgdsjwydbndegh"
    sender = '2967322586@qq.com'
    receivers = ['guaige1995@qq.com']
    message = MIMEText(msg)
    message['From'] = Header("Guai_296", 'utf-8')
    message['To'] = Header("guaige1995", 'utf-8')
    message['Subject'] = Header(rid, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("Sent")


header = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzI0MDM3MTI5NSIsImlhdCI6MTYwMTIwMTQyOSwiZXhwIjoxNjAxODA2MjI5fQ.M5SNqPjoGCNsIr7gwVAgCZtecmfAMcvLAqc773sa_MWlPflGMATeqU-6ia1FmxE158Z1Uti5FBsdLZ0ruzCLaw"
}


rid = '7189349'
year_month = time.strftime("%Y-%m-", time.localtime())
day = time.strftime("%d", time.localtime())
date = year_month + day
def get_text():
    url = "https://www.bojianger.com/data/api/auth/audience_detail_danmu.do?date=" + date + "&rid=0&uid=381583758&order=-1&time=-1&duration=0+~24&pageNum=1&pageSize=20"
    ret = requests.get(url, headers=header).json()['data']
    name = ret['name']
    latest_text = (ret['page']['rows'][0]['txt'])
    room = ret['page']['rows'][0]['anchorName']
    return latest_text, room
text0 = get_text()
print(text0[1] + ' ' + text0[0])
while True:
    text = get_text()
    #print('\r' + text0[1] + ' ' + text0[0] + '\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
    if not text0 == text:
        print(text[1] + ' ' + text[0])
        #mail_reminder(text[1], text[0])
        text0 = text
    time.sleep(5)