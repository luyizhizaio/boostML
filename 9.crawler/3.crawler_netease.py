# -*- coding:utf-8 -*-

import urllib2
import re
import os
import sys
from bs4 import BeautifulSoup
import httplib

reload(sys)
sys.setdefaultencoding('utf-8')

def write_file(url,path):
  headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
  try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('gbk')
    # print content
    pattern = re.compile('<div class="post_content_main" id="epContentLeft">.*?<h1>(.*?)</h1>', re.S)
    title = re.findall(pattern=pattern, string=content)
    if not title:
      return
    title = title[0]
    print title  # 标题

    soup = BeautifulSoup(content, 'html.parser')

    #div class="post_text" id="endText" style="border-top:1px solid #ddd;">
    article=soup.find(name='div',attrs={'class':'post_text','id':'endText'} )

    text = article.find_all(name='p')
    clear_text = ''
    for item in text:
      t = item.get_text()
      if t:
        clear_text += (t + '\n')
    print clear_text    # 正文

    file_path = path + url[url.rfind('/')+1:url.rfind('.')] + '.txt'
    f = open(file_path,mode='w')
    f.write('原始链接：'+url+ '\n\n')
    f.write(clear_text)
    f.close()
  except urllib2.URLError, e:
    if hasattr(e, "code"):
      print e.code
    if hasattr(e, "reason"):
      print e.reason
def crawl_topic(url,topic):
  print '正在爬取主题：',topic
  print '链接',url
  topic_path = main_dictionary + topic + '/'
  if not os.path.exists(topic_path):
    os.mkdir(topic_path)
  headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
  try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('gbk') # 页面内容

    #print content
    pattern = re.compile('<td class=".*?"><span>.*?</span><a href="(.*?)">(.*?)</a></td>')
    items = re.findall(pattern=pattern, string=content)
    pattern = re.compile('<td class=".*?"><a href="(.*?)">(.*?)</a></td>')
    items += re.findall(pattern=pattern, string=content)
    print items

    for i,(link ,title) in enumerate(items):
      print "link:",link,"title:" ,title
      write_file(link,topic_path)  #topic_path 主题目录
  except urllib2.URLError, e:
    if hasattr(e, "code"):
      print e.code
    if hasattr(e, "reason"):
      print e.reason
  print '\n\n\n\n'




if __name__ =="__main__":
  main_dictionary = './Content/'
  if not os.path.exists(main_dictionary):
    os.mkdir(main_dictionary)

  url = 'http://news.163.com/rank/'
  headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
  try:
    print '建立连接'
    request = urllib2.Request(url,headers={})
    response = urllib2.urlopen(request)

    content = response.read().decode('gbk')
    print content

    #re 支持查询中的正则表达式
    pattern = re.compile(u'<div class="list"><ul id="calendarList"><li></li></ul></div>'
                         u'.*?<div class="subNav">快速跳转：(.*?)<div class="area areabg1">', re.S)

    link_name = re.findall(pattern = pattern, string = content)[0]
    print "link_name:",link_name

    #link_name: <a href="http://news.163.com/special/0001386F/rank_news.html">新闻</a>
    # <a href="http://news.163.com/special/0001386F/rank_ent.html">娱乐</a>
    # <a href="http://news.163.com/special/0001386F/rank_sports.html">体育</a>
    # <a href="http://money.163.com/special/002526BH/rank.html">财经</a>
    # <a href="http://news.163.com/special/0001386F/rank_tech.html">科技</a>
    # <a href="http://news.163.com/special/0001386F/rank_auto.html">汽车</a>
    # <a href="http://news.163.com/special/0001386F/rank_lady.html">女人</a>
    # <a href="http://news.163.com/special/0001386F/rank_house.html">房产</a>
    # <a href="http://news.163.com/special/0001386F/game_rank.html">游戏</a>
    # <a href="http://news.163.com/special/0001386F/rank_travel.html">旅游</a>
    # <a href="http://news.163.com/special/0001386F/rank_edu.html">教育</a></div>
    #<div class="subNav">　　　　　
    # <a href="http://news.163.com/special/0001386F/rank_whole.html">全站</a>
    # <a href="http://news.163.com/photorank/" class="photoset-icon">图集排行榜</a>
    # </div>
    soup = BeautifulSoup(link_name,'html.parser')
    for item in soup.find_all('a'):
      crawl_topic(item['href'],item.get_text())
      break

  except urllib2.URLError,e:
    if hasattr(e,"code"):
      print e.code
    if hasattr(e,"reason"):
      print e.reason
  except httplib.IncompleteRead,e:
    print 'httplib.incompleteread----'
    print e
    if hasattr(e,'code'):
      print e.code
    if hasattr (e,'reason'):
      print e.reason
