__author__ = 'dayue'
#-*-coding:utf-8 -*-

path ='F:\GitHub\pydata-book\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
import json
records = [json.loads(line) for line  in open(path)]
print 'records: %s' %(records[0])
#records: {u'a': u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11',
#  u'c': u'US',
# u'nk': 1,
# u'tz': u'America/New_York',
# u'gr': u'MA',
# u'g': u'A6qOVH',
# u'h': u'wfLQtf',
# u'cy': u'Danvers',
# u'l': u'orofrog',
# u'al': u'en-US,en;q=0.8',
# u'hh': u'1.usa.gov',
# u'r': u'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf',
# u'u': u'http://www.ncbi.nlm.nih.gov/pubmed/22415991', u't': 1331923247,
# u'hc': 1331822918,
# u'll': [42.576698, -70.954903]}


time_zones = [rec['tz'] for rec in records if  'tz' in rec]

print 'time_zones: %s' %(time_zones[:10])
#time_zones:
# [u'America/New_York',
# u'America/Denver',
# u'America/New_York',
# u'America/Sao_Paulo',
# u'America/New_York',
# u'America/New_York',
# u'Europe/Warsaw',
# u'',
# u'',
# u'']


#2.对时区进行计数
#方法1：
def get_counts(sequence):
    counts ={}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

from collections import defaultdict

def get_counts2 (sequence):
    counts = defaultdict(int) #s所有的值均初始化为0
    for x in sequence:
        counts[x] += 1
    return counts

#执行函数
counts = get_counts(time_zones)

print 'result:%s' %(counts['America/New_York'])
#result:1251

print 'length:%s' %(len(time_zones))
#length:3440

#得到前10位的时区及其计数值
def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz ,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print top_counts(counts)

# [(33, u'America/Sao_Paulo'),
#  (35, u'Europe/Madrid'),
#  (36, u'Pacific/Honolulu'),
#  (37, u'Asia/Tokyo'),
#  (74, u'Europe/London'),
#  (191, u'America/Denver'),
#  (382, u'America/Los_Angeles'),
#  (400, u'America/Chicago'),
#  (521, u''),
#  (1251, u'America/New_York')]

from collections import Counter
counts = Counter(time_zones)
print counts.most_common(10)
# [(u'America/New_York', 1251),
#  (u'', 521), (u'America/Chicago', 400),
#  (u'America/Los_Angeles', 382),
#  (u'America/Denver', 191),
#  (u'Europe/London', 74),
#  (u'Asia/Tokyo', 37),
#  (u'Pacific/Honolulu', 36),
#  (u'Europe/Madrid', 35),
#  (u'America/Sao_Paulo', 33)]

#3.用pandas对时区进行计数

from pandas import DataFrame,Series

import pandas as pd ; import __init__ as np
frame =DataFrame(records)

#输出摘要视图
print frame
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 3560 entries, 0 to 3559
# Data columns:
# _heartbeat_    120  non-null values
# a              3440  non-null values
# al             3094  non-null values
# c              2919  non-null values
# cy             2919  non-null values
# g              3440  non-null values
# gr             2919  non-null values
# h              3440  non-null values
# hc             3440  non-null values
# hh             3440  non-null values
# kw             93  non-null values
# l              3440  non-null values
# ll             2919  non-null values
# nk             3440  non-null values
# r              3440  non-null values
# t              3440  non-null values
# tz             3440  non-null values
# u              3440  non-null values
# dtypes: float64(4), object(14)

#输出排名前十的tz
print frame['tz'][:10]
# 0     America/New_York
# 1       America/Denver
# 2     America/New_York
# 3    America/Sao_Paulo
# 4     America/New_York
# 5     America/New_York
# 6        Europe/Warsaw
# 7
# 8
# 9
# Name: tz

tz_counts = frame['tz'].value_counts()

print 'tz_counts %s' %(tz_counts[:10])

# America/New_York       1251
#                         521
# America/Chicago         400
# America/Los_Angeles     382
# America/Denver          191
# Europe/London            74
# Asia/Tokyo               37
# Pacific/Honolulu         36
# Europe/Madrid            35
# America/Sao_Paulo        33

#4.使用matplotlib绘图
print '4.使用matplotlib绘图'
#fillna函数可以替换缺失值
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts()

print(tz_counts[:10])
# America/New_York       1251
# Unknown                 521
# America/Chicago         400
# America/Los_Angeles     382
# America/Denver          191
# Missing                 120
# Europe/London            74
# Asia/Tokyo               37
# Pacific/Honolulu         36
# Europe/Madrid            35

#画水平条形图
tz_counts[:10].plot(kind='barh',rot=0)


#5.解析agent

print frame['a'][1]

print frame['a'][50]

print frame['a'][51]

results = Series([x.split()[0] for x in frame.a.dropna()])

print results[:5]

# 0               Mozilla/5.0
# 1    GoogleMaps/RochesterNY
# 2               Mozilla/4.0
# 3               Mozilla/5.0
# 4               Mozilla/5.0

print results.value_counts()[:8]
# Mozilla/5.0                 2594
# Mozilla/4.0                  601
# GoogleMaps/RochesterNY       121
# Opera/9.80                    34
# TEST_INTERNET_AGENT           24
# GoogleProducer                21
# Mozilla/6.0                    5
# BlackBerry8520/5.0.0.681       4

#6.按windows和非windows用户对时区统计信息进行分解

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),
                            'Windows','Not Windows')
print operating_system[:5]

# 0        Windows
# 1    Not Windows
# 2        Windows
# 3    Not Windows
# 4        Windows
# Name: a

by_tz_os = cframe.groupby(['tz',operating_system])
#size对分组结果进行计数，在利用unstack对计数结果进行重塑
agg_counts = by_tz_os.size().unstack().fillna(0)

print agg_counts[:10]

# a                               Not Windows  Windows
# tz
#                                         245      276
# Africa/Cairo                              0        3
# Africa/Casablanca                         0        1
# Africa/Ceuta                              0        2
# Africa/Johannesburg                       0        1
# Africa/Lusaka                             0        1
# America/Anchorage                         4        1
# America/Argentina/Buenos_Aires            1        0
# America/Argentina/Cordoba                 0        1
# America/Argentina/Mendoza                 0        1

#选取最常出现的时区
indexer = agg_counts.sum(1).argsort()

print indexer[:10]
# tz
#                                   24
# Africa/Cairo                      20
# Africa/Casablanca                 21
# Africa/Ceuta                      92
# Africa/Johannesburg               87
# Africa/Lusaka                     53
# America/Anchorage                 54
# America/Argentina/Buenos_Aires    57
# America/Argentina/Cordoba         26
# America/Argentina/Mendoza         55


count_subset = agg_counts.take(indexer)[-10:] #获取最后10行
print count_subset

# a                    Not Windows  Windows
# tz
# America/Sao_Paulo             13       20
# Europe/Madrid                 16       19
# Pacific/Honolulu               0       36
# Asia/Tokyo                     2       35
# Europe/London                 43       31
# America/Denver               132       59
# America/Los_Angeles          130      252
# America/Chicago              115      285
#                              245      276
# America/New_York             339      912
#

#stacked =True 生成堆积条形图
count_subset.plot(kind='barh',stacked =True)



#将各行规范化为 总计为1 重新绘图
normed_subset = count_subset.div(count_subset.sum(1),axis=0)

normed_subset.plot(kind='barh',stacked=True)
















