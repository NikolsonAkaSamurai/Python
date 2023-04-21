from binance.client import Client
import config
import pandas as pd
import time


client = Client(config.api_key, config.api_secret)

def top_coin():
    all_tickers = pd.DataFrame(client.get_ticker())
    usdt = all_tickers[all_tickers.symbol.str.contains('USDT')]
    work = usdt[~((usdt.symbol.str.contains('UP')) | (usdt.symbol.str.contains('DOWN')))]
    top_coin = work[work.priceChangePercent == work.priceChangePercent.max()]
    top_coin = top_coin.symbol.values[0]
    return top_coin


print(top_coin())


# def last_data(symbol, interval, lookback):
#
#     frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
#     frame = frame.iloc[:,:6]
#     frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
#     frame = frame.set_index('Time')
#     frame.index = pd.to_datetime(frame.index, unit='ms')
#     frame = frame.astype(float)
#     return frame
#
# def strategy(buy_amt, SL=0.985, Target=1.02, open_positon=False):
#     try:
#         asset = top_coin()
#         df = last_data(asset, '1m', '120')
#     except:
#         time.sleep(61)
#         asset = top_coin()
#         df = last_data(asset, '1m', '120')
