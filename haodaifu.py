#/usr/bin/env python3
import urllib.request
import os
import ssl

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
    url="https://www.haodf.com/jibing/ruxianai/daifu_all_all_all_all_all.htm"
    # url = "https://wwww.baidu.com"
    html = open_page(url).decode('gb2312','ignore')
    a = html.find('发布医生')
    b = html.find('blue_a3">', a, a + 500)
    print(html[b+9:b + 11])

    # page_unm=int(get_page(url))
    #
    # for i in range(page):
    #     # page_unm+=i
    #     page_url=url+'_'+str(i)+'.htm'
    #
    #     html = open_page(page_url).decode('utf-8')
    #     # doctor_list = []





if __name__ == "__main__":
    download_doctor()
