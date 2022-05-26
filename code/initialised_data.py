'''
----------------------------------------------
Project: Stock Market Analysis
File: initialsed_data.py
Description:

    extracts data from NSE website based on dates
    and stock symbol provided and stores into
    data folder
    
-----------------------------------------------
'''

import requests
from io import StringIO
import pandas as pd
from  datetime import datetime , timedelta
import bs4
import os
from utils import get_stock_dict, get_cols
import json

DATA_PATH = '../data/'

session = requests.session()

head = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}

def get_data(company, from_date, to_date):
    session.get("https://www.nseindia.com", headers=head)
    session.get("https://www.nseindia.com/get-quotes/equity?symbol=" + company, headers=head)
    session.get("https://www.nseindia.com/api/historical/cm/equity?symbol="+company, headers=head)
    url = "https://www.nseindia.com/api/historical/cm/equity?symbol=" + company + "&series=[%22EQ%22]&from=" + from_date + "&to=" + to_date + "&csv=true"
    webdata = session.get(url=url, headers=head)
    try:
        company_df = pd.read_csv(StringIO(webdata.text[3:]))
        return company_df
    except: 
        raise Exception("Cannot fetch data from NSE")

if __name__=='__main__':

    with open('config.json') as file:
        config_data = json.load(file)

    from_date = config_data['from_date']
    to_date = config_data['to_date']

    nifty_50_dict = get_stock_dict()
    nifty_50_list = list(nifty_50_dict.values())

    cols = get_cols()

    for stock_symbol in nifty_50_list:
        company_df = get_data(stock_symbol, from_date, to_date)
        company_df = company_df.rename(columns=cols)
        company_df.to_csv(DATA_PATH + stock_symbol + '.csv', index=False)