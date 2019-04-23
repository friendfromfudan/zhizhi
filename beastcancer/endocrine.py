import urllib.request
import os
import ssl
import csv
from lxml import etree
import codecs

ssl._create_default_https_context = ssl._create_unverified_context

def open_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0)Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    html=urllib.request.urlopen(req).read()
    return html


def download_qa(page=360):
    i=1
    # 打开文件，追加a
    out = open('/Users/youpeng/study/practice/doctor.csv', 'a', newline='',encoding='utf-8-sig')

    qas=[]
    while i<41:
        print('Page', i)
        url = "http://www.mijian360.com/search/help/keyword/%E5%86%85%E5%88%86%E6%B3%8C%E6%B2%BB%E7%96%97/isBlur/1/p/"+str(i)+'html'
        html = open_page(url).decode('utf-8', 'ignore')
        html_data = etree.HTML(html)
        qa_list = html_data.xpath('/html/body/div[3]/div/div/div[3]/dl')
        for content in qa_list:

            data1=content.xpath('./dd/h3/a//text()')
            data2=content.xpath('./dd/p[1]//text()')
            print (data1)
            print (data2)
            info1=''.join(data1)
            info2=''.join(data2)
            print(info1)
            print(info2)
            qas.append(info1)
            qas.append(info2)
        i+=1

    for item in qas:
        with open('/Users/youpeng/zhizhi/beastcancer/qa.txt', 'a', encoding='utf-8') as f:
            f.write(str(item)+'\n')




if __name__ == "__main__":
    download_qa()
