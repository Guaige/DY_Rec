import time
import requests


def Track_Latest():
    url = "https://details.jd.com/lazy/getOrderTrackInfoMultiPackage.action"
    data = "orderId=114993895858&orderType=0&orderStatus=15&orderStoreId=305&pickDate=1589385600043"
    headers = {
        "cookie" : "shshshfpa=9cbf9135-de16-c379-3f6e-24738877c57e-1576494686; shshshfpb=gZ2dCfM2cb4ANucn6Hozlyw%3D%3D; pinId=dz6XM9i9LsC1ffsfn98I-w; __jdu=15764946854061188222073; __jdv=76161171|direct|-|none|-|1589338721391; areaId=1; PCSYCityID=CN_110000_110100_110114; pin=zhsjzczy; unick=guaige1995; _tp=NF%2FggdzB%2Ff4KXNEj1TRFSg%3D%3D; _pst=zhsjzczy; user-key=08d72469-73b7-4c1b-95a3-8f3d0953fb06; ipLoc-djd=1-2901-4135-0.1096256177; ipLocation=%u5317%u4eac; TrackID=1Qa3ZHn7hiZzR_Zc7Xt5qlC-izCb-kQfniGciyQ7Vpo-FmzjCYaQlPDRrpIoIxB3yk7g7oM96tdGOH87eLQ3KGQglzYQu39LuIcIjS3iZJvs; ceshi3.com=000; mt_xid=V2_52007VwMWVFpdWl8YQB1ZBGADEltUW1FZHk8bbFJnAhFUWgoBRhZNSlQZYlRCUUELAV8WVR4MA2EDGltZXAVcF3kaXQZmHxNWQVhXSx9LElkAbAYaYl1oUmocSB5fAW8DEldbaFBeHks%3D; cn=0; thor=1EE3399E9847437F75EAAAD4338DB86E9E06FFB11980FF4C377DEAA11DAF1FF39A8ED8F6055FAFA696EBF6672FC04F14EE0E43D02D3B32CD6C0428522838665046B8652BE9AC7CC44D2255CEC979F59B88E6DAB7C66C25A8EB742050BBBB1CA89ED37292564390F336D1AF1B83220587E231FB4DC987E9D8E429B75E56D0915AAB97BAC81CC4A0AB5FEA38704FA6473B; shshshfp=ecce5c84052334c6f3058fb84d9ebd89; shshshsID=369ae57c6b23e61891c6986aa5f6f758_1_1589445321915; __jda=122270672.15764946854061188222073.1576494685.1589440773.1589445321.76; __jdc=122270672; 3AB9D23F7A4B3C9B=6I5O3XPZPXH3TVNV6CROMV74ZAZW5VYIRPDWY47LXH6VPSQFILMSK4LO6CMIWREEYRL7FUQ2NLGFIFT4CSWQA5K7SA; __jdb=122270672.5.15764946854061188222073|76.1589445321",
        "content-type": "application/x-www-form-urlencoded",
    }
    #ret = requests.post(url, data=data).json()['multiPackageTrackInfoList'][0]['trackGroupInfo']['orderTrackShowList']
    ret = requests.post(url, data=data, headers=headers).json()['multiPackageTrackInfoList'][0]['trackGroupInfo']['orderTrackShowList']
    count = 0
    for i in ret:
        #(i['Content'] + '\t' + i['CreationTime'])
        count += 1
    #time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('\r' + time.strftime("%H:%M:%S", time.localtime()) + '\t' + i['Content'] + '\t' + i['CreationTime'], end='', flush=True)
    return count


ctr = 13
while 1:
    cur = Track_Latest()
    if cur > ctr:
        print("\rUpdate !")
        ctr = cur
    time.sleep(60)