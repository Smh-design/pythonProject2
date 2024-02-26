import pandas as pd
from datetime import timedelta

# Your file path and sheet name
path = r'C:\Users\NE01471\Desktop\Python\贷款台账-20231231.xlsx'
sheet = '还本计划'

# Read the Excel file into a DataFrame
df = pd.read_excel(path, sheet_name=sheet)

# Function to calculate interest based on the specified conditions
def calculate_interest(row):
    if '固定' in row['利率定价']:
        # Extract fixed interest rate from '固定' content
        interest_rate = float(row['利率定价'].split('固定')[1][:-1]) / 100
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
        return None  # Handle other cases accordingly

    # Calculate interest based on 结息方式
    if '季末' in row['结息方式']:
        interest_days = calculate_interest_days(row['提款日（以贷款明细为准）'], row['约定还款时间'], frequency='quarterly')
    elif '到期' in row['结息方式']:
        interest_days = calculate_interest_days(row['提款日（以贷款明细为准）'], row['约定还款时间'], frequency='once')
    elif '月末' in row['结息方式']:
        interest_days = calculate_interest_days(row['提款日（以贷款明细为准）'], row['约定还款时间'], frequency='monthly')
    else:
        return None  # Handle other cases accordingly

    # Calculate interest based on daily rate
    daily_rate = interest_rate / 360
    interest_amount = (interest_days * daily_rate) * row['待还还本（本币）']
    return interest_amount

# Function to calculate the number of interest days based on the specified frequency
def calculate_interest_days(start_date, end_date, frequency):
    # Implement your logic to calculate interest days based on the specified frequency
    # For demonstration purposes, returning a fixed value
    return 90

# Function to get LPR interest rate based on specified conditions
def get_lpr_interest_rate(date):
    # Implement your logic to get LPR interest rate based on date
    # For demonstration purposes, returning a fixed value
    return 4.55014 / 100

# Create a new column '利息' with calculated interest amounts
df['利息'] = df.apply(calculate_interest, axis=1)

# Print the DataFrame with selected columns and calculated interest amounts
selected_columns = ['银行', '待还还本（本币）', '利息']
selected_data = df[selected_columns]
print(selected_data)