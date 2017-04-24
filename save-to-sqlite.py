#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import DataFrame
import pandas as pd
import tushare as ts
from sqlalchemy import create_engine
import sqlalchemy
import os
stock_info = ts.get_stock_basics()
for i in stock_info.index:
    df = ts.get_hist_data(i)
    idf=DataFrame(df)
    idf['num']=i  
    engine=create_engine('sqlite:///stock.db',echo=False)
    try:
        idf.to_sql('hist_data',engine,if_exists='append') 
    except:
        continue


