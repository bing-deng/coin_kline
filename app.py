import requests
import json
import datetime
import time
import os


symbolList = ["BTC_CW"]#,"EOS_CW","BCH_CW","BSV_CW","ETC_CW","ETH_CW","XRP_CW","TRX_CW"]
today =  str(datetime.date.today())
os.mkdir(today)
pwd = os.path.dirname(os.path.realpath(__file__)) +"/" + today
for j in ["1min","5min","15min","30min","60min"]:
    for i in symbolList:
        url = "http://api.hbdm.com/market/history/kline?period=" + j + "&size=200&symbol="+i
        
        t = requests.get(url).json()
        name = i+"_"+j+"_"+today+".json"
        with open(os.path.join(pwd,name), 'w') as outfile:
            json.dump(t, outfile)
    time.sleep(2)