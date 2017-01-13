__author__ = 'lichangyue'
#-*-coding:utf-8 -*-
#规整化数据集
from pandas import  Series , DataFrame
import pandas as pd
import numpy as np

#merge 根据key连接行

df1= DataFrame({'key':['b','b','a','c','a','a','b'],
                'data1':range(7)})

df2= DataFrame({'key':['a','b','d'],
                'data2':range(3)})

print df1
#    data1 key
# 0      0   b
# 1      1   b
# 2      2   a
# 3      3   c
# 4      4   a
# 5      5   a
# 6      6   b

print df2
#    data2 key
# 0      0   a
# 1      1   b
# 2      2   d

#默认做内连接 ，默认以重叠的列作为键
print pd.merge(df1, df2)
#    data1 key  data2
# 0      2   a      0
# 1      4   a      0
# 2      5   a      0
# 3      0   b      1
# 4      1   b      1
# 5      6   b      1
#指定连接的key
print pd.merge(df1,df2,on='key')
#    data1 key  data2
# 0      2   a      0
# 1      4   a      0
# 2      5   a      0
# 3      0   b      1
# 4      1   b      1
# 5      6   b      1
#两个df连接的列名不同
df3= DataFrame({'lkey':['b','b','a','c','a','a','b'],
                'data1':range(7)})

df4= DataFrame({'rkey':['a','b','d'],
                'data2':range(3)})

print pd.merge(df3,df4,left_on='lkey' , right_on='rkey')
#    data1 lkey  data2 rkey
# 0      2    a      0    a
# 1      4    a      0    a
# 2      5    a      0    a
# 3      0    b      1    b
# 4      1    b      1    b
# 5      6    b      1    b

#全外连接 使用outer,# 左外连接：left,右外链接：right
print pd.merge(df1,df2,how='outer')
#    data1 key  data2
# 0      2   a      0
# 1      4   a      0
# 2      5   a      0
# 3      0   b      1
# 4      1   b      1
# 5      6   b      1
# 6      3   c    NaN
# 7    NaN   d      2



#多对多的合并操作：

df1= DataFrame({'key':['b','b','a','c','a','b'],
                'data1':range(6)})

df2= DataFrame({'key':['a','b','d','b','d'],
                'data2':range(5)})

print df1


print df2


#左连接
print pd.merge(df1,df2,on ='key',how = 'left')
#    data1 key  data2
# 0      2   a      0
# 1      4   a      0
# 2      0   b      1
# 3      0   b      3
# 4      1   b      1
# 5      1   b      3
# 6      5   b      1
# 7      5   b      3
# 8      3   c    NaN

print pd.merge(df1, df2,how='inner')
#    data1 key  data2
# 0      2   a      0
# 1      4   a      0
# 2      0   b      1
# 3      0   b      3
# 4      1   b      1
# 5      1   b      3
# 6      5   b      1
# 7      5   b      3

#多个键进行合并，
left=DataFrame({'key1':['foo','foo','bar'],
                'key2':['one','two','one'],
                'lval':[1,2,3]})

right=DataFrame({'key1':['foo','foo','bar','bar'],
                'key2':['one','one','one','two'],
                'lval':[4,5,6,7]})
print pd.merge(left,right,on=['key1','key2'],how='outer')
#   key1 key2  lval_x  lval_y
# 0  bar  one       3       6
# 1  bar  two     NaN       7
# 2  foo  one       1       4
# 3  foo  one       1       5
# 4  foo  two       2     NaN

print pd.merge(left,right,on='key1')
#   key1 key2_x  lval_x key2_y  lval_y
# 0  bar    one       3    one       6
# 1  bar    one       3    two       7
# 2  foo    one       1    one       4
# 3  foo    one       1    one       5
# 4  foo    two       2    one       4
# 5  foo    two       2    one       5

print  pd.merge(left,right,on='key1',suffixes=('_left','_right'))
#   key1 key2_left  lval_left key2_right  lval_right
# 0  bar       one          3        one           6
# 1  bar       one          3        two           7
# 2  foo       one          1        one           4
# 3  foo       one          1        one           5
# 4  foo       two          2        one           4
# 5  foo       two          2        one           5
print '###################'
#DF连接键在索引中，

