import akshare as ak
import pandas as pd
macro_china_lpr_df = ak.macro_china_lpr()

macro_china_lpr_df['TRADE_DATE'] = pd.to_datetime(macro_china_lpr_df['TRADE_DATE'])
print(macro_china_lpr_df)
start_date = pd.to_datetime('2023-01-20')
filtered_df = macro_china_lpr_df[(macro_china_lpr_df['TRADE_DATE'] == start_date)]
