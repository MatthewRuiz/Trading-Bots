import numpy as np
from functools import reduce
from bot_log import BotLog

class BotIndicators():    
    def __init__(self):
        self.output = BotLog()
        self.SMAs = []
        self.WMAs = []
        self.EMAs = []
        pass
    
    def SMA(self, dataPoints, period):
        if (len(dataPoints) >= period):
            sma = float(sum(dataPoints[-period:]) / float(period))
            self.SMAs.append(sma)
            return sma
        
    def WMA(self, dataPoints, period):
        if (len(dataPoints) >= period):
            sumOfWeightedAverages = 0
            sumOfWeight = 0
            tempPeriod = period
        
            for weight in range (1,period+1):
                s = dataPoints[-tempPeriod]
                tempPeriod -= 1
                sumOfWeightedAverages += (s*weight)
                sumOfWeight += weight
            
            wma = sumOfWeightedAverages / sumOfWeight 
            self.WMAs.append(wma)
            return wma
        
    def EMA(self, dataPoints, num_periods):
        if (len(dataPoints) >= 2):
            if len(self.EMAs) == 0:
                previousDay = 0
            else:
                previousDay = self.EMAs[len(self.EMAs)-1]
            multiplier = (2 / (num_periods + 1))
            ema = (dataPoints[-1] - previousDay) * multiplier + previousDay
            self.EMAs.append(ema)
            return ema
        
    def RSI(self, dataPoints, period):
        if (len(dataPoints) >= period):
            firstAverageGain = reduce(lambda x,y: x+y, dataPoints)
            
        print (firstAverageGain)
        
    def printIndicators(self):
        self.output.log("SMA: {}".format(self.SMAs))
        #self.output.log("WMA: {}".format(self.WMAs))
        #self.output.log("EMA: {}".format(self.EMAs))
        
    
            
            
            
    