left1 = DataFrame({'key':['a','b','a','a','b','c'],
                   'value':range(6)})

right1 = DataFrame({'group_val':[3.5,7]},index = ['a','b'])

print left1
#   key  value
# 0   a      0
# 1   b      1
# 2   a      2
# 3   a      3
# 4   b      4
# 5   c      5


print right1
#    group_val
# a        3.5
# b        7.0

#指定右边使用index连接
print pd.merge(left1,right1 , left_on='key' , right_index=True)
#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0

#全外链接
print pd.merge(left1,right1,left_on='key',right_index=True,how='outer')
#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0
# 5   c      5        NaN

#处理层次化索引的数据

lefth = DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],
                   'key2':[2000,2001,2002,2001,2002],
                   'data':np.arange(5.)})

righth = DataFrame(np.arange(12).reshape(6,2),
                   index = [['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],
                   [2001,2000,2000,2000,2001,2002]],
                   columns=['event1','event2'])
print lefth
#    data    key1  key2
# 0     0    Ohio  2000
# 1     1    Ohio  2001
# 2     2    Ohio  2002
# 3     3  Nevada  2001
# 4     4  Nevada  2002
print righth
#              event1  event2
# Nevada 2001       0       1
#        2000       2       3
# Ohio   2000       4       5
#        2000       6       7
#        2001       8       9
#        2002      10      11

#合并多列 , 左边用key1，key2练级， 右边用索引连接
print pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)
#    data    key1  key2  event1  event2
# 3     3  Nevada  2001       0       1
# 0     0    Ohio  2000       4       5
# 0     0    Ohio  2000       6       7
# 1     1    Ohio  2001       8       9
# 2     2    Ohio  2002      10      11

#全外连接
print pd.merge(lefth,righth,left_on=['key1','key2'],
         right_index=True, how ='outer')
#    data    key1  key2  event1  event2
# 4   NaN  Nevada  2000       2       3
# 3     3  Nevada  2001       0       1
# 4     4  Nevada  2002     NaN     NaN
# 0     0    Ohio  2000       4       5
# 0     0    Ohio  2000       6       7
# 1     1    Ohio  2001       8       9
# 2     2    Ohio  2002      10      11


#DF的join方法。合并躲过电泳相同或相似的索引的DF对象

print left1.join(right1,on='key')
#   key  value  group_val
# 0   a      0        3.5
# 1   b      1        7.0
# 2   a      2        3.5
# 3   a      3        3.5
# 4   b      4        7.0
# 5   c      5        NaN

print '###################################################################'
arr = np.arange(12).reshape((3,4))
print arr
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print np.concatenate([arr,arr],axis=1)
# [[ 0  1  2  3  0  1  2  3]
#  [ 4  5  6  7  4  5  6  7]
#  [ 8  9 10 11  8  9 10 11]]

#pandas的concat函数
#三个不重复索引的Series
s1 =Series([0,1],index=['a','b'])
s2 =Series([2,3,4],index=['c','d','e'])
s3 =Series([5,6],index=['f','g'])

print pd.concat([s1,s2,s3])
# a    0
# b    1
# c    2
# d    3
# e    4
# f    5
# g    6

print pd.concat([s1,s2,s3],axis=1)
#     0   1   2
# a   0 NaN NaN
# b   1 NaN NaN
# c NaN   2 NaN
# d NaN   3 NaN
# e NaN   4 NaN
# f NaN NaN   5
# g NaN NaN   6

s4= pd.concat([s1 *5,s3])

print pd.concat([s1,s4],axis=1)
#     0  1
# a   0  0
# b   1  5
# f NaN  5
# g NaN  6
print pd.concat([s1,s4],axis=1,join='inner')
#    0  1
# a  0  0
# b  1  5

#join_axes指定其他轴上使用的索引 (指定行索引)
print pd.concat([s1,s4],axis=1,join_axes=[['a','c','b','e']])
#     0   1
# a   0   0
# c NaN NaN
# b   1   5
# e NaN NaN

#创建层次化索引
result= pd.concat([s1,s2,s3],keys=['one','two','three'])
print result
# one    a    0
#        b    1
# two    c    2
#        d    3
#        e    4
# three  f    5
#        g    6