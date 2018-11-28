#/usr/bin/env python3
import urllib.request
import os
import ssl
import csv
import codecs

ssl._create_default_https_context = ssl._create_unverified_context

def open_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0)Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    html=urllib.request.urlopen(req).read()
    return html

# def get_page(url):
#     html=open_page(url).decode('utf-8')
#     a=html.find('page.cur')+10
#     return html[a]

def download_doctor(page=360):
    i=0
    # 打开文件，追加a
    out = open('/Users/youpeng/study/practice/doctor.csv', 'a', newline='',encoding='utf-8-sig')
    # 设定写入模式
    csv_write = csv.writer(out, dialect='excel')

    while i<361:
        print('Page', i)
        url = "https://www.haodf.com/jibing/ruxianai/daifu_all_all_all_all_all_"+str(i)+".htm"
        html = open_page(url).decode('gb2312', 'ignore')
        a = html.find('个人网站')
        while a != -1:
            doc_card = []
            doc_start = html.find('blue_a3', a, a + 500) + 9
            doc_end = html.find('</a>', doc_start, doc_start + 100)
            tittle_start = html.find('ml15', doc_end, doc_end + 500) + 6
            tittle_end = html.find('</span>', tittle_start, tittle_start + 300)
            # print(doc_start, doc_end)
            hosp_start = html.find('ml10', doc_end, doc_end + 500) + 6
            hosp_end = html.find('</span>', hosp_start, hosp_start + 300)
            # print(hosp_start, hosp_end)（
            print('医生:', html[doc_start:doc_end])
            doc_card.append(html[doc_start:doc_end])
            print('医院:', html[hosp_start:hosp_end])
            doc_card.append(html[hosp_start:hosp_end])
            print('职称:', html[tittle_start:tittle_end])
            doc_card.append(html[tittle_start:tittle_end])
            csv_write.writerow(doc_card)
            print('写入成功')
            a = html.find('个人网站', hosp_end + 100)
        i=i+1

    # page_unm=int(get_page(url))
    #
    # for i in range(page):
    #     # page_unm+=iå
    #     page_url=url+'_'+str(i)+'.htm'
    #
    #     html = open_page(page_url).decode('utf-8')
    #     # doctor_list = []

if __name__ == "__main__":
    download_doctor()
