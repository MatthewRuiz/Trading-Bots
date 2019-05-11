import time

class TimeConversions(object):
    @staticmethod
    def milliseconds_to_date(ms):
        return time.strftime('%Y-%m-%d %H:%m', time.localtime(int(ms/1000)))