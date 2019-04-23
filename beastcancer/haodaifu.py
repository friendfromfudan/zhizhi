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
    num=0
    qas=[]
    while i<101:
        print('Page', i)
        url = "https://so.haodf.com/all.php?kw=%E4%B9%B3%E8%85%BA%E7%99%8C%E5%86%85%E5%88%86%E6%B3%8C%E6%B2%BB%E7%96%97&page="+str(i)
        html = open_page(url).decode('utf-8', 'ignore')
        html_data = etree.HTML(html)
        qa_list = html_data.xpath('/html/body/div[1]/div[3]/div')
        for content in qa_list:

            data1=content.xpath('./div[2]/span/text()')


            if "申请" not in data1[0] :
                print (data1[0])
                qas.append(data1[0])
                num+=1
        i+=1
    print (num)
    for item in qas:
        with open('/Users/youpeng/zhizhi/beastcancer/haodaifu.txt', 'a', encoding='utf-8') as f:
            f.write(str(item)+'\n')



if __name__ == "__main__":
    download_qa()
