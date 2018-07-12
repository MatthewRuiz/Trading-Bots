
Data
----

We can use the file [*price_retreiver.py*](price_retriever.py) to retrieve historical data for a given trading-pair from Binance. 
In this example, we will trade the BTC/USDT pair on a 4-hour timeframe starting on 08/17/17, respectfully. 

```python
import price_retriever as pr

pair = 'BTCUSDT'            # The BTC pricing data from the USDT market.
period = '4h'               # 4-hour timeframe
start_date = '2017-08-17'   # UTC Format

# Get the historical data from Binance
pr.getHistoricalData(pair, period, start_date)
```

Notice that the file *BTCUSDT.txt* is created into the /history/historical_data/ folder.

##### 

BACKTESTING
-----------

The only available strategy at this time is to check for the [Golden Cross](https://www.investopedia.com/terms/g/goldencross.asp) using the [Standard Moving Average](https://www.investopedia.com/terms/s/sma.asp) for periods of 50 and 200 along with a [Exponential Moving Average](https://www.investopedia.com/terms/e/ema.asp) with a period of 20.

```python
import backtest at bt

bt.golden_cross('BTCUSDT')
```
The following data will be printed to the console:

```
+------------------+-------------+------------+----------------------------------+------------+---------+
|   Date Entered   | Entry Price | Exit Price | Length of Trade                  |     Net($) |  Net(%) |
+------------------+-------------+------------+----------------------------------+------------+---------+
| 2017-10-02 12:10 |   $4,419.94 |  $4,226.05 | Length of Trade : 49days 0hours  |   $-193.89 |  -4.39% |
| 2017-10-06 00:10 |   $4,392.36 |  $5,541.51 | Length of Trade : 19days 20hours |  $1,149.15 |  26.16% |
| 2017-10-29 12:10 |   $6,085.00 |  $7,149.18 | Length of Trade : 16days 0hours  |  $1,064.18 |  17.49% |
| 2017-11-15 15:11 |   $7,240.06 | $16,488.98 | Length of Trade : 40days 16hours |  $9,248.92 | 127.75% |
| 2017-12-27 07:12 |  $15,155.01 | $14,378.90 | Length of Trade : 9days 0hours   |   $-776.11 |  -5.12% |
| 2018-02-20 11:02 |  $11,668.00 |  $9,807.89 | Length of Trade : 54days 0hours  | $-1,860.11 | -15.94% |
| 2018-02-27 23:02 |  $10,748.86 | $10,679.56 | Length of Trade : 12days 12hours |    $-69.30 |  -0.64% |
| 2018-04-18 00:04 |   $8,107.23 |  $8,915.09 | Length of Trade : 55days 0hours  |    $807.86 |   9.96% |
| 2018-05-03 00:05 |   $9,249.86 |  $9,187.56 | Length of Trade : 7days 8hours   |    $-62.30 |  -0.67% |
| 2018-07-10 00:07 |   $6,601.17 |  $6,376.13 | Length of Trade : 62days 8hours  |   $-225.04 |  -3.41% |
+------------------+-------------+------------+----------------------------------+------------+---------+
Net Profit: $9,083.36
```


# More to come

