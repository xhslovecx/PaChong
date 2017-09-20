# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:33:49 2017

@author: xhs
"""
import requests
from bs4 import BeautifulSoup as bs
import re
def get_url(url):
    try:
        r=requests.get(url)
        r.status_code
        r.encoding=r.apparent_encoding
        soup=bs(r.text,'html.parser')
        return soup
    except:
        return ''
url='https://www.zhipin.com/job_detail/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&scity=101210100&source=2'
#'url='https://www.zhipin.com/c101210100/h_101210100/?query=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&page=1&ka=page-1'
soup=get_url(url)
company_list=soup.find_all('div',class_="job-primary")
add_list=[]
pattern_chinese=re.compile('[\u4e00-\u9fa5]')
for item in company_list:
    A=item.find_all('a')
    add={}
    add['name']=''.join(re.findall(pattern_chinese,str(A[0]))) 
    add['href']=A[0]['href']+'?ka='+A[0]['ka']
    add_list.append(add) 
file=open('E:/Python/coding/pachong/address.txt','r')
file.write(str(add_list))