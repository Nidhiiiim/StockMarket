'''
----------------------------------------------
Project: Stock Market Analysis
File: utils.py
Description:
    
    helper functions used frequently in other
    scripts
    
-----------------------------------------------
'''

from datetime import datetime, date, timedelta
import plotly
import plotly.express as px


def get_cols():
    cols = {'Date ': 'date', 'series ': 'series', 'OPEN ': 'open', 'HIGH ': 'high', 
            'LOW ': 'low', 'PREV. CLOSE ': 'prev_close', 'ltp ': 'ltp', 'close ': 'close', 
            'vwap ': 'vwap', '52W H ': '52wh', '52W L ': '52wl', 'VOLUME ': 'volume', 
            'VALUE ': 'value', 'No of trades ': 'no_of_trades'}

    return cols 


def convert_to_date(df):
    for i in range(0,len(df)):
        df['date'][i] = datetime.strptime(df['date'][i], '%d-%b-%Y').date()
    return df

def convert_to_string(df):
    for i in range(0,len(df)):
        df['date'][i] = df['date'][i].strftime('%d-%b-%Y')
    return df
 
def get_stock_dict():
    nifty_50_dict = {
                        'ADANIPORTS' : 'ADANIPORTS' ,
                        'ASIANPAINT' : 'ASIANPAINT',
                        'AXISBANK' : 'AXISBANK',
                        'BAJAJ-AUTO' : 'BAJAJ-AUTO',
                        'BAJAJFINSV' : 'BAJAJFINSV',
                        'BAJFINANCE' : 'BAJFINANCE',
                        'BHARTIARTL' : 'BHARTIARTL',
                        'BPCL' : 'BPCL',
                        'BRITANNIA' : 'BRITANNIA' ,
                        'CIPLA' : 'CIPLA',
                        'COALINDIA' : 'COALINDIA' ,
                        'DIVISLAB' : 'DIVISLAB' ,
                        'DRREDDY' : 'DRREDDY' ,
                        'EICHERMOT' : 'EICHERMOT',
                        'GRASIM' : 'GRASIM' ,
                        'HCLTECH' : 'HCLTECH' ,
                        'HDFC' : 'HDFC' ,
                        'HDFCBANK' : 'HDFCBANK',
                        'HDFCLIFE' : 'HDFCLIFE',
                        'HEROMOTOCO' : 'HEROMOTOCO',
                        'HINDALCO' : 'HINDALCO',
                        'HINDUNILVR' : 'HINDUNILVR',
                        'ICICIBANK' : 'ICICIBANK',
                        'INDUSINDBK' : 'INDUSINDBK',
                        'INFY' : 'INFY',
                        'IOC' : 'IOC' ,
                        'ITC' : 'ITC',
                        'JSWSTEEL' : 'JSWSTEEL',
                        'KOTAKBANK' : 'KOTAKBANK' ,
                        'LT' : 'LT' ,
                        'M&M' : 'M%26M',
                        'MARUTI' : 'MARUTI',
                        'NESTLEIND' : 'NESTLEIND',
                        'NTPC' : 'NTPC',
                        'ONGC' : 'ONGC' ,
                        'POWERGRID' : 'POWERGRID',
                        'RELIANCE' : 'RELIANCE',
                        'SBILIFE' : 'SBILIFE' ,
                        'SBIN' : 'SBIN',
                        'SHREECEM' : 'SHREECEM',
                        'SUNPHARMA' : 'SUNPHARMA',
                        'TATACONSUM' : 'TATACONSUM' ,
                        'TATAMOTORS' : 'TATAMOTORS',
                        'TATASTEEL' : 'TATASTEEL' ,
                        'TCS' : 'TCS',
                        'TECHM' : 'TECHM',
                        'TITAN' : 'TITAN',
                        'ULTRACEMCO' : 'ULTRACEMCO',
                        'UPL' : 'UPL',
                        'WIPRO'  : 'WIPRO'
                    }

    return nifty_50_dict


