'''
----------------------------------------------
Project: Stock Market Analysis
File: current.py
Description:
    
    extracts data from NSE website for current
    date and writes it into data folder for 
    the corresponding stock 
    
-----------------------------------------------
'''

import os
from datetime import timedelta , date , datetime
from csv import writer 
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from initialised_data import get_data
from utils import get_stock_dict, convert_to_date

TODAY_DATE = datetime.today() #date(2021,12,29)
CURRENT_DATE = TODAY_DATE - timedelta(1)
PREVIOUS_DATE = CURRENT_DATE - timedelta(3)

STR_CURRENT_DATE = CURRENT_DATE.strftime("%d-%m-%Y")
STR_PREVIOUS_DATE = PREVIOUS_DATE.strftime("%d-%m-%Y")

DATA_PATH = '../data/'

if __name__=='__main__':

    nifty_50_dict = get_stock_dict()
    nifty_50_list = list(nifty_50_dict.values())

    for stock_symbol in nifty_50_list:
        try:
            company_df = get_data(stock_symbol,from_date=STR_PREVIOUS_DATE,to_date=STR_CURRENT_DATE)

            current_record = company_df.head(1) 
            current_record = current_record.values.flatten().tolist()
            
            file_name = DATA_PATH + stock_symbol + '.csv'
            
            with open(file_name,'a') as file:
                writer_object = writer(file)
                writer_object.writerow(current_record)
                file.close()

            company_df = pd.read_csv(DATA_PATH + stock_symbol + '.csv')
            company_df = company_df.append(current_record)
            
            company_df = convert_to_date(company_df)
            company_df = company_df.sort_values(by=['date'])

            company_df.to_csv(DATA_PATH + stock_symbol + '.csv', index=False)

        except:
            raise Exception("Data for date {} cannot be fetched from NSE".format(STR_CURRENT_DATE))

