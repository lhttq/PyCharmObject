# encoding=utf-8
import requests
import pymysql
import re
import chardet
from lxml import etree
import os
from bs4 import BeautifulSoup


# BeautifulSoup 是HTML解析库

def get_onepage(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    url = 'http://search.dangdang.com/?key=%D0%C4%C0%ED%D1%A7&act=input&page_index=' + str(page)
    res = requests.get(url, headers=headers)
    res.encoding = chardet.detect(res.content)['encoding']  # 自动编码
    return res.text


def parse_onepage(html):
    result = etree.HTML(html)

    # 解析到数组
    x = 1
    arr = [[] for i in range(6)]
    while (result.xpath('string(//ul[@class="bigimg"]/li[$s])', s=x)):
        x += 1
    for i in range(1, x):
        arr[0].append(result.xpath('string(//ul[@class="bigimg"]/li[$s]/p[@class="name"]/a)', s=i))  # 标题
        arr[1].append(result.xpath('string(//ul[@class="bigimg"]/li[$s]/p[@class="price"]/span)', s=i))  # 现价
        arr[2].append(
            result.xpath('string(//ul[@class="bigimg"]/li[$s]/p[@class="search_book_author"]/span[1])', s=i))  # 作者
        arr[3].append(
            result.xpath('string(//ul[@class="bigimg"]/li[$s]/p[@class="search_book_author"]/span[2])', s=i))  # 出版时间
        arr[4].append(
            result.xpath('string(//ul[@class="bigimg"]/li[$s]/p[@class="search_book_author"]/span[3])', s=i))  # 出版社

        # 处理图片链接
        img_line = str(result.xpath('string(//ul[@class="bigimg"]/li[$s]/a/img/@src)', s=i))
        img_comp = "http"
        img_flg = re.compile(img_comp, re.S)
        result_img = img_flg.findall(img_line)
        if result_img:
            arr[5].append(result.xpath('string(//ul[@class="bigimg"]/li[$s]/a/img/@src)', s=i))
        else:
            arr[5].append(result.xpath('string(//ul[@class="bigimg"]/li[$s]/a/img/@data-original)', s=i))

    # 数据清理
    for i in range(len(arr[3])):  # 去除出版时间前的"/"
        arr[3][i] = arr[3][i].lstrip(' /')
    for i in range(len(arr[4])):  # 去除出版社前的"/"
        arr[4][i] = arr[4][i].lstrip(' /')

    # 封装到字典
    item = {}
    item['b1'] = arr[0]
    item['b2'] = arr[1]
    item['b3'] = arr[2]
    item['b4'] = arr[3]
    item['b5'] = arr[4]
    item['b6'] = arr[5]
    return item


def write_toMysql(item_z):
    con = pymysql.connect(host='localhost', user='root', passwd='123456', db='dangdang_book', charset='utf8')
    cur = con.cursor()
    for i in range(len(item_z['b1'])):
        title = item_z['b1'][i]
        price = item_z['b2'][i]
        author = item_z['b3'][i]
        date = item_z['b4'][i]
        company = item_z['b5'][i]
        sql_t = "insert into books values(null,%s,%s,%s,%s,%s)"
        parm_t = (title, price, author, date, company)
        cur.execute(sql_t, parm_t)
    con.commit()
    cur.close()
    con.close()


def save_img(img_list, page):
    # 清洗书名,用以为图片命名:
    # 如果有“：”则分开，若没有则按空格分开
    img_arr = []
    for imagename_i in range(0, len(img_list['b6'])):
        imgname_org = img_list['b1'][imagename_i]

        imgname_comp = "："
        imgname_maohao = re.compile(imgname_comp, re.S)
        imgname_maohao_res = imgname_maohao.findall(imgname_org)  # 此时有冒号的被分开
        if imgname_maohao_res:  # 名字中有“：”
            imgname_split = imgname_org.split("：")
        else:  # 按空格分开
            imgname_split = imgname_org.split()

        imgname_res = imgname_split[0]  # 选取截取后的名字存入数组
        img_arr.append(imgname_res)

    # 下载到本地文件夹
    folder_path = "D:\\work\\python_objs\\book\\images_1\\"
    for image_flg in range(0, len(img_list['b6'])):
        image_path = folder_path + str(page) + "." + str(image_flg + 1) + "-" + img_arr[image_flg] + ".png"
        image_url = requests.get(img_list['b6'][image_flg])
        image_url.raise_for_status()
        with open(image_path, 'wb') as fd:
            fd.write(image_url.content)
            fd.close()


def main(page):
    # 获取单页HTML
    html = get_onepage(page)

    # 解析html
    item_z = parse_onepage(html)

    # 写进数据库mysql
    write_toMysql(item_z)

    # 存储图片到本地
    save_img(item_z, page)


if __name__ == '__main__':
    for i in range(1, 11):  # 分页,爬取前十页的信息
        main(i)