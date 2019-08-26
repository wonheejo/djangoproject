
import requests
import pandas as pd
import datetime
import numpy as np
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import seaborn as sns


"""
BTC = Bitcon
ETH = Ethereum
XRP = Ripple
BNB = Binance coin
LTC = Litecoin
EOS = EOS
TRON = Tron
BCH = Bitcoin cash ABC

"""

#function to call on the request of cryptocurrency
def binancePrice():

    #request to get candle data from binance api
    BTC = requests.get('https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1m')
    ETH = requests.get('https://api.binance.com/api/v1/klines?symbol=ETHUSDT&interval=1m')
    XRP = requests.get('https://api.binance.com/api/v1/klines?symbol=XRPUSDT&interval=1m')
    BNB = requests.get('https://api.binance.com/api/v1/klines?symbol=BNBUSDT&interval=1m')
    LTC = requests.get('https://api.binance.com/api/v1/klines?symbol=LTCUSDT&interval=1m')
    EOS = requests.get('https://api.binance.com/api/v1/klines?symbol=EOSUSDT&interval=1m')
    TRX = requests.get('https://api.binance.com/api/v1/klines?symbol=TRXUSDT&interval=1m')
    BCH = requests.get('https://api.binance.com/api/v1/klines?symbol=BCHABCUSDT&interval=1m')

    #request to get binance server time
    t = requests.get('https://api.binance.com/api/v1/time')

    #names the various columns from the requested candle data in a dataframe
    BTC_df = pd.DataFrame(BTC.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    ETH_df = pd.DataFrame(ETH.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    XRP_df = pd.DataFrame(XRP.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    BNB_df = pd.DataFrame(BNB.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    LTC_df = pd.DataFrame(LTC.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    EOS_df = pd.DataFrame(EOS.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    TRX_df = pd.DataFrame(TRX.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])
    BCH_df = pd.DataFrame(BCH.json(), columns=['Opentime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Closetime', '7', '8', '9', '10', '11'])

    #changes the binance servertime into time that is readable(gregorian time)
    BTC_df['Opentime']= pd.to_datetime(BTC_df['Opentime'], unit='ms')
    ETH_df['Opentime']= pd.to_datetime(ETH_df['Opentime'], unit='ms')
    XRP_df['Opentime']= pd.to_datetime(XRP_df['Opentime'], unit='ms')
    BNB_df['Opentime']= pd.to_datetime(BNB_df['Opentime'], unit='ms')
    LTC_df['Opentime']= pd.to_datetime(LTC_df['Opentime'], unit='ms')
    EOS_df['Opentime']= pd.to_datetime(EOS_df['Opentime'], unit='ms')
    TRX_df['Opentime']= pd.to_datetime(TRX_df['Opentime'], unit='ms')
    BCH_df['Opentime']= pd.to_datetime(BCH_df['Opentime'], unit='ms')

    #makes the 'opentime' of the first column each dataframe as the index
    BTC_df.set_index('Opentime', inplace=True)
    ETH_df.set_index('Opentime', inplace=True)
    XRP_df.set_index('Opentime', inplace=True)
    BNB_df.set_index('Opentime', inplace=True)
    LTC_df.set_index('Opentime', inplace=True)
    EOS_df.set_index('Opentime', inplace=True)
    TRX_df.set_index('Opentime', inplace=True)
    BCH_df.set_index('Opentime', inplace=True)

    #droppnig unnecessary columns
    BTC_df = BTC_df.drop(['Closetime', '11'], axis=1)
    ETH_df = ETH_df.drop(['Closetime', '11'], axis=1)
    XRP_df = XRP_df.drop(['Closetime', '11'], axis=1)
    BNB_df = BNB_df.drop(['Closetime', '11'], axis=1)
    LTC_df = LTC_df.drop(['Closetime', '11'], axis=1)
    EOS_df = EOS_df.drop(['Closetime', '11'], axis=1)
    TRX_df = TRX_df.drop(['Closetime', '11'], axis=1)
    BCH_df = BCH_df.drop(['Closetime', '11'], axis=1)

    #converts entire dataframe from object to float and integer
    BTC_df = BTC_df.apply(pd.to_numeric)
    ETH_df = ETH_df.apply(pd.to_numeric)
    XRP_df = XRP_df.apply(pd.to_numeric)
    BNB_df = BNB_df.apply(pd.to_numeric)
    LTC_df = LTC_df.apply(pd.to_numeric)
    EOS_df = EOS_df.apply(pd.to_numeric)
    TRX_df = TRX_df.apply(pd.to_numeric)
    BCH_df = BCH_df.apply(pd.to_numeric)

    # concatenation of the 'close' price columns into one
    data1 = pd.concat([BTC_df['Close'], ETH_df['Close'], XRP_df['Close'], BNB_df['Close'], LTC_df['Close'], EOS_df['Close'],TRX_df['Close'], BCH_df['Close']], axis=1)
    # naming of the columns in the new panda dataframe named 'data'
    data1.columns = ['BTC', 'ETH', 'XRP', 'BNB', 'LTC', 'EOS', 'TRX', 'BCH']
    print(data1)

    #normalizes the dataframes
    BTC_df = (BTC_df - BTC_df.mean()) / (BTC_df.max() - BTC_df.min())
    ETH_df = (ETH_df - ETH_df.mean()) / (ETH_df.max() - ETH_df.min())
    XRP_df = (XRP_df - XRP_df.mean()) / (XRP_df.max() - XRP_df.min())
    BNB_df = (BNB_df - BNB_df.mean()) / (BNB_df.max() - BNB_df.min())
    LTC_df = (LTC_df - LTC_df.mean()) / (LTC_df.max() - LTC_df.min())
    EOS_df = (EOS_df - EOS_df.mean()) / (EOS_df.max() - EOS_df.min())
    TRX_df = (TRX_df - TRX_df.mean()) / (TRX_df.max() - TRX_df.min())
    BCH_df = (BCH_df - BCH_df.mean()) / (BCH_df.max() - BCH_df.min())

    #concatenation of the 'close' price columns into one
    data2 = pd.concat([BTC_df['Close'], ETH_df['Close'], XRP_df['Close'], BNB_df['Close'], LTC_df['Close'], EOS_df['Close'], TRX_df['Close'], BCH_df['Close']], axis=1)
    #naming of the columns in the new panda dataframe named 'data'
    data2.columns = ['BTC', 'ETH', 'XRP', 'BNB', 'LTC', 'EOS', 'TRX', 'BCH']
    print(data2)
    #print(data2.corr())

    #function to visualize the given correlation matrix into a heatmap
    def snsplotfunc(data):
        data = data.corr()
        matrix = sns.heatmap(data,
                             cmap='YlGnBu',
                             annot=True,
                             vmin=0,
                             vmax=1,
                             linewidths=0.5,
                             square=True)

        matrix.set_xticklabels(matrix.get_xticklabels(),
                               horizontalalignment='center')

        matrix.set_yticklabels(matrix.get_yticklabels(),
                               verticalalignment='center',
                               rotation=0)
        matrix.xaxis.set_ticks_position('top')
        matrix.set_title('Correlation of Cryptocurrencies', fontsize=20)
        plt.show()
    #snsplotfunc(data2)

    def matrix1(data):

        coin_names = ['BTC', 'ETH', 'XRP', 'BNB', 'LTC', 'EOS', 'TRX', 'BCH']

        colors = {
            'background': '#111111',
            'text': '#7FDBFF'
        }

        data1 = [go.Heatmap(
            x = coin_names,
            y = coin_names,
            z = data.corr(),
            hoverinfo = 'data.corr()',
            xgap = 3,
            ygap = 3,
            showscale = True)
        ]
        layout = go.Layout(
            title = 'Correlation of Cryptocurrencies',
            xaxis = dict(
                showline = False,
                showgrid = False,
                zeroline = False
            ),
            yaxis = dict(
                showline = False,
                showgrid = False,
                zeroline = False
            ),
            margin = dict(l=80, r=80, t=400, b=300)
        )
        fig = go.Figure(data = data1, layout = layout)
        fig.show()

    matrix1(data2)


    def visualizefunc(data):

        graph1 = go.Figure()
        graph1.add_trace(go.Scatter(
            x = data.index,
            y = data['BTC'],
            name = "BTC",
            line_color = 'deepskyblue',
            opacity = 0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y = data['ETH'],
            name = "ETH",
            line_color = 'darkcyan',
            opacity = 0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y = data['XRP'],
            name = "XRP",
            line_color = 'hotpink',
            opacity = 0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y=data['BNB'],
            name="BNB",
            line_color='maroon',
            opacity=0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y=data['LTC'],
            name="LTC",
            line_color='navy',
            opacity=0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y=data['EOS'],
            name="EOS",
            line_color='rosybrown',
            opacity=0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y=data['TRX'],
            name="TRX",
            line_color='turquoise',
            opacity=0.8
        ))
        graph1.add_trace(go.Scatter(
            x=data.index,
            y=data['BCH'],
            name="BCH",
            line_color='red',
            opacity=0.8
        ))
        graph1.update_layout(title_text = "Normalized closing price of Cryptocurrencies")
        graph1.show()

    #visualizefunc(data2)

binancePrice()


#New data gets added to the bottom and old data get removed from the top
"""
[
  [
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "17928899.62484339" // Ignore.
  ]
]
"""

