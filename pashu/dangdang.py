#/usr/bin/env python3
import urllib.request
import ssl
from lxml import etree

ssl._create_default_https_context = ssl._create_unverified_context

def open_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
    req = urllib.request.Request(url=url, headers=headers)
    html=urllib.request.urlopen(req).read()
    return html


if __name__ == '__main__':
    html=open_page('http://search.dangdang.com/?key=9787517067146')
    # print(data)
    html_data = etree.HTML(html)
    book_list = html_data.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(book_list)
    for content in book_list:
        item = {}
        item['name'] = content.xpath('./p[@class="name"]/a/text()')
        item['price'] = content.xpath('./p[@class="price"]/span[1]/text()')
        item['oldprice']= content.xpath('./p[@class="price"]/span[2]/text()')
        print(item['name'])
        print(item['price'])
        print(item['oldprice'])