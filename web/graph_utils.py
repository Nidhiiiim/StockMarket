'''
----------------------------------------------
Project: Stock Market Analysis
File: graph_utils.py
Description:

    helper functions used frequently for the
    purpose of plotting visualizations
    
-----------------------------------------------
'''

import plotly
import plotly.express as px
from datetime import datetime, date, timedelta

current_date = datetime.today()

def plot_graph(df):
    fig = px.line(df, x='date', y='close')
    return fig

def get_previous_trading_day(day_delta):
    previous_date = current_date - timedelta(day_delta)
    shift = timedelta(max(1,(previous_date.weekday() + 6) % 7 - 3))
    previous_date = previous_date - shift
    return previous_date

def filter_dataframe(previous_date, df):
    df = df[(df['date'] > previous_date) & (df['date'] <= current_date)]
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