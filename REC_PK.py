import hashlib
import os
import execjs
import requests
import re
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header


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


class DouYu:

    def __init__(self, rid):
        self.did = '10000000000000000000000000001501'
        self.t10 = str(int(time.time()))
        self.t13 = str(int((time.time() * 1000)))

        self.s = requests.Session()
        self.res = self.s.get('https://m.douyu.com/' + str(rid)).text
        result = re.search(r'rid":(\d{1,7}),"vipId', self.res)

        if result:
            self.rid = result.group(1)
        else:
            raise Exception('房间号错误')

    @staticmethod
    def md5(data):
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    def get_pre(self):
        url = 'https://playweb.douyucdn.cn/lapi/live/hlsH5Preview/' + self.rid
        data = {
            'rid': self.rid,
            'did': self.did
        }
        auth = DouYu.md5(self.rid + self.t13)
        headers = {
            'rid': self.rid,
            'time': self.t13,
            'auth': auth
        }
        res = self.s.post(url, headers=headers, data=data).json()
        error = res['error']
        data = res['data']
        key = ''
        if data:
            rtmp_live = data['rtmp_live']
            key = re.search(r'(\d{1,7}[0-9a-zA-Z]+)_?\d{0,4}(/playlist|.m3u8)', rtmp_live).group(1)
        return error, key

    def get_js(self):
        result = re.search(r'(function ub98484234.*)\s(var.*)', self.res).group()
        func_ub9 = re.sub(r'eval.*;}', 'strc;}', result)
        js = execjs.compile(func_ub9)
        res = js.call('ub98484234')

        v = re.search(r'v=(\d+)', res).group(1)
        rb = DouYu.md5(self.rid + self.did + self.t10 + v)

        func_sign = re.sub(r'return rt;}\);?', 'return rt;}', res)
        func_sign = func_sign.replace('(function (', 'function sign(')
        func_sign = func_sign.replace('CryptoJS.MD5(cb).toString()', '"' + rb + '"')

        js = execjs.compile(func_sign)
        params = js.call('sign', self.rid, self.did, self.t10)
        params += '&ver=219032101&rid={}&rate=-1'.format(self.rid)

        url = 'https://m.douyu.com/api/room/ratestream'
        res = self.s.post(url, params=params).text
        key = re.search(r'(\d{1,7}[0-9a-zA-Z]+)_?\d{0,4}(.m3u8|/playlist)', res).group(1)

        return key

    def get_real_url(self):
        error, key = self.get_pre()
        if error == 0:
            pass
        elif error == 102:
            raise Exception('房间不存在')
        elif error == 104:
            raise Exception('房间未开播')
        else:
            key = self.get_js()
        return "http://tx2play1.douyucdn.cn/live/{}.flv".format(key)


ID = input("PK_ID: ")
MailCount = 0
Count = 0
if __name__ == '__main__':
    while True:
        try:
            s = DouYu(ID)
            ret = s.get_real_url()
            pattern = re.compile(r'\d+vs\d+')
            if pattern.search(ret):
                try:
                    time_s = time.strftime("%H_%M_%S", time.localtime())
                    filename = time_s + '__' + pattern.search(ret).group() + ".flv"
                    print('\rTracking ' + filename)
                    r = requests.get(ret, stream=True, timeout=5)
                    f = open(filename, "wb")
                    for chunk in r.iter_content(chunk_size=512):
                        if chunk:
                            f.write(chunk)
                            print("\rRecording_PK\t" + ret + '\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
                except Exception as e:
                    ErrorText = str(e) + ' ' + pattern.search(ret).group() + ' ' + time.strftime("%H:%M:%S", time.localtime())
                    f = open(pattern.search(ret).group() + '.txt', "a")
                    print(ErrorText)
                    f.write(ErrorText + '\n')
                    f.close()
                cmd = "ffmpeg -i " + filename + " -codec copy CUT_" + filename
                print('\n' + cmd)
                print(os.popen(cmd))
            else:
                print('\r Tracked Normal Link :\t' + ret + '\t' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
            '''
            ret_n = ''
            if Count == 0:
                time_s = time.strftime("%H_%M_%S", time.localtime())
                if pattern.search(ret):
                    strID = pattern.search(ret).group()
                else:
                    strID = str(ID)
                filename = strID + "__" + time_s + ".flv"
                print('\rTracking ' + filename)
                cmd = 'curl -o ' + filename + ' ' + ret
                print(cmd)
                print(os.popen(cmd))
                Count += 1
                ret_l = ret
                if not pattern.search(ret):
                    ret_n = ret
                continue
            if ret_l != ret and ret_n != ret:
                time_s = time.strftime("%H_%M_%S", time.localtime())
                if pattern.search(ret):
                    strID = pattern.search(ret).group()
                else:
                    ret_n = ret
                    strID = str(ID)
                filename = strID + "__" + time_s + ".flv"
                print('\rTracking ' + filename)
                cmd = 'curl -o ' + filename + ' ' + ret
                print(cmd)
                print(os.popen(cmd))
                ret_l = ret

            pattern = re.compile(r'\d+vs\d+')
            if not pattern.search(ret):
                print('\rNOT PKing!\t' + ret + ' ' + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
                continue
            ID_PK = pattern.search(ret).group()            
            MailCount += 1
            if MailCount == -1:
                mail_reminder(str(ID) + ' Living!', str(ID))
                print('Mail Sent!\t' + str(ID) + ' ' + time.strftime("%H:%M:%S", time.localtime()))

            cmd = "ffmpeg -i " + filename + " -codec copy CUT_" + filename
            print(cmd)
            #print(os.popen(cmd))
            
            '''

        except Exception as e:
            ErrorText = str(e) + ' ' + time.strftime("%H:%M:%S", time.localtime())
            f = open(str(ID) + '_PK.txt', "a")
            print('\r' + ErrorText, end='', flush=True)
            f.write(ErrorText + '\n')
            f.close()
        time.sleep(1)
