
from alpha_vantage.timeseries import TimeSeries



key = 'UJ5ZFHNSAGEVGEY6'

ts = TimeSeries(key)

aapl,meta =ts.get_daily(symbol ='AAPL')

li = []
print(aapl['2021-03-05'])




class Stock_Manager:

    def __init__(self):
        self.key = 'UJ5ZFHNSAGEVGEY6'
        











### create 