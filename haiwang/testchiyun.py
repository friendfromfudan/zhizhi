# coding=utf-8
__author__ = '芝麻开心'

#这个博客是代码的原创，本人大部分的工作是搬砖http://www.cnblogs.com/mylovelulu/p/9511369.html

# 导入jieba模块，用于中文分词
import jieba
# 导入matplotlib，用于生成2D图形
import matplotlib.pyplot as plt
# 导入wordcount，用于制作词云图
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



if __name__ == '__main__':
    # 获取所有评论
    comments = []
    with open('/Users/youpeng/zhizhi/comments.txt', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        i=0
        for row in rows:
            i+=1
            print(i)
            comment = row.split(',')[3]
            if comment != '':
                comments.append(comment)

    # 设置分词
    comment_after_split = jieba.cut(str(comments), cut_all=False)  # 非全模式分词，cut_all=false
    words = ' '.join(comment_after_split)  # 以空格进行拼接
    print(words)

    # 设置屏蔽词
    stopwords = STOPWORDS.copy()
    stopwords.add('电影')
    stopwords.add('一部')
    stopwords.add('一个')
    stopwords.add('没有')
    stopwords.add('什么')
    stopwords.add('有点')
    stopwords.add('这部')
    stopwords.add('这个')
    stopwords.add('不是')
    stopwords.add('真的')
    stopwords.add('感觉')
    stopwords.add('觉得')
    stopwords.add('还是')
    stopwords.add('但是')
    stopwords.add('就是')
    stopwords.add('一出')

    stopwords.add('还有')

    # 导入背景图
    bg_image = plt.imread('/users/youpeng/zhizhi/bg.jpg')

    # 设置词云参数，参数分别表示：画布宽高、背景颜色、背景图形状、字体、屏蔽词、最大词的字体大小
    wc = WordCloud(
                   scale=4,
                   background_color='white',
                   mask=bg_image,
                   font_path='/System/Library/Fonts/PingFang.ttc',
                   stopwords=stopwords,
                   max_font_size=400,
                   random_state=50,
                   collocations=False
                   )
    # 将分词后数据传入云图
    wc.generate_from_text(words)
    plt.imshow(wc)
    plt.axis('off')  # 不显示坐标轴
    plt.show()
    # 保存结果到本地
    wc.to_file('词云图.jpg')
