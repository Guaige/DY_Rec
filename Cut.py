#coding=gbk
import os


def duration(str_s, str_e):
    r = [0, 0, 0]
    time_s = str_s.split(':')
    time_e = str_e.split(':')
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


file_name = input("文件名 : ")
time_s = input("起始时间 : ")
time_e = input("结束时间 : ")
cmd = "ffmpeg -ss 0 -t " + duration(time_s, time_e) + " -accurate_seek -i " + file_name + " -codec copy CUT_" + file_name
print(cmd)
print(os.popen(cmd))
# ffmpeg -ss 10 -t 15 -accurate_seek -i test.mp4 -codec copy cut.mp4