import akshare as ak

currency_hist_df = ak.currency_hist(symbol="eur-gbp", period="每日", start_date="20180101", end_date="20240229")
print(currency_hist_df)