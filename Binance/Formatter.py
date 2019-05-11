class Formatter(object):
    @staticmethod
    def percentage_format(num):
        return '{:.2%}'.format(num)
    
    @staticmethod
    def money_format(num):
        return '${:,.2f}'.format(num)