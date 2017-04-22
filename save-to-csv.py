#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import DataFrame
import pandas as pd
import tushare as ts
import os
from sqlalchemy import create_engine
filename = './hist.csv'
stock_info = ts.get_stock_basics()
for i in stock_info.index:
    df = ts.get_hist_data(i)
    idf=DataFrame(df)
    idf['num']=i  
    if os.path.exists(filename):
        try:
            idf.to_csv(filename,mode = 'a',header=None)
        except:
            continue
    else:
        idf.to_csv(filename)
