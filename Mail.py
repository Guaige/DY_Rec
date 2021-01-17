import smtplib
from email.mime.text import MIMEText
from email.header import Header


'''
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''
def mail_reminder(rid):
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "2967322586"  # 用户名
    mail_pass = "ylrtzbaxjxikdgbi"  # 口令
    sender = '2967322586@qq.com'
    receivers = ['2967322586@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText('Douyu.com/' + rid + ' is Living!', 'plain', 'utf-8')
    message['From'] = Header("Douyu Reminder", 'utf-8')
    message['To'] = Header("2967322586", 'utf-8')
    subject = rid + 'Living!'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
