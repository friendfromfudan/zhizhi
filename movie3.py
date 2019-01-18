import tushare as ts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def get_tushare_data(data):
    '''获取tushare月度票房数据'''
    df = ts.month_boxoffice(data)
    return df
data = ['2018-10','2018-9','2018-8','2018-7','2018-6','2018-5','2018-4','2018-3','2018-2','2018-1']
rm = []
for i in data:
    df = get_tushare_data(i)
    rm.append(df)
res = pd.concat(rm, axis=0, ignore_index=True)#合并所有月份数据
df = pd.DataFrame(res)#转换dataframe
df.head(2)