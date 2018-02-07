# -*- coding:utf-8 -*-
import os 
import glob
import bs4
import copy
import time
files= glob.glob(pathname="./build/html/**/*.html",recursive=True)
url="https://github.com/zhaojiedi1992/My_Study_Gawk/blob/master/source"
#url2="../_sources/awk语言/简介.rst.txt"
# <a href="../_sources/awk语言/运行awk.rst.txt" rel="nofollow"> View page source</a>
time.sleep(2)
for file_item in files:
    new_content=None
    with open(file_item,mode='r',encoding='utf-8') as f:
        print(file_item)
        content=f.read()
        html = bs4.BeautifulSoup(content,'html.parser')
        view_code = html.select_one(".wy-breadcrumbs-aside")
        if view_code.text is None :
            continue
        view_code_a = view_code.select_one("a")
        if view_code.text is None :
            continue
        print(view_code_a)
        new_a = bs4.BeautifulSoup('<a href="' + view_code_a["href"].replace(".txt","").replace("../_sources",url) + '" rel="nofollow"> ' + "编辑github" +'</a>')
        print(new_a)
        view_code.append(new_a)
        new_content =html.html
    with open(file_item +".bak",mode='w',encoding='utf-8') as f:
        f.write(new_content)
    #os.remove(file_item)
    #os.rename(file_item+".bak",file_item)
