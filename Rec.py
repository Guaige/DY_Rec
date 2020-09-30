# encoding: utf-8
import os

import requests
import time


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


def duration(str_s, str_e):
    r = [0, 0, 0]
    time_s = str_s.split('_')
    time_e = str_e.split('_')
    ctr = 0
    for i in range(2, -1, -1):
        time_i = int(time_e[i])
        if ctr == 1:
            time_i -= 1
        if time_i >= int(time_s[i]):
            ctr = 0
            r[i] = time_i - int(time_s[i])
        else:
            ctr = 1
            if i == 0:
                r[0] = time_i -int(time_s[0]) + 24
            else:
                r[i] = time_i - int(time_s[i]) + 60
    return str(r[0]) + ':' + str(r[1]) + ':' + str(r[2])


def Rec(rid):
    msg = "Error 404"
    try:
        ret = requests.post(
            "http://playweb.douyucdn.cn/lapi/live/hlsH5Preview/{}?rid={}&did=607b839e075721d60e19e5bc00011501"
                .format(rid, rid), headers=header())
        msg = ret.json()['msg']
        key = ret.json()['data']['rtmp_live'].split("_")[0]
        if len(key) > 20:
            key = key.split('/')[0]
        addr = "http://tx2play1.douyucdn.cn/" + key + ".flv"
        time_s = time.strftime("%H_%M_%S", time.localtime())
        filename = key + "__" + time_s + ".flv"
        print('\r' + filename)
        r = requests.get(addr, stream=True, timeout=5)
        f = open(filename, "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
                print("\rRecording\t" + time.strftime("%H:%M:%S", time.localtime()), end='', flush=True)
        print("No 1937")
        return time_s, filename
    except:
        print("\rFailure :\t" + msg + time.strftime("\t%H:%M:%S", time.localtime()), end='', flush=True)
        return "1937"


#ID = input("ID : ")
ID = 7189349
while 1:
    time_s = Rec(ID)
    '''
    if not time_s == "1937":
        time_e = time.strftime("%H_%M_%S", time.localtime())
        cmd = "ffmpeg -ss 0 -t " + duration(time_s[0], time_e) + " -accurate_seek -i " + time_s[1] + " -codec copy CUT_" + time_s[1]
        print(cmd)
        print(os.popen(cmd))
    '''
    time.sleep(5)

