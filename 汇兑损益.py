
import pandas as pd
path = r'C:\Users\NE01471\Desktop\Python\副本Accounting核算基础表20230516.xlsx' # 文件路径，根据你的实际情况修改
sheet = '会计科目' # sheet名称，根据你的实际情况修改
df = pd.read_excel(path, sheet_name=sheet) # 读取Excel文件，返回一个DataFrame对象
print(df) # 打印DataFrame对象，查看数据
import numpy as np
pch = df['名称'] # 获取PCH列的数据
print(pch)
