__author__ = 'lichangyue'
#-*-coding:utf-8 -*-
from pandas import  Series , DataFrame
import pandas as pd
import numpy as np

#加载数据，默认逗号分隔，返回df

# a,b,c,d,message
# 1,2,3,4,hello
# 5,6,7,8,world
# 9,10,11,12,foo
df = pd.read_csv('ex1.csv')

print df
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

#使用read_table ，指定分隔符

print pd.read_table('ex1.csv',sep=',')
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

#加载无标题数据
# 1,2,3,4,hello
# 5,6,7,8,world
# 9,10,11,12,foo
print  pd.read_csv('ex2.csv',header=None)
#    X0  X1  X2  X3     X4
# 0   1   2   3   4  hello
# 1   5   6   7   8  world
# 2   9  10  11  12    foo
#自定义列名
print  pd.read_csv('ex2.csv',names = ['a','b','c','d','message'])
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo


#把message作为DataFrame的索引,用index_col指定索引名。
names = ['a','b','c','d','message']

print pd.read_csv('ex2.csv',names=names,index_col='message')
#          a   b   c   d
# message
# hello    1   2   3   4
# world    5   6   7   8
# foo      9  10  11  12

# key1,key2,value1,value2
# one,a,1,2
# one,b,3,4
# one,c,5,6
# one,d,7,8
# two,a,9,10
# two,b,11,12
# two,c,13,14
# two,d,15,16

#指定key1，key2 为索引列
parsed = pd.read_csv('csv_mindex.csv',index_col=['key1','key2'])
print parsed
# key1 key2
# one  a          1       2
#      b          3       4
#      c          5       6
#      d          7       8
# two  a          9      10
#      b         11      12
#      c         13      14
#      d         15      16

print list(open('ex3.txt'))
# ['            A         B         C\n',
#  'aaa -0.264438 -1.026059 -0.619500\n',
#  'bbb  0.927272  0.302904 -0.032399\n',
#  'ccc -0.264273 -0.386314 -0.217601\n',
#  'ddd -0.871858 -0.348382  1.100491\n']

#由不同数量的空格分隔的。
result = pd.read_table('ex3.txt',sep='\s+')
print  result
#             A         B         C
# aaa -0.264438 -1.026059 -0.619500
# bbb  0.927272  0.302904 -0.032399
# ccc -0.264273 -0.386314 -0.217601
# ddd -0.871858 -0.348382  1.100491

#跳过文件 第一行，第三行，第四行,因为这几行是注释

# # hey!
# a,b,c,d,message
# # just wanted to make things more difficult for you
# # who reads CSV files with computers, anyway?
# 1,2,3,4,hello
# 5,6,7,8,world
# 9,10,11,12,foo
print pd.read_csv('ex4.csv',skiprows=[0,2,3])
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo


#缺失值处理
result= pd.read_csv('ex5.csv')
print result
#   something  a   b   c   d message
# 0       one  1   2   3   4     NaN
# 1       two  5   6 NaN   8   world
# 2     three  9  10  11  12     foo
print pd.isnull(result)
#   something      a      b      c      d message
# 0     False  False  False  False  False    True
# 1     False  False  False   True  False   False
# 2     False  False  False  False  False   False


result = pd.read_csv('ex5.csv',na_values=['NULL'])
print result
#   something  a   b   c   d message
# 0       one  1   2   3   4     NaN
# 1       two  5   6 NaN   8   world
# 2     three  9  10  11  12     foo
print pd.isnull(result)
#   something      a      b      c      d message
# 0     False  False  False  False  False    True
# 1     False  False  False   True  False   False
# 2     False  False  False  False  False   False

#用字典为各列指定不同的NA标记值
sentinels = {'message':['foo','NA'],'something':['two']}
print pd.read_csv('ex5.csv',na_values=sentinels)
#   something  a   b   c   d message
# 0       one  1   2   3   4     NaN
# 1       NaN  5   6 NaN   8   world
# 2     three  9  10  11  12     NaN

print '###########################################'

data = pd.read_csv('ex5.csv')
print data
#to_csv写出， 逗号分隔
data.to_csv('out.csv')
#打印出文本结果，使用| 分隔
import sys
data.to_csv(sys.stdout, sep='|')
# |something|a|b|c|d|message
# 0|one|1|2|3.0|4|
# 1|two|5|6||8|world
# 2|three|9|10|11.0|12|foo

#指定缺失值输出,
data.to_csv(sys.stdout,na_rep='NULL')
# ,something,a,b,c,d,message
# 0,one,1,2,3.0,4,NULL
# 1,two,5,6,NULL,8,world
# 2,three,9,10,11.0,12,foo
#禁用行列标签
data.to_csv(sys.stdout, index=False , header=False)
# one,1,2,3.0,4,
# two,5,6,,8,world
# three,9,10,11.0,12,foo
#输出指定的列，并按指定的顺序排序
data.to_csv(sys.stdout,index=False,cols=['a','b','c'])
# a,b,c
# 1,2,3.0
# 5,6,
# 9,10,11.0

#Series 的to_csv方法

dates = pd.date_range('1/1/2000',periods =7)
print dates

ts = Series(np.arange(7), index=dates)
print ts
# 2000-01-01    0
# 2000-01-02    1
# 2000-01-03    2
# 2000-01-04    3
# 2000-01-05    4
# 2000-01-06    5
# 2000-01-07    6
# Freq: D
ts.to_csv('tseries.csv')

#读取数据到series
sdata =Series.from_csv('tseries.csv',parse_dates = True)
print sdata
# 2000-01-01    0
# 2000-01-02    1
# 2000-01-03    2
# 2000-01-04    3
# 2000-01-05    4
# 2000-01-06    5
# 2000-01-07    6

print pd.read_csv('tseries.csv',header=False ,index_col =0)
#                      0
# 2000-01-01 00:00:00
# 2000-01-02 00:00:00  1
# 2000-01-03 00:00:00  2
# 2000-01-04 00:00:00  3
# 2000-01-05 00:00:00  4
# 2000-01-06 00:00:00  5
# 2000-01-07 00:00:00  6

print '##################################'

import csv
# "a","b","c"
# "1","2","3"
# "1","2","3","4"
f = open('ex7.csv')
reader = csv.reader(f)

for line in reader:
    print line
# ['a', 'b', 'c']
# ['1', '2', '3']
# ['1', '2', '3', '4']

line = list(csv.reader(open('ex7.csv')))







