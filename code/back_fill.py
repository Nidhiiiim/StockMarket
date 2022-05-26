'''
----------------------------------------------
Project: Stock Market Analysis
File: backfill.py
Description:
    
    loads data for the time period 1st Jan 2015
    to 31st Dec 2021 into the data folder
    
-----------------------------------------------
'''

import pandas as pd 
from initialised_data import get_data
from utils import get_stock_dict, get_cols, convert_to_date
from datetime import datetime

DATA_PATH = '../data/'

def consolidate_data(stock_symbol):
    df = get_data(stock_symbol, from_date='01-01-2015', to_date='31-12-2016')
    df = df.rename(columns=cols)
    
    df1 = get_data(stock_symbol, from_date='01-01-2017', to_date='31-12-2018')
    df1 = df1.rename(columns=cols)
    
    df2 = get_data(stock_symbol, from_date='01-01-2019', to_date='31-12-2020')
    df2 = df2.rename(columns=cols)
    
    df3 = get_data(stock_symbol, from_date='01-01-2021', to_date='31-12-2021')
    df3 = df3.rename(columns=cols)
    
    df4 = df.append(df1, ignore_index=True)
    df5 = df4.append(df2, ignore_index=True)
    df6 = df5.append(df3, ignore_index=True)
    
    df6.to_csv(DATA_PATH + stock_symbol + '.csv', index=False)


def transform_data(stock_symbol):
    df = pd.read_csv(DATA_PATH + stock_symbol + '.csv')
    
    df = convert_to_date(df)
    df = df.sort_values('date')
    
    df.to_csv(DATA_PATH + stock_symbol + '.csv', index=False)
    

if __name__=='__main__':

    nifty_50_dict = get_stock_dict()
    nifty_50_list = list(nifty_50_dict.values())

    cols = get_cols()

    for stock_symbol in nifty_50_list:
        consolidate_data(stock_symbol)
        transform_data(stock_symbol)