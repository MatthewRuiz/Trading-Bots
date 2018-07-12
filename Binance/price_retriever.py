# Binance Python Wrapper
from binance_api.client import Client
# Allows us to access historical data
import save_historical_data as shd
import json
import urllib.request as ur

# class Price_Retriever():
#     # initialize
#     def __init__(self, exchange, pair, period):
#         self.pair = pair
#         self.period = period
                
        # self.data = []
        # self.output = BotLog()
        
        # if (exchange == "Binance"):
        #     self.conn = Client('API Key','API Secret')
    
def getCurrentPrice():
    ret = ur.urlopen(ur.Request('https://api.binance.com/api/v3/ticker/price'))
    stuff = json.loads(ret.read())
    for x in range(0,240):
        if (stuff[x]["symbol"] == "BTCUSDT"):
            lastPairPrice = {}
            lastPairPrice = stuff[int(x)]["price"]
    return lastPairPrice
    
def getHistoricalData(pair, fake_period, start_time, end_time=None):
    period = Client.KLINE_INTERVAL_4HOUR
    ret = shd.get_historical_klines(pair, period, start_time)
    with open("history/historical_data/{}.txt".format(pair),"w+") as file_object:
        exDict = []
        for x in ret:
            time = x[0]
            openPrice = x[1]
            close = x[4]
            high = x[2]
            low = x[3]
            volume = x[5]
            #exDict[time] = {'open' : openPrice,'close' : close,'high' : high,'low' : low,'volume' : volume}
            exDict.append([time,openPrice,close,high,low,volume])
            
        json.dump(exDict, file_object)
        #self.output.log("Time: "+str(time)+" Open: "+str(openPrice)+" Close: "+str(close)+" High: "+str(high)+" Low: "+str(low))

    return None # temporary
