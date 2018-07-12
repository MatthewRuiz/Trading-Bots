import time
from bot_log import BotLog

class BotCandlestick():
    def __init__(self,period):
        self.output = BotLog()
        self.period = period
        self.current = None
        self.open = None
        self.close = None
        self.high = None
        self.low = None
        self.startTime = time.time()
        self.priceAverage = None
        
        
    def tick(self,price):
        self.current = float(price)
        # set open if new candlestick
        if(self.open is None):
            self.open = self.current
        # set high if previous is surpassed
        if ((self.high is None) or (self.current > self.high)): 
            self.high = self.current
        # set low if previous is greater
        if ((self.low is None) or (self.current < self.low)):
            self.low = self.current
        # If it is the end of the candlestick, set close price and  the price average.
        if (time.time() >= (self.startTime + self.period)):
            self.close = self.current
            self.priceAverage = (self.high + self.low + self.close)/float(3)
            
        self.output.log("Open: "+str(self.open)+" Close: "+str(self.close)+" High: "+str(self.high)+" Low: "+str(self.low)+" Current: "+str(self.current))

    def isClosed(self):
        if (self.close is not None):
            return True
        else:
            return False