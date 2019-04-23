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
    with open('/Users/youpeng/zhizhi/beastcancer/qas.txt', mode='r', encoding='utf-8') as f:
        rows = f.readlines()
        i=0
        for row in rows:
            comments.append(row)

    # 设置分词
    jieba.suggest_freq('他莫昔芬', True)
    jieba.suggest_freq('他莫西芬', True)
    jieba.suggest_freq('它莫昔芬', True)
    jieba.suggest_freq('阿那曲唑', True)
    jieba.suggest_freq('诺雷德', True)
    jieba.suggest_freq('导管癌', True)
    jieba.suggest_freq('赫赛汀', True)
    jieba.suggest_freq('戈舍瑞林', True)




    comment_after_split = jieba.cut(str(comments), cut_all=False)  # 非全模式分词，cut_all=false

    words = ' '.join(comment_after_split)  # 以空格进行拼接
    print(words)

    # 设置屏蔽词
    stopwords = STOPWORDS.copy()
    stopwords.add('姐妹')
    stopwords.add('可以')
    stopwords.add('开始')
    stopwords.add('你们')
    stopwords.add('知道')
    stopwords.add('就行')
    stopwords.add('互助')
    stopwords.add('医生')
    stopwords.add('内分泌')
    stopwords.add('治疗')
    stopwords.add('什么')
    stopwords.add('现在')
    stopwords.add('请问')
    stopwords.add('需要')
    stopwords.add('乳腺癌')
    stopwords.add('期间')
    stopwords.add('患者')
    stopwords.add('提问')
    stopwords.add('您好')
    stopwords.add('结果')
    stopwords.add('还是')
    stopwords.add('谢谢')
    stopwords.add('所以')
    stopwords.add('因为')
    stopwords.add('莫昔芬')
    stopwords.add('莫西芬')
    stopwords.add('最近')
    stopwords.add('结束')
    stopwords.add('导管')
    stopwords.add('目前')
    stopwords.add('但是')
    stopwords.add('然后')
    stopwords.add('这样')
    stopwords.add('这种')
    stopwords.add('曲唑')
    stopwords.add('如果')
    stopwords.add('戈舍')

    # 导入背景图
    bg_image = plt.imread('/Users/youpeng/zhizhi/beastcancer/timg.jpg')

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
    wc.to_file('/Users/youpeng/zhizhi/beastcancer/endocrine.jpg')
