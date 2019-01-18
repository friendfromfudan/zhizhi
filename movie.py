## python的数据分析实战：全年电影数据分析

#### 一、题目及要求
#
# - 数据初步挖掘和分析：
# - 做一份电影数据分析，通过对2018全年的电影数据获取进行分析和探索
# - 1).票房最高的电影Top10
# - 2).人气最高的电影Top10
# - 3).性价比最好的电影(根据价格，时长和口碑指数)
# - 4).统计每个月有多少上映的电影数量，找出淡季和旺季
# #### 二、搭建环境
# - python：2.7.15
# - tushare：0.4.3获取了1~11月月度电影csv文件保存在本地
#### 三、代码


import tushare as ts
import time
import pandas as pd
import numpy as np
from pyecharts import Funnel
from pyecharts import Pie
from pyecharts import Bar
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')


def Today():
    today = time.time() # 输出的是时间戳
    struct_time = time.localtime(today)  # 作用是格式化时间戳为本地的时间
    strft_time = time.strftime('%Y-%m-%d', struct_time)
    print(type(strft_time),strft_time)
    return strft_time

#1.合并月度票房记录
def get_movieData(date):
    date_list = date.split('-')
    print (date.split('-'))
    month = date_list[1]
    movie_data = []
    for i in range(1,int(month)+1):
        print ("生成%i月的月度票房"%i)
        #1.1 分月抓取电影月度数据
        p_mon = '2018-'+str(i)
        pro = ts.pro_api('8b3691c5ca767ea4a6efe770721b7d6681897aa7cb132b5f9fff746c')
        df = pro.bo_monthly(date=p_mon)
        #df = ts.month_boxoffice(p_mon)#老库v0.4.3
        #1.2 新增一行记录是属于哪个月的数据
        df.insert(0, 'p_mon', p_mon)
        #1.3 删除“其他”数据,找到第11行，确认删除数据inplace=True
        df.drop(df.index[10], inplace=True)
        movie_data.append(df)
        #print type(df), df
    #合并多个df
    result = pd.concat(movie_data,ignore_index=True)
    return result

#2.对表头重命名;数据 排序 去重等
def handle_df(df):
    #2.1 表头英文名转换中文
    df.rename(columns={'p_mon':u'月分区','Irank':u'月内排名','MovieName': u'电影名称',
                       'WomIndex': u'口碑指数','avgboxoffice': u'平均票价',
                       'avgshowcount': u'场均人次', 'box_pro': u'月度占比',
                       'boxoffice': u'单月票房(万)', 'days': u'月内天数',
                       'releaseTime': u'上映日期'},inplace=True)
    return df
    #print df
    #df.to_csv('G://Movie.csv')

    #isDup_movieName = df.duplicated(['MovieName'])
    #print isDup_movieName

# 3.对电影名称分组，求和票房（变相去重）
def moive_boxoffice_sort(df):
    #3.1 修改票房的数据结构为float，便于技术
    print (df.dtypes)
    #df.apply(pd.to_numeric, errors='ignore')
    df['month_amount'] = df['month_amount'].astype('float')
    #df[u'单月票房(万)'] = df.apply(pd.to_numeric, errors='ignore')

    #3.2 用电影名称作为分组 然后求和票房,重新生成index
    group_df = df.groupby('name',as_index=False)['month_amount'].sum()
    #print df.dtypes
    #3.3 对票房降序
    #group_df.sort(columns = [u'单月票房(万)'],axis = 0,ascending = False)
    group_df = group_df.sort_values(by='month_amount',ascending=False)
    #group_df.rank(ascending = False,method='max')
    movie_top10 = group_df.head(10).reset_index(drop = True)
    print(movie_top10)
    print('开始绘制电影top10漏斗图')
    # for i in range(0,10):
    #     new = movie_top10.loc[i,'month_amount']
    #     temp = new/(10000.00)
    #     movie_top10.iloc[i, 1] = temp
    # print movie_top10

    draw_Funnel(movie_top10)

def draw_Funnel(df):
    attr = df['name'].values.tolist()
    name = []  # 电影名称
    for x in attr:
        name.append(x.encode('utf-8'))
    print(len(name), name)
    v1 = df['month_amount'].values.tolist()
    month_amount = []  # 电影口碑指数
    for x in v1:
        month_amount.append(float('%.2f' % (x/10000.0)))
    print(len(month_amount), month_amount)
    #1. 初始化图形参数
    funnel = Funnel('2018年度电影Top10', width=800, height=600, title_pos='center')
    funnel.add('电影名称',name ,month_amount , is_label_show=True,label_pos="inside",label_formatter='{b}:{c}亿', legend_orient='vertical', legend_pos='left')
    funnel.render()
    print('电影top10漏斗图绘制完成')

# 4.对电影名称分组，排序口碑
def movie_favorite_sort(df):
    #1.名称去重 场均人次保留最大值
    group_favorite = df.groupby(['name'], as_index=False)['p_pc'].max().sort_values(by='p_pc', ascending=False)
    print('开始绘制2018年电影人气top10图')
    movie_favorite = group_favorite.head(15).reset_index()
    print(movie_favorite)
    draw_Pie(movie_favorite)

def draw_Pie(df):
    attr1 = df['name'].values.tolist()
    print(len(attr1))
    name = []
    for x in attr1:
        name.append(x.encode('utf-8'))
    print(len(name),name)
    att2r = df['p_pc'].values.tolist()
    p_pc = []
    for x in att2r:
        p_pc.append(int(x))
    print(len(p_pc),p_pc)

    pie = Pie("2018年电影人气Top15", title_pos='center', width=1000)
    pie.add(
        "电影场均人次：人/场",
        name,
        p_pc,
        center=[50, 50],
        is_random=True,
        radius=[30, 75],
        rosetype="area",
        is_legend_show=False,
        is_label_show=True,
    )
    pie.render()

# 5.性价比最好的电影(根据价格，时长和口碑指数)
def movie_highPerformance_ratio(df):
    list_day_df = df.groupby('name', as_index=False)['list_day'].sum()
    #去空值
    df['wom_index'] = df['wom_index'].replace(np.nan, 0)
    index_price_df = df.groupby('name', as_index=False)['wom_index','avg_price'].mean()
    print(index_price_df)
    result_df = pd.merge(list_day_df, index_price_df, on='name')
    result_df.insert(4, 'score', 0)
    #合并清洗后的列并添加一行 结果列
    print(result_df)
    for index, row in result_df.iterrows():
        #口碑占比8 上映天数占比1 价格占比1
        score = ((row["wom_index"]-7.0)/7.0*7) + ((row["list_day"]-30.0)/30.0*1)+(35.0-row["avg_price"]/35.0*2)
        score_result =  float('%.2f'%(score))
        result_df.iloc[index, 4] = score_result
    high_per_df = result_df.sort_values(by='score', ascending=False).reset_index(drop=True)
    draw_Bar(high_per_df.head(10))
def draw_Bar(df):
    bar = Bar("2018年性价比最高的电影Top10")
    attr = df['name'].values.tolist()
    name = [] # 电影名称
    for x in attr:
        name.append(x.encode('utf-8'))
    print(len(name),name)
    v1 = df['wom_index'].values.tolist()
    wom_index = [] # 电影口碑指数
    for x in v1:
        wom_index.append(float('%.2f'%x))
    print(len(wom_index),wom_index)
    v2 = df['list_day'].values.tolist()
    list_day = []  # 电影上映天数
    for x in v2:
        list_day.append(float('%.2f'%x))
    print(len(list_day), list_day)
    v3 = df['avg_price'].values.tolist()
    avg_price = []  # 电影口碑指数
    for x in v3:
        avg_price.append(float('%.2f'%x))
    print(len(avg_price), avg_price)
    v4 = df['score'].values.tolist()
    score = []  # 电影平均票价
    for x in v4:
        score.append(float('%.2f'%x))
    print(len(score), score)

    bar.add("电影综合评分", name, score, mark_point=["min", "average","max"],xaxis_rotate=15, yaxis_rotate=15,is_label_show=True,xaxis_line_color="blue",xaxis_line_width=1,xaxis_label_textcolor="orange",yaxis_label_textcolor="pink",bargap=10)
    #bar.add("电影口碑指数", name, wom_index, mark_line=["min", "max"],is_datazoom_show=True)
    # bar.add("电影上映天数", name, list_day, mark_point=["min", "max"],is_datazoom_show=True)
    # bar.add("电影平均票价", name, avg_price, mark_point=["min", "max"],is_datazoom_show=True)
    bar.render()


# 6.统计每个月有多少上映的电影数量，找出淡季和旺季
def movie_hotMonth(df):
    #统计每个月的总票房数
    month_movie = df.groupby('date', as_index=False)['month_amount'].sum().sort_values(by='month_amount', ascending=False).reset_index(drop=True)
    for index,row in month_movie.iterrows():
        month = row['date'].split('-')[1]
        #年份清洗，留下月份
        month_movie.iloc[index, 0] = month
    print(month_movie)
    draw_Pie_hotMonth(month_movie)
    draw_Bar_hotMonth(month_movie)


def draw_Pie_hotMonth(df):
    attr = df['date'].values.tolist()
    date = [] #月份
    for x in attr:
        date.append((str(x)+u'月').encode('utf-8'))
    print(len(date),date)
    v1 = df['month_amount'].values.tolist()
    month_amount = [] # 月份总票房
    for x in v1:
        month_amount.append(float('%.2f'%x))
    print(len(month_amount),month_amount)
    pie = Pie("2018年电影淡季和旺季-饼图", title_pos='center')
    pie.add(
        "当月总票房",
        date,
        month_amount,
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
        is_legend_show=False
    )
    pie.render()

def draw_Bar_hotMonth(df):
    attr = df['date'].values.tolist()
    date = [] # 电影月份
    for x in attr:
        date.append((str(x)+u'月').encode('utf-8'))
    print(len(date),date)
    v1 = df['month_amount'].values.tolist()
    month_amount = [] # 当月票房
    for x in v1:
        month_amount.append(float('%.2f'%(x/10000.0)))
    print(len(month_amount),month_amount)
    bar = Bar("2018年电影淡季和旺季-柱状图")
    bar.add("当月总票房:亿", date, month_amount,mark_point=["min", "average","max"])
    bar.render('Bar.html')

#  单进程
if __name__ == '__main__':
    #0.读取本地csv--库用不了的时候



    df2 = pd.read_csv('/Users/youpeng/movie.csv')
    #1.获取拼接月度票房csv,为处理
    # df1 = get_movieData(Today())
    # print (type(df2),df2)
    # print (type(df2),df2)
    # #2.更改表头
    # df2 = handle_df(df1)
    #
    # #3.获取2018年度电影票房top10并画图
    # moive_boxoffice_sort(df2)
    #
    # #4.获取2018年年度电影人气top10并画图
    # movie_favorite_sort(df2)
    #
    # #5.获取2018年年度电影性价比最好的电影(根据价格，时长和口碑指数)并画图
    # movie_highPerformance_ratio(df2)
    #
    # #6.统计每个月有多少上映的电影数量，找出淡季和旺季
    # movie_hotMonth(df2)
    #
    # df.to_csv('/Users/youpeng/Movie.csv')





