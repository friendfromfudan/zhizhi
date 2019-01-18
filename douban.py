import requests,csv,time,pandas,numpy,re,jieba,wordcloud
from lxml import etree
# from lxml import xpath
# import xpath
# import mataplotlib


def parse_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0)Gecko/20100101 Firefox/23.0'}
    response = requests.get(url, headers=headers)
    return response.content.decode()


def get_content_list(html_str):
    html = etree.HTML(html_str)
    content_list = html.xpath('//div[@class="mod-bd"]/div[@class="comment-item"]')

    contents = []
    for content in content_list:
        item = {}
        item['name'] = content.xpath('./div[2]/h3/span[2]/a/text()')[0] if len(
            content.xpath('./div[2]/h3/span[2]/a/text()')) > 0 else None
        str_datetime = content.xpath('./div[2]/h3/span[2]/span[@class="comment-time "]/text()')[0] if len(
            content.xpath('./div[2]/h3/span[2]/span[@class="comment-time "]/text()')) > 0 else None
        str_datetime = str(str_datetime).strip()
        item['datetiem'] = str_datetime
        item['text'] = content.xpath('./div[2]/p/span/text()')[0] if len(
            content.xpath('./div[2]/p/span/text()')) > 0 else None
        item['rate'] = content.xpath('./div[2]/h3/span[2]/span[2]/@title')[0] if len(
            content.xpath('./div[2]/h3/span[2]/span[2]/@title')) > 0 else None
        contents.append(item)
    next_url = 'https://movie.douban.com/subject/27172891/comments' + html.xpath('//div[@id="paginator"]/a[@class="next"]/@href')[0] if len(
        html.xpath('//div[@id="paginator"]/a[@class="next"]/@href')) > 0 else None
    return (contents, next_url)

def save_content_list(contents):
    with open('/Users/youpeng/zhizhi/movie.csv', 'a', encoding='utf-8') as f:
        w = csv.writer(f)
        # print(contents[0][0].keys())
        # print(contents[0].key())
        fieldnames = contents[0].keys()
        w.writerow(fieldnames)
        for row in contents:
            w.writerow(row.values())

if __name__ == '__main__':
    url="https://movie.douban.com/subject/27172891/comments"
    # html1= etree.HTML(html)
    # html1.xpath('//div[@class="mod-bd"]/div[@class="comment-item"]')
    # print(html)
    while url!=None:
        html = parse_url(url=url)
        (content, url) = get_content_list(html_str=html)
        print(url)
        print(content)
        save_content_list(contents=content)

    # if url!=False:

    # print(content)


