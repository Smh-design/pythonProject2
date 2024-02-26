import pandas as pd
import akshare as ak
from datetime import timedelta
# Your file path and sheet name
path = r'C:\Users\NE01471\Desktop\Python\贷款台账-20231231.xlsx'
sheet = '还本计划'

# Read the Excel file into a DataFrame
df = pd.read_excel(path, sheet_name=sheet)

selected_columns = ["银行",'利率定价', '利息计算方式', '结息方式', '提款日（以贷款明细为准）', '约定还款时间', '待还还本（本币）']

# 选取特定列
data = df[selected_columns]

filtered_data = df[df["银行"] == "中国银行"]
selected_filtered_data = filtered_data[selected_columns]

print(selected_filtered_data)

def calculate_interest(row):
    if '固定利率' in row['利率定价']:
        # Extract fixed interest rate from '固定' content
        interest_rate = float(row['利率定价'].split('固定利率')[1][:-1]) / 100
    elif '定价日' in row['利率定价']:
        # Calculate interest based on 1 year LPR + 0.0055
        interest_rate = 0.0455014
    elif '实际提款日和1年LPR+55BP' in row['利率定价']:
        # Calculate interest based on 1 year LPR + 0.0055
        lpr_date = max(row['约定还款时间'].replace(year=row['约定还款时间'].year - 1),
                       row['提款日（以贷款明细为准）'])
        interest_rate = get_lpr_interest_rate(lpr_date) + 0.0055
    elif 'LPR+30BP' in row['利率定价']:
        # Calculate interest based on 1 year LPR + 0.0030
        lpr_date = max(row['约定还款时间'].replace(year=row['约定还款时间'].year - 1),
                       row['提款日（以贷款明细为准）'])
        interest_rate = get_lpr_interest_rate(lpr_date) + 0.0030
    else:
        interest_rate = 0.0
    return interest_rate
selected_filtered_data.loc[:,'利率'] = filtered_data.apply(calculate_interest, axis=1)

print(selected_filtered_data)
