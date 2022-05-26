'''
----------------------------------------------
Project: Stock Market Analysis
File: holiday_check.py
Description:
    
    checks whether current date is a sunday,
    monday or a bank holiday
    
-----------------------------------------------
'''

from datetime import datetime, date, timedelta
import sqlite3
import json


TODAY_DATE = datetime.today()
CURRENT_DATE = TODAY_DATE - timedelta(1)
DAY = CURRENT_DATE.strftime("%A")
STR_CURRENT_DATE = CURRENT_DATE.strftime("%Y-%m-%d")


def is_bank_holiday(holiday_tbl_name, current_date):
    conn = sqlite3.connect('../web/test.db')
    cursor = conn.cursor()

    query = ''' SELECT * FROM {holiday_tbl_name} '''.format(holiday_tbl_name=holiday_tbl_name)

    cursor.execute(query)

    result = cursor.fetchall();

    for i in range(0,len(result)):
        if current_date in result[i][0]:
            flag = True
            break
        else:
            flag = False

    return flag 


if __name__=='__main__':

    with open('config.json') as file:
        config_data = json.load(file)

    holiday_tbl_name = config_data['holiday_tbl_name']

    is_bank_holiday = is_bank_holiday(holiday_tbl_name, STR_CURRENT_DATE)

    if DAY.lower() == 'monday' or DAY.lower() == 'sunday' or is_bank_holiday:
        raise Exception("DAG cannot be scheduled today")

    else:
        print("DAG can be scheduled today")