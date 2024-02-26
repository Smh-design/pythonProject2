import akshare as ak
import pandas as pd

currency_boc_safe_df = ak.currency_boc_safe()
print(currency_boc_safe_df)
currency_boc_safe_df['日期'] = pd.to_datetime(currency_boc_safe_df['日期'])

start_date = pd.to_datetime('2018-01-01')

target_currencies = ["美元","欧元","日元"]

filtered_df = currency_boc_safe_df[(currency_boc_safe_df['日期'] >= start_date)]

monthly_first_last_df = filtered_df.groupby(filtered_df['日期'].dt.to_period("M")).agg({'日期': ['first', 'last'], '美元': ['first', 'last'], '欧元': ['first', 'last'], '日元': ['first', 'last']})
# Reset index to make the result more readable
# Export the result to Excel
monthly_first_last_df.reset_index(drop=True, inplace=True)
excel_file_path = 'monthly_first_last_data.xlsx'

monthly_first_last_df.to_excel(excel_file_path)