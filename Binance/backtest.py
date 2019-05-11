import sys, getopt, json, datetime, argparse
from TradingStrategies import TradingStrategies
from Formatter import Formatter
from TradeUtilityFunctions import TradeUtilityFunctions
from TimeConversions import TimeConversions
from bot_indicators import BotIndicators
from prettytable import PrettyTable
    
def load_data(pair):
    with open('history/historical_data/{}.txt'.format(pair)) as file:
        data = json.load(file)
        
    return data

def create_table():
    table = PrettyTable ()
    table.field_names = ['Date Entered', 'Entry Price', 'Date Exited', 'Exit Price', 'Length of Trade', 'Net($)', 'Net(%)']
    
    table.align['Entry Price'] = 'r'
    table.align['Exit Price'] = 'r'
    table.align['Length of Trade'] = 'l'
    table.align['Net($)'] = 'r'
    table.align['Net(%)'] = 'r'

    return table

def test_one(pair):
    # print('pair: ' + pair)
    table = create_table()      
    indicators = BotIndicators()
    data = load_data(pair)      # Historical data for given currency

    position_entered = False    # Used to track when to enter/exit trade
    entry_price = 0.0           
    entry_date = 0
    exit_date = 0
    purse = 0.0                 # Amount gained/lossed from trading
    close_prices = []
    table_row = []    
    period_count = 0          


    for tick in data:
        # tick - OHLCV
        current_price = float(tick[2])
        close_prices.append(current_price)

        golden_cross_entry = TradingStrategies.golden_cross(close_prices, indicators)

        if not position_entered:
            if (golden_cross_entry):
                position_entered = True
                entry_price = current_price
                entry_date = TimeConversions.milliseconds_to_date(tick[0])
                current_price_formatted = Formatter.money_format(current_price)
                table_row = [entry_date, current_price_formatted]
                # print('entry_date: {} current_price: {}'.format(entry_date, money_format(current_price)))
        else:
            if not golden_cross_entry:
                position_entered = False
                exit_date = TimeConversions.milliseconds_to_date(tick[0])
                length_of_trade = TradeUtilityFunctions.get_length_of_trade(period_count)
                net_of_trade = TradeUtilityFunctions.calculate_net_of_trade(entry_price, current_price)
                net_usd = net_of_trade[0]
                purse += net_usd
                percentage = net_of_trade[1]

                # print('net_usd: {} percentage: {}'.format(net_usd, percentage))

                table_row.extend((exit_date, Formatter.money_format(current_price),
                 length_of_trade, Formatter.money_format(net_usd), Formatter.percentage_format(percentage)))

                table.add_row(table_row)

                period_count = 0

        if position_entered:
            period_count += 1

    print(table)
    print ('Net Profit: {}'.format(Formatter.money_format(purse)))


def test_two(pair):
    data = load_data(pair)      # Historical data for given currency

    for tick in data:
        print(TradeUtilityFunctions.is_green_candle(tick))
        break