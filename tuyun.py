import pandas as pd
import re
import jieba
import numpy as np
import wordcloud as wc
import matplotlib.pyplot as plt
from PIL import Image
from numpy import array


if __name__ == '__main__':
    data = pd.read_csv('/Users/youpeng/zhizhi/movie.csv')
    text = ''
    for i in data['text']:
        text += (str(i))

    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    texts = re.findall(pattern, text)
    cleaned_texts = ''.join(texts)

    segment = jieba.lcut(cleaned_texts)
    alldata = ''
    for i in segment:
        alldata = alldata + ' ' + str(i)

    pic = Image.open('/Users/youpeng/zhizhi/douban.jpg')
    picarray = array(pic)
    mywc = wc.WordCloud(collocations=False, font_path='/System/Library/Fonts/PingFang.ttc', mask=picarray, background_color='black').generate(alldata)
    fig = plt.figure(figsize=(14, 10))
    plt.imshow(mywc)
    plt.axis('off')
    plt.show()