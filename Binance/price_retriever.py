# Binance Python Wrapper
from binance_api.client import Client
from bot_log import BotLog
# Allows us to access historical data
import save_historical_data as shd
import json
import urllib.request as ur

class Price_Retriever():
    # initialize
    def __init__(self, exchange, pair, period):
        self.pair = pair
        self.period = period
                
        self.data = []
        self.output = BotLog()
        
        if (exchange == "Binance"):
            self.conn = Client('API Key','API Secret')
    
    def getCurrentPrice(self):
        ret = ur.urlopen(ur.Request('https://api.binance.com/api/v3/ticker/price'))
        stuff = json.loads(ret.read())
        for x in range(0,240):
            if (stuff[x]["symbol"] == self.pair):
                lastPairPrice = {}
                lastPairPrice = stuff[int(x)]["price"]
        return lastPairPrice
    
    def getHistoricalData(self, pair, period, start_time, end_time=None):
        ret = shd.get_historical_klines(pair, period, start_time)
        with open("history/binance/BTCUSDT/{}.txt".format(pair),"w+") as file_object:
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

        return 5 # temporary
    
                

#                 +---------------+------------+------------+----------------------------------+------------+---------+
# |      Date     |      Entry |       Exit | Length of Trade                  |     Net($) |  Net(%) |
# +---------------+------------+------------+----------------------------------+------------+---------+
# | 1506960000000 |  $4,419.94 |  $4,226.05 | Length of Trade : 49days 0hours  |   $-193.89 |  -4.39% |
# | 1507262400000 |  $4,392.36 |  $5,541.51 | Length of Trade : 19days 20hours |  $1,149.15 |  26.16% |
# | 1509292800000 |  $6,085.00 |  $7,149.18 | Length of Trade : 16days 0hours  |  $1,064.18 |  17.49% |
# | 1510776000000 |  $7,240.06 | $16,488.98 | Length of Trade : 40days 16hours |  $9,248.92 | 127.75% |
# | 1514376000000 | $15,155.01 | $14,378.90 | Length of Trade : 9days 0hours   |   $-776.11 |  -5.12% |
# | 1519142400000 | $11,668.00 |  $9,807.89 | Length of Trade : 54days 0hours  | $-1,860.11 | -15.94% |
# | 1519790400000 | $10,748.86 | $10,679.56 | Length of Trade : 12days 12hours |    $-69.30 |  -0.64% |
# | 1524024000000 |  $8,107.23 |  $8,915.09 | Length of Trade : 55days 0hours  |    $807.86 |   9.96% |
# | 1525320000000 |  $9,249.86 |  $9,187.56 | Length of Trade : 7days 8hours   |    $-62.30 |  -0.67% |
# | 1531195200000 |  $6,601.17 |  $6,376.13 | Length of Trade : 62days 8hours  |   $-225.04 |  -3.41% |
# +---------------+------------+------------+----------------------------------+------------+---------+
# $9,083.36