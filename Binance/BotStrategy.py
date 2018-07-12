from BotLog import BotLog
from BotIndicators import BotIndicators

class BotStrategy():
    def __init__(self):
        self.output = BotLog()
        self.prices = []
        self.close = []
        self.currentPrice = ""
        self.currentOpen = ""
        self.currentClose = ""
        self.indicators = BotIndicators()
        
        self.BTCSMA = []
        
    def tick(self, candlestick):
        self.currentPrice = float(candlestick.priceAverage)
        self.prices.append(self.currentPrice)
        self.SMA = self.indicators.SMA(self.prices,3)
        self.WMA = self.indicators.WMA(self.prices,3)
        self.EMA = self.indicators.EMA(self.prices,3)
        
        if self.SMA != None:
            self.output.log("Moving Average: " + str(self.SMA))
            
        if self.WMA != None:
            self.output.log("Weighted Moving Average: " + str(self.WMA))
            
    def printIndicators(self):
        self.indicators.printIndicators()
        