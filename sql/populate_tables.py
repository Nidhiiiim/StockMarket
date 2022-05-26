'''
-----------------------------------------------
Project: Stock Market Analysis
File: populate_tables.py
Description:

    reads query from file, creates schemas 
	for tables and populates data
    
-----------------------------------------------
'''

from datetime import datetime, date 
import sqlite3
import json

conn = sqlite3.connect('../web/test.db')
cursor = conn.cursor()

def open_file(file_name):
    f = open(file_name, "r")
    query = f.read()
    return query

def sql_create(table_name):
    table_ddl = table_name + '_ddl.sql'
    query = open_file(table_ddl)
        
    cursor.execute(query)
    
def sql_insert(table_name):
    table_dml = table_name + '_dml.sql'
    query = open_file(table_dml)
    
    cursor.execute(query)
    cursor.execute('COMMIT;')

if __name__ == '__main__':

    with open('../code/config.json') as file:
        config_data = json.load(file)

    holiday_tbl_name = config_data['holiday_tbl_name']
    sector_table_name = config_data['sector_tbl_name']
    stock_tbl_name = config_data['stock_tbl_name']

    sql_create(holiday_tbl_name)
    sql_create(stock_tbl_name)
    sql_create(sector_table_name)

    sql_insert(holiday_tbl_name)
    sql_insert(stock_tbl_name)
    sql_insert(sector_table_name)
