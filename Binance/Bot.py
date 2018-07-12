import argparse
import price_retriever

# Binance Python Wrapper
from binance_api.client import Client
from bot_candlestick import BotCandlestick
from bot_strategy import BotStrategy

def main(argv):
    
    # Check for valid period
    if (argv.period in [1,5,15,30,45,60,120]):
        period = argv.period
    else:
        print ('Binance requires periods in 1,5,15,30,45,60,120 minute increments')
    
    # Check for valid currency pair
    if (argv.currency.upper() in ['BTCUSDT','XMRBTC']):
        pair = argv.currency.upper()
    else:
        print ('Not a valid pair. Please format currency in the format: XXXYYY')
        print ('Unless you are converting BTC to fiat, i.e., BTCUSDT,')
        print ('BTC should be in the YYY position i.e., XMRBTC.')
          
    # Check if exchange is Binance
    # If so, assign exchange the supplied argument.
    if (argv.exchange in ['Binance']):
        exchange = argv.exchange
    elif (argv.exchange == None):
        print ('Exchange is not valid. Please use "Binance" or "Bitfinex"')
       
       
    # chart = Price_Retriever(exchange, pair, period)
    # strategy = BotStrategy()
    
    # candlesticks = []
    
    # developingCandlestick = BotCandlestick(period)
    # Will grab data from 8/17/2017 - 7/12/2018
    price_retriever.getHistoricalData(pair, Client.KLINE_INTERVAL_4HOUR, "August 17, 2017")
    
        
def parse_arguments():
    # Holds all the information necessary to aprse the command line into Python data types.
    parser = argparse.ArgumentParser()
    
    # optional arguments:          
    #   -h                  Show this help message and exit.
    #   --test              Is this run a test run?
    #   --exchange          The desired exchange.
    #   -p, --period        Specifies the period length.
    #   -c, --currency      The currency pair of interest.
    #   -s                  Start time.
    #   -e                  End time.
    parser.add_argument('-t','--test', help='is this run test run (y/n)?',type=str)
    parser.add_argument('--exchange', help='the desired exchange')
    parser.add_argument('-p', '--period', help='the desired period length', type=int)
    parser.add_argument('-c', '--currency', help='the currency pair of interest')
    parser.add_argument('-s', help='start time', type=bool)
    parser.add_argument('-e', help='end time', type=bool)
    
    args = parser.parse_args() 
    return args

def nice_decimal(num):
    return '{0:.3g}'.format(float(num))
    
if __name__ == '__main__':
    arguments = parse_arguments()
    main(arguments)

    
    