import requests
ret = requests.get("https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=42409").json()['data']['items']
#res = ret.json()['data']['items']
for i in ret:
    print(i['price'])