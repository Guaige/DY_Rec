#!/usr/bin/env python
# encoding: utf-8
import requests
import time
import os
import re


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


def get_addr(rid, cyc):
    ret = requests.post(
        "http://playweb.douyucdn.cn/lapi/live/hlsH5Preview/{}?rid={}&did=607b839e075721d60e19e5bc00011501"
            .format(rid, rid),headers=header())
    print("Awake")
    try:
        #print("Fetching URL")
        key = ret.json()['data']['rtmp_live'].split("_")[0]
        #print(key)
        if len(key) >= 20:
            #print("OverLength")
            key_true = key.split("/")[0]
            #print("key_true = "+key_true)
            key = key_true
        #addr = "timeout 1800 wget http://tx2play1.douyucdn.cn/" + ret.json()['data']['rtmp_live'].split("_")[0] + ".flv "+"-O "+ ret.json()['data']['rtmp_live'].split("_")[0] + "_"+time.strftime("%H:%M:%S", time.localtime())+".flv"
        global FILE_NAME
        if FILE_NAME != "Initial_File":
            cmd_cut = "ffmpeg -ss 00:00:00 -t 00:02:18 -i " + FILE_NAME + ".flv -vcodec copy -acodec copy " + FILE_NAME + "_cut.flv"
            #os.popen(cmd_cut)
            file = open("Cut.txt", "a+")
            file.write(cmd_cut + '\n')
            file.close()
            print(cmd_cut)
            cmd_cvt = "ffmpeg -i " + FILE_NAME + "_cut.flv -c copy -bsf:v h264_mp4toannexb -f mpegts " + FILE_NAME + ".ts"
            #os.popen(cmd_cvt)
            file = open("Cvt.txt", "a+")
            file.write(cmd_cvt + '\n')
            file.close()
            print(cmd_cvt)
            #ffmpeg -i 1.flv -c copy -bsf:v h264_mp4toannexb -f mpegts 1.ts
            cmd_rm_cvt = "rm -r " + FILE_NAME + "_cut.flv"
            cmd_rm = "rm -r " + FILE_NAME + ".flv"
            file = open("rm.txt", "a+")
            file.write(cmd_rm + '\n' + cmd_rm_cvt + '\n')
            file.close()
            #os.popen(cmd_rm)
            print(cmd_rm)
            #os.popen(cmd_rm_cvt)
            print(cmd_rm_cvt)
            print("Previous Cutted")
            file = open("Concat.txt", "a+")
            file.write("file \'" + FILE_NAME +".ts\'\n")
            file.close()
            print("Concat_File Writed")
        FILE_NAME = key + "_"+time.strftime("%H:%M:%S", time.localtime())
        addr = "timeout " + cyc + " wget -c http://tx2play1.douyucdn.cn/" + key + ".flv "+"-O " + FILE_NAME + ".flv"
        print("FILE_NAME : " + FILE_NAME)
        if not re.match(r'(\d+)vs(\d+)x', key):
            global URL
            URL = "timeout " + cyc + " wget -c http://tx2play1.douyucdn.cn/" + key + ".flv "+"-O "+ key + "_"
            print("URL Stored")
        os.popen(addr)
        print(addr)
        #print("Sleeping")
        #time.sleep(60)
        return addr
    except:
        if ret.json()['msg'] == "不支持" and URL != "Initial URL":
            URL_true = URL + time.strftime("%H:%M:%S", time.localtime())+".flv"
            os.popen(URL_true)
            print(ret.json()['msg'])
            print("Keep Recording")
        #time.sleep(60)
        else:
            print(ret.json()['msg'])
        return ret.json()['msg']


#global URL
URL = "Initial URL"
ID = 687423
FILE_NAME = "Initial_File"
ID = input("ID : ")
CYCLE = input("Duration : ")
while 1:
    # print("New")
    get_addr(ID, CYCLE)
    print("Sleeping")
    #print(URL)
    #print(CYCLE)
    time.sleep(int(CYCLE))
    # print("Awake")
# os.popen(get_addr(ID))
# print(cmd.read())

