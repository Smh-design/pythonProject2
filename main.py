# This is a sample Python script.
import data


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
path = r'C:\Users\NE01471\Desktop\Python\贷款台账-20231231.xlsx' # 文件路径，根据你的实际情况修改
sheet = '还本计划' # sheet名称，根据你的实际情况修改
df = pd.read_excel(path, sheet_name=sheet) # 读取Excel文件，返回一个DataFrame对象
print(df) # 打印DataFrame对象，查看数据
import numpy as np
pch = df['待还还本（本币）'] # 获取PCH列的数据
print(pch)
data = df # 读取Excel文件
table = pd.pivot_table(data, index="银行", columns="预估存入时间", values="待还还本（本币）", aggfunc="sum") # 按照银行和预估存入时间进行分组汇总
table = table.resample("Q", axis=1).sum() # 按照季度对列进行重采样
print(table) # 打印结果
table.to_excel("D:/result3.xlsx", sheet_name="data")