# encoding: utf-8
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
        filename = key + time.strftime("__%H_%M_%S", time.localtime())+".flv"
        print('\r' + filename)
        r = requests.get(addr, stream=True, timeout=1)
        f = open(filename, "wb")
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
                print("\rRecording", end='', flush=True)
    except:
        print("\rFailure : " + msg, end='', flush=True)


ID = input("ID : ")
#ID = 1379191
while 1:
    Rec(ID)

