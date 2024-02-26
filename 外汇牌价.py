import akshare as ak
import pandas as pd


currency_boc_sina_df = ak.currency_boc_sina(symbol="美元", start_date="20180901", end_date="20240222")

excel_file_path = '美元.xlsx'

currency_boc_sina_df.to_excel(excel_file_path)