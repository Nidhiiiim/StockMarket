# Stock Market Analysis
A tool to analyse NSE Stock Data for Nifty 50 stocks

## Overview

- Automated data collection from NSE website for each business day
- Automated data quality checks to ensure correctness of the data
- Visualizations showing trends for the stock for 5 Day, 1 Month, 6 Months and 1 Year 

## Architecture Diagram
![Architecture Diagram](https://github.com/Nidhiiiim/StockMarket/blob/423bf5fa4f3106f63ace9a118335fb4cf0483974/images/architecture_diagram.png)

## Tech Stack
#### Python Libraries
- requests
- pandas
#### Database
- SQLite
#### Pipeline Orchestration 
- Apache Airflow
#### Web 
- Flask 
- HTML / CSS
- JavaScript

## Project Directory Structure

```
Stock_Market_Analysis
├─ .github
│  └─ ISSUE_TEMPLATE
│     ├─ feature-template.md
│     ├─ story-template.md
│     └─ task-template.md
├─ .gitignore
├─ code
│  ├─ backfill.py
│  ├─ config.json
│  ├─ current.py
│  ├─ holiday_check.py
│  ├─ utils.py
│  ├─ __init__.py
│  
├─ dags
├─ images
├─ README.md
├─ sql
│  ├─ holidays_ddl.sql
│  ├─ holidays_dml.sql
│  ├─ sectors_ddl.sql
│  ├─ sectors_dml.sql
│  ├─ stocks_ddl.sql
│  └─ stocks_dml.sql
├─ web
│  ├─ app.py
│  ├─ graph_utils.py
│  ├─ static
│  │  └─ styles
│  │     └─ style.css
│  ├─ templates
│  │  ├─ index.html
│  │  └─ results.html
│  ├─ test.db
│  ├─ __init__.py
│  
├─ __init__.py

```

## Files Description 
1. **config.json** - configuration file
2. **initialised_data.py** - extracts data from NSE website based on dates
and stock symbol provided and stores into data folder
3. **current_data.py** -  extracts data from NSE website for current date 
and writes it into data folder for the corresponding stock 
4. **holiday_check.py** - checks whether current date is a sunday, monday 
or a bank holiday
5. **data_quality_check.py** - performs the following checks:-
    - row count check
    - null values check
    - check if data is populated for current date
6. **back_fill.py** -  loads data for the time period 1st Jan 2015 to 
31st Dec 2021 into the data folder
7. **get_daily_data_dag.py** - DAG which runs from Tuesday to Saturday 
at 8 AM IST in order to extracts data from NSE website
8. **graph_utils.py** - helper functions used frequently for the 
purpose of plotting visualizations


## Setup


## License
MIT
