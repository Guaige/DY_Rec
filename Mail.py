import smtplib
from email.mime.text import MIMEText
from email.header import Header


'''
try:
    server = smtplib.SMTP()
    server.connect(mail_host, 25)  # 25 为 SMTP 端口号
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''
def mail_reminder(rid):
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


mail_reminder('796449')