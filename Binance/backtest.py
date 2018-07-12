import sys, getopt
import json
import time
import datetime
from BotIndicators import BotIndicators
from prettytable import PrettyTable

def main():
    test1()
    
def load_data():
    with open('history/binance/BTCUSDT/test.txt') as file:
        data = json.load(file)
        
    return data

def test1():
    """Test for golden cross"""
    closePrices = []                 
    indicators = BotIndicators()           
    data = load_data()
    position_entered = False
    entry_price = 0.0
    purse = 0.0

    period_count = 0

    table = PrettyTable ()
    table.field_names = ['Date', 'Entry', 'Exit', 'Length of Trade', 'Net($)', 'Net(%)']
    
    table.align['Entry'] = 'r'
    table.align['Exit'] = 'r'
    table.align['Length of Trade'] = 'l'
    table.align['Net($)'] = 'r'
    table.align['Net(%)'] = 'r'

    table_row = []
    for tick in data:
        closePrices.append(float(tick[2])) 
        
        sma_200 = indicators.SMA(closePrices, 200)
        sma_50 = indicators.SMA(closePrices, 50)
        ema_20 = indicators.EMA(closePrices, 20)
        
        entry = is_valid_entry(sma_200,sma_50,ema_20)

        if (position_entered == False):
            if (entry == True):
                position_entered = True
                entry_price = float(tick[2])
                table_row = [
                                time.strftime('%Y-%m-%d %H:%m', time.localtime(int(tick[0]/1000))), # Convert from milliseconds to seconds
                                money_format(entry_price)
                            ]
        else:
            if (entry == False):
                position_entered = False
                exit_price = float(tick[2])
                length_of_trade = get_length_of_trade(period_count)
                net_of_trade = calculate_net_of_trade(entry_price, exit_price)
                net_usd = net_of_trade[0]
                percentage = net_of_trade[1]
                purse += net_of_trade[0]

                table_row.extend((money_format(exit_price), length_of_trade,
                                 money_format(net_usd), percentage_format(percentage)))

                table.add_row(table_row)

                period_count = 0
         
        period_count += 1

    print(table)        
    print ('Net Profit: {}'.format(money_format(purse)))

def is_valid_entry(sma_200,sma_50,ema_20):
    if (sma_200 == None or sma_50 == None or ema_20 == None):
        return False
    elif (sma_50 > sma_200 and ema_20 > sma_50):
        return True
    else:
        return False
    
def print_entry(entry_price):
    print ( "Entry Price at: " + str(entry_price))

def get_length_of_trade(period_count):
    total_hours = period_count * 4
    days = int(total_hours / 24)
    hours = int(total_hours - (days * 24))
    
    return "Length of Trade : " + str(days) + "days " + str(hours) + "hours"

def calculate_net_of_trade(entry_price,exit_price):
    percentage = float((exit_price - entry_price) / entry_price)
    net_of_trade = exit_price - entry_price
    return [net_of_trade, percentage]

def percentage_format(num):
    return '{:.2%}'.format(num)
    
def money_format(num):
    return '${:,.2f}'.format(num)


if __name__ == "__main__":
    main()