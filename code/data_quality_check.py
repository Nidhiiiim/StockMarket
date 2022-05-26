'''
----------------------------------------------
Project: Stock Market Analysis
File: data_quality_check.py
Description:
    
    performs the following checks:-
    - row count check
    - null values check
    - check if data is populated for current date
    
-----------------------------------------------
'''

from datetime import datetime, date, timedelta
import pandas as pd
from utils import get_stock_dict

TODAY_DATE = datetime.today() #date(2021,12,24)
CURRENT_DATE = TODAY_DATE - timedelta(1)
STR_CURRENT_DATE = CURRENT_DATE.strftime('%Y-%m-%d')

DATA_PATH = '../data/'

def check_row_count(nifty_50_list):
    for stock in nifty_50_list:
        df = pd.read_csv(DATA_PATH + stock + '.csv')

        if len(df) > 0:
            print("Row count check is successful")

        else:
            raise Exception("Row count check has failed")

def check_null_values(nifty_50_list):
    for stock in nifty_50_list:
        df = pd.read_csv(DATA_PATH + stock + '.csv') 

        if df.isnull().values.any() == False:
            print("No null values found")

        else:
            raise Exception("There are null values in data")

def check_data_for_current_date(nifty_50_list):
    for stock in nifty_50_list:
        df = pd.read_csv(DATA_PATH + stock + '.csv') 
        df = df[ df['date'] == STR_CURRENT_DATE ]

        if len(df) > 0: 
            print("Data for date {} is populated".format(CURRENT_DATE))

        else:
            raise Exception("Date for date {} is not populated".format(CURRENT_DATE))


if __name__=='__main__':

    nifty_50_dict = get_stock_dict()
    nifty_50_list = list(nifty_50_dict.keys())

    check_row_count(nifty_50_list)
    check_null_values(nifty_50_list)
    check_data_for_current_date(nifty_50_list)