# -*- coding:utf-8 -*-

import urllib2


import urllib2
import re
import os
import sys
import requests
from bs4 import BeautifulSoup




#爬取糗事百科数据

reload(sys)
sys.setdefaultencoding('utf-8')



def write_file(file_name,writer_name,agree,comment,postings):
  f = open (dictionary + file_name+'.txt',mode='w')





if __name__ =="__main__":
  dictionary = '.\\qiubai\\'
  if not os.path.exists(dictionary): #判断目录是否存在
    os.mkdir(dictionary)
  f_all = open(dictionary + 'all.txt',mode='w')


  for page in range(1,100):
    url = 'http://www.qiushibaike.com/hot/page/' +str(page)
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}


    try:
      request = urllib2.Request(url,headers=headers)
      response = urllib2.urlopen(request)
      content = response.read().decode('utf-8')
      print content

    except urllib2.URLError,e:
      if hasattr(e,"code"):
        print e.code
      if hasattr(e,"reasom"):
        print e.reason
      break














