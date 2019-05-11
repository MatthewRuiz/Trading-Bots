class TradingStrategies(object):

    def __init__(self):
        print('init')

    @staticmethod
    def golden_cross(close_prices, indicators):

        sma_200 = indicators.SMA(close_prices, 200)
        sma_50 = indicators.SMA(close_prices, 50)
        ema_20 = indicators.EMA(close_prices, 20)

        if (sma_200 == None or sma_50 == None or ema_20 == None):
            return False
        elif (sma_50 > sma_200 and ema_20 > sma_50):
            return True
        else:
            return False

    @staticmethod
    def bullish_three_line_strike(open_prices, close_prices): 
        print()
    
