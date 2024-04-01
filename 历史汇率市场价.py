import akshare as ak
import pandas as pd
from selenium import webdriver
import io
import numpy as np
from datetime import timedelta

# 提取收盘价数据
# Set up the web driver (make sure you have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()

url = "https://cn.investing.com/currencies/usd-cnh-historical-data"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Open the webpage
driver.get(url)

# Wait for user interaction to select the desired time interval manually
input("Please manually select the desired time interval on the webpage and press Enter when ready...")

# Proceed with the data extraction
response = driver.page_source

# 使用 io.StringIO 包装 HTML 字符串
html_stringio = io.StringIO(response)
tables = pd.read_html(html_stringio)

# 选择你需要的表格
table = tables[2]  # Assuming you want the second table (index 1)

# 选择前两列的数据并重命名
usd_cnh = table.iloc[:, :2]
usd_cnh = usd_cnh.rename(columns={'日期': '日期', '收盘': '收盘_usd_cnh'})

# Close the webdriver when done
driver.quit()

# 将数据导出到 Excel 文件
usd_cnh.to_excel('usd_cnh_data.xlsx', index=False)
print("Data has been exported to 'usd_cnh_data.xlsx'")
