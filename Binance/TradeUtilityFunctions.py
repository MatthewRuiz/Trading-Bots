class TradeUtilityFunctions(object):
    @staticmethod
    def get_length_of_trade(period_count):
        total_hours = period_count * 4
        days = int(total_hours / 24)
        hours = int(total_hours - (days * 24))
        
        return str(days) + "days " + str(hours) + "hours"

    @staticmethod
    def calculate_net_of_trade(entry_price,exit_price):
        percentage = float((exit_price - entry_price) / entry_price)
        net_of_trade = exit_price - entry_price
        return [net_of_trade, percentage]

    @staticmethod
    def is_green_candle(tick):
        open_price = float(tick[1])
        close_price = float(tick[4])
        return open_price > close_price

    @staticmethod
    def check_trend(data_points):
        print()