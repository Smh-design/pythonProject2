# 导入需要的库
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义一个函数，用来从给定的网址中抓取电池产品的信息
def get_battery_info(url):
    # 发送请求，获取网页内容
    response = requests.get(url)
    # 判断是否请求成功
    if response.status_code == 200:
        # 解析网页内容，使用lxml解析器
        soup = BeautifulSoup(response.text, 'lxml')
        # 找到包含电池产品信息的div标签
        div = soup.find('div', class_='product-list')
        # 判断是否找到了div标签
        if div:
            # 创建一个空列表，用来存储电池产品的信息
            battery_list = []
            # 找到所有的li标签，每个li标签对应一个电池产品
            lis = div.find_all('li')
            # 遍历每个li标签
            for li in lis:
                # 创建一个空字典，用来存储一个电池产品的信息
                battery = {}
                # 找到电池产品的名称，存储在字典中
                name = li.find('h3').text.strip()
                battery['name'] = name
                # 找到电池产品的类型，存储在字典中
                type = li.find('p', class_='type').text.strip()
                battery['type'] = type
                # 找到电池产品的特点，存储在字典中
                feature = li.find('p', class_='feature').text.strip()
                battery['feature'] = feature
                # 找到电池产品的应用领域，存储在字典中
                application = li.find('p', class_='application').text.strip()
                battery['application'] = application
                # 将字典添加到列表中
                battery_list.append(battery)
            # 返回列表
            return battery_list
        else:
            # 如果没有找到div标签，返回空列表
            return []
    else:
        # 如果请求失败，返回空列表
        return []

# 定义一个网址，用来抓取宁德时代的电池产品信息
url = 'http://www.catl.com/'
# 调用函数，获取电池产品信息
battery_list = get_battery_info(url)
# 判断是否获取到了电池产品信息
if battery_list:
    # 将列表转换为数据框，方便查看和保存
    df = pd.DataFrame(battery_list)
    # 打印数据框
    print(df)
    # 保存数据框为csv文件
    df.to_csv('battery_info.csv', index=False)
else:
    # 如果没有获取到电池产品信息，打印提示信息
    print('没有找到电池产品信息')

