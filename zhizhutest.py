#/usr/bin/env python3
import urllib.request
import os
import csv

#打开文件，追加a
out = open('/Users/youpeng/study/practice/doctor.csv','a', newline='')
#设定写入模式
csv_write = csv.writer(out,dialect='excel')

def open_page(url):
    req=urllib.request.Request(url)
    # req.add_header('User','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0')
    response=urllib.request.urlopen(url)
    html=response.read()
    return html

# def get_page(url):
#     html=open_page(url).decode('utf-8')
#     a=html.find('page.cur')+10
#     return html[a]

def find_image(url):
    html=open_page(url).decode('utf-8')
    image_list=[]
    a=html.find('img src=')
    while a!=-1:
        b=html.find('.jpg',a,a+255)
        if b!=-1:
            image_list.append(html[a+9:b+4])
        else:
            b=a+9
        a=html.find('img src',b)
    return image_list

def save_image(folder,image_list):
    for each in image_list:
        file_name=each.split('/')[-1]
        with open(file_name,'wb') as f:
            img=open_page(each)
            f.write(img)

def download_jpg(folder='/Users/youpeng/study/picture/',page=10):
    os.mkdir(folder)
    os.chdir(folder)

    url="http://www.ivsky.com/tupian/chengshilvyou/"
    # page_unm=int(get_page(url))
    for i in range(page):
        # page_unm+=i
        page_url=url+'index_'+str(i)+'.html'
        image_list=find_image(page_url)
        save_image(folder,image_list)

if __name__ == "__main__":
    download_jpg()
