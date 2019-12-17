import requests
import re
url = 'http://www.xbiquge.la/10/10489/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
# 模拟浏览器发送http请求
response = requests.get(url, headers=headers)
# 编码方式
response.encoding = 'utf-8'
# 网页源码
html = response.text
# 章节标题
title = re.findall(r'<meta property="og:title" content="(.*?)"/>',html)[0]  # r代表后面字符串不转义
# 获取每一章的信息(章节的url)
dl = re.findall(r'<div id="list">.*?</div>', html, re.S)[0]
chapter_info_list = re.findall('<dd><a href=\'(.*?)\' >(.*?)</a></dd>', dl)  # 使用单引号需要转义，故去掉r而使用\'，并且注意空格

# 循环每一个章节，分别下载
f = open(f"{title}.txt",'w',encoding="utf-8")
for chapter_info in chapter_info_list:
    f.write("***************Start***************\n")
    # chapter_url = chapter_info[0]
    # chapter_title = chapter_info[1]
    chapter_url,chapter_title = chapter_info
    chapter_url = "http://www.xbiquge.la%s" % chapter_url
    # 下载章节内容
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0", }
    chapter_response = requests.get(chapter_url, headers=headers)
    chapter_response.encoding = 'utf-8'
    chapter_html = chapter_response.text
    # 提取章节内容
    chapter_content = re.findall(r'<div id="content">(.*?)<p', chapter_html, re.S)[0]
    # 清洗提取的数据
    # 将其中内容的空格部分替换成空
    chapter_content = chapter_content.replace(' ', '')
    # 将其中内容的<br />部分替换成空
    chapter_content = chapter_content.replace('<br/>', '')
    # 将其中内容的<&nbsp;>部分替换成空
    chapter_content = chapter_content.replace('&nbsp;', '')
    # 写入
    f.write(f"{chapter_title}\n")
    f.write(f"{chapter_content}\n")
    f.write("***************End***************\n")
    print(chapter_url)

