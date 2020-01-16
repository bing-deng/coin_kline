import requests
import json
import datetime
import time

symbolList = ["BTC_CW","EOS_CW","BCH_CW","BSV_CW","ETC_CW","ETH_CW","XRP_CW","TRX_CW"]
for j in ["1min","5min","15min","30min","60min"]:
    for i in symbolList:
        url = "http://api.hbdm.com/market/history/kline?period=" + j + "&size=200&symbol="+i
        today =  datetime.date.today()
        t = requests.get(url).json()
        name = i+"_"+j+"_"+str(today)+".json"
        # name = "./" + j +"/"+ name
        with open(name, 'w') as outfile:
            json.dump(t, outfile)
    time.sleep(2)