import urllib.request
import _thread
import re
import ssl
import json
# 导入jieba模块，用于中文分词
import jieba
# 导入wordcount，用于制作词云图
from wordcloud import WordCloud, STOPWORDS
from flask import Flask
import matplotlib.pyplot as plt
import jieba.analyse
from time import sleep
from flask import render_template, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    # 初始化模版数据为空
    userinfo = {}
    # 如果是一个Post请求,并且有微博用户id,则获取微博数据并生成相应云图
    # request.method的值为请求方法
    # request.form既为提交的表单
    if request.method == 'POST' and request.form.get('uid'):
        uid = request.form.get('uid')
        userinfo = get_user_info(uid)
        posts = get_all_post(uid, userinfo['containerid'])
        # try:
        #     _thread.start_new_thread(ciyun, (posts,uid))
        # except:
        #     print("Error: 无法启动线程")
        #dest_img = ciyun(posts,uid)
        # userinfo['personas'] = dest_img
        print(userinfo)
    return render_template('index.html', **userinfo)




# 获取数据，根据url获取
def open_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0)Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    html=urllib.request.urlopen(req).read()
    return html






# 定义获取博主信息的函数
# 参数uid为博主的id

def get_user_info(uid):
    # 发送请求
    result = open_page('https://m.weibo.cn/api/container/getIndex?type=uid&value={}'.format(uid)).decode('utf-8', 'ignore')
    # print(result)
    # print(result.decode('utf-8'))


    json_data = json.loads(result)['data'] # 获取繁华信息中json内容
    userinfo = {
        'name': json_data['userInfo']['screen_name'],                    # 获取用户头像
        'description': json_data['userInfo']['description'],             # 获取用户描述
        'follow_count': json_data['userInfo']['follow_count'],           # 获取关注数
        'followers_count': json_data['userInfo']['followers_count'],     # 获取粉丝数
        'profile_image_url': json_data['userInfo']['profile_image_url'], # 获取头像
        'verified_reason': json_data['userInfo']['verified_reason'],     # 认证信息
        'containerid': json_data['tabsInfo']['tabs'][1]['containerid']   # 此字段在获取博文中需要
    }

    # 获取性别，微博中m表示男性，f表示女性
    if json_data['userInfo']['gender'] == 'm':
        gender = '男'
    elif json_data['userInfo']['gender'] == 'f':
        gender = '女'
    else:
        gender = '未知'
    userinfo['gender'] = gender
    return userinfo





def get_all_post(uid, containerid):

    #
    # 从第一页开始
    page = 0
    # 这个用来存放博文列表
    posts = []
    while page<1:
        print(page)
        # 请求博文列表
        result = open_page('https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid={}&page={}'
                              .format(uid, containerid, page)).decode('utf-8', 'ignore')
        # json_data = result.json()
        json_data = json.loads(result)['data']  # 获取评论信息中json内容
        # 当博文获取完毕，退出循环
        if not json_data['cards']:
            break

        # 循环将新的博文加入列表
        for i in json_data['cards']:
            try:
                posts.append(i['mblog']['text'])
            except Exception as e:
                print("error")

        # 停顿半秒，避免被反爬虫
        sleep(2)

        # for item in posts:
        #     with open('/Users/youpeng/zhizhi/weibo-comments.txt', 'a', encoding='utf-8') as f:
        #         f.write(str(item))

        # 跳转至下一页
        page += 1

        # print(posts)
    # 返回所有博文
    return posts



def ciyun (data_list,uid):
    comments = []
    # with open(wordspath, mode='r', encoding='utf-8') as f:
    #     rows = f.readlines()
    #     i = 0
    #     for row in rows:
    #         row=re.sub("[A-Za-z0-9\!\%\[\]\,\。\____\/]", "", row)
    #         comments.append(row)
    # data_list=re.sub("[A-Za-z0-9\!\%\[\]\,\。\____\/]", "", data_list)

    for row in data_list:
        row = re.sub("[A-Za-z0-9\!\%\[\]\,\。\____\/]", "", row)
        comments.append(row)
    # 设置分词
    comment_after_split = jieba.cut(str(comments), cut_all=False)  # 非全模式分词，cut_all=false
    words = ' '.join(comment_after_split)  # 以空格进行拼接
    # print(words)

    # 设置屏蔽词
    stopwords = STOPWORDS.copy()
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
    stopwords.add('微博')
    stopwords.add('还有')

    # 导入背景图
    bg_image = plt.imread('/users/youpeng/zhizhi/timg.jpg')

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
    print("ok")

    wc.generate_from_text(words)

    plt.imshow(wc)
    plt.axis('off')  # 不显示坐标轴
    #plt.show()

    dest_img = './static/{}.png'.format(uid)
    # 保存结果到本地
    #plt.savefig(dest_img)
    wc.to_file(dest_img)

    print("ok")
    return dest_img




if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消证书验证
    app.run()


    #userinfo = get_user_info('1350995007')
    #usercommnet=get_all_post('1350995007', '1076031350995007')
    #ciyun('/users/youpeng/zhizhi/weibo-comments.txt','/users/youpeng/zhizhi/timg.jpg','1350995007')
    userinfo={}
    uid=1350995007
    userinfo = get_user_info(uid)
    posts = get_all_post(uid, userinfo['containerid'])
    dest_img = ciyun(posts, uid)
    userinfo['personas'] = dest_img
    #print(usercommnet)
    # print(userinfo['name'])
    # print(userinfo['description'])
    # print(userinfo['follow_count'])
    # print(userinfo['profile_image_url'])
    # print(userinfo['verified_reason'])
    # print(userinfo['containerid'])
