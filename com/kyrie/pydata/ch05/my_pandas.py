__author__ = 'lichangyue'
#-*-coding:utf-8 -*-

from pandas import  Series , DataFrame
import pandas as pd
import numpy as np

print 'first'

obj = Series(np.arange(4.),index=['a','b','c','d'])

print obj['b']
# 1.0
print obj[1]
# 1.0

print obj[2:4]
# c    2
# d    3
print obj[['b','a','d']]
# b    1
# a    0
# d    3
print '------'
#通过值来索引
print obj[[1,3]]
# b    1
# d    3
print '------'
print obj[obj < 2]
# a    0
# b    1

#标签切片运算，包含末端的数值
print obj['b':'d']
# b    1
# c    2
# d    3
#设值
obj['b':'d'] =5
print  obj
# a    0
# b    5
# c    5
# d    5
#####################################
print '##############'
#对DataFrame 进行索引就是获取一个或多个列

data= DataFrame(np.arange(16).reshape((4,4)),
                index = ['Ohio','Colorado','Utah','New York'],
                columns=['one','two','three','four'])
print data
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

print data['two']
# Ohio         1
# Colorado     5
# Utah         9
# New York    13
# Name: two

print data[['three','one']]

#           three  one
# Ohio          2    0
# Colorado      6    4
# Utah         10    8
# New York     14   12

#切片
print data[:2]  #获取前两行
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7

print data[data['three'] > 5]  #判断第三列的值大于5
#           one  two  three  four
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

#通过布尔型DataFrame进行索引

print data < 5
#             one    two  three   four
# Ohio       True   True   True   True
# Colorado   True  False  False  False
# Utah      False  False  False  False
# New York  False  False  False  False

#修改值 ，data中小于5的值为0
data[ data < 5 ]  = 0
print data
#           one  two  three  four
# Ohio        0    0      0     0
# Colorado    0    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

#在df的行上进行标签索引，使用ix索引字段 ，选取行和列的子集。
print data.ix['Colorado',['two','three']]  #选取指定行的，指定列
# two      5
# three    6
# Name: Colorado

print data.ix[['Colorado','Utah'],[3,0,1]]
#           four  one  two
# Colorado     7    0    5
# Utah        11    8    9

#获取第二列
print  data.ix[2]
# one       8
# two       9
# three    10
# four     11
# Name: Utah

#获取从第一行到Utah行的第二列
print data.ix[:'Utah','two']
# Ohio        0
# Colorado    5
# Utah        9
# Name: two

# 取data的three列的值大于5的行和前3列
print data.ix[data.three > 5, :3]
#           one  two  three
# Colorado    0    5      6
# Utah        8    9     10
# New York   12   13     14

print '########################################################################'
#2.3.算数运算和数据对齐


s1 = Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.1],index= ['a','c','e','f','g'])
print s1
# a    7.3
# c   -2.5
# d    3.4
# e    1.5
print s2
# a   -2.1
# c    3.6
# e   -1.5
# f    4.0
# g    3.1
print  s1 +s2
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# g    NaN



df1 = DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),
                index=['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),
                index=['Utah','Ohio','Texas','Oregon'])

print df1
#           b  c  d
# Ohio      0  1  2
# Texas     3  4  5
# Colorado  6  7  8

print df2
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregon  9  10  11

#相加返回新的df，索引和列为原来来个DataFrame的并集
print df1 + df2
#            b   c   d   e
# Colorado NaN NaN NaN NaN
# Ohio       3 NaN   6 NaN
# Oregon   NaN NaN NaN NaN
# Texas      9 NaN  12 NaN
# Utah     NaN NaN NaN NaN

df1 = DataFrame(np.arange(12.).reshape((3,4)),columns = list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4,5)),columns = list('abcde'))

print df1 +df2
#     a   b   c   d   e
# 0   0   2   4   6 NaN
# 1   9  11  13  15 NaN
# 2  18  20  22  24 NaN
# 3 NaN NaN NaN NaN NaN
print df1.add(df2 , fill_value =0)
#     a   b   c   d   e
# 0   0   2   4   6   4
# 1   9  11  13  15   9
# 2  18  20  22  24  14
# 3  15  16  17  18  19

print df1.reindex(columns=df2.columns, fill_value=0)
#    a  b   c   d  e
# 0  0  1   2   3  0
# 1  4  5   6   7  0
# 2  8  9  10  11  0

print '##############################################'

arr= np.arange(12.).reshape((3,4))  #生成二维数组
print arr
# [[  0.   1.   2.   3.]
#  [  4.   5.   6.   7.]
#  [  8.   9.  10.  11.]]

print arr[0]
# [ 0.  1.  2.  3.]

#减去一个数组 ，叫做广播
print  arr - arr[0]
# [[ 0.  0.  0.  0.]
#  [ 4.  4.  4.  4.]
#  [ 8.  8.  8.  8.]]

#DataFrame 和Series 之间的运算差不多如上面所述

frame = DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),
                  index=['Utah','Ohio','Texas','Oregon'])

print  frame
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregon  9  10  11
series = frame.ix[0]  #获取第一行数据
print series
# b    0
# d    1
# e    2
# Name: Utah

print frame -series
#         b  d  e
# Utah    0  0  0
# Ohio    3  3  3
# Texas   6  6  6
# Oregon  9  9  9

series2 = Series(range(3),index=['b','e','f'])
print series2
# b    0
# e    1
# f    2

print frame
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregon  9  10  11

print frame + series2
#         b   d   e   f
# Utah    0 NaN   3 NaN
# Ohio    3 NaN   6 NaN
# Texas   6 NaN   9 NaN
# Oregon  9 NaN  12 NaN



print frame
#         b   d   e
# Utah    0   1   2
# Ohio    3   4   5
# Texas   6   7   8
# Oregon  9  10  11
series3 = frame['d']
print series3
# Utah       1
# Ohio       4
# Texas      7
# Oregon    10
# Name: d

print frame.sub(series3, axis=0)
#         b  d  e
# Utah   -1  0  1
# Ohio   -1  0  1
# Texas  -1  0  1
# Oregon -1  0  1

print '######################################################'

frame =DataFrame(np.random.randn(4,3),columns=list('bde'),
                 index=['Utah','Ohio','Texas','Oregon'])

print frame
#                b         d         e
# Utah   -0.776852  0.976385  0.153123
# Ohio   -0.078862 -0.710521 -1.514677
# Texas  -0.427293  0.644912 -0.006891
# Oregon  1.415490 -0.112789  0.565584

print np.abs(frame)
#                b         d         e
# Utah    0.776852  0.976385  0.153123
# Ohio    0.078862  0.710521  1.514677
# Texas   0.427293  0.644912  0.006891
# Oregon  1.415490  0.112789  0.565584


#将函数应用到由各列和行所形成的一维数组上。DataFrame的apply方法即可实现此功能：

f= lambda x : x.max() - x.min()

print frame.apply(f)
# b    2.192342
# d    1.686906
# e    2.080261

print frame.apply(f,axis=1)  #在行上应用
# Utah      1.753236
# Ohio      1.435815
# Texas     1.072205
# Oregon    1.528279


#
def f(x):
    return Series([x.min(),x.max()],index=['min','max'])

print frame.apply(f)
#             b         d         e
# min -0.400401 -0.271205 -0.693948
# max  0.756087  1.845886  2.541060

#元素级别的python函数也可以使用
#例各个浮点值的格式化字符串
format = lambda x: '%.2f' % x
print frame.applymap(format)
#             b      d      e
# Utah     0.27  -1.61   0.84
# Ohio    -0.72   0.74  -0.76
# Texas    0.98  -0.86   0.33
# Oregon   0.84  -0.40   1.56



print frame['e'].map(format)
# Utah      -0.50
# Ohio       0.65
# Texas     -0.97
# Oregon    -0.25
# Name: e

print  '##############################'

obj = Series(range(4),index=['d','a','b','c'])
#返回字典顺序
print obj.sort_index()
# a    1
# b    2
# c    3
# d    0

#
#对于dataframe，可以根据任一轴上的索引排序
frame = DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],
                  columns=['d','a','b','c'])

#行排序
print frame.sort_index()
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3
#列排序
print  frame.sort_index(axis=1)
#        a  b  c  d
# three  1  2  3  0
# one    5  6  7  4

#数据默认是升序排序， 也可以指定降序排序
print frame.sort_index(axis=1, ascending=False)
#        d  c  b  a
# three  0  3  2  1
# one    4  7  6  5

#按值对Series进行排序，使用order方法 ,
obj =Series([4,7,-3,2])
print obj.order()
# 2   -3
# 3    2
# 0    4
# 1    7
#排序时，任何缺失值默认都会被放到Series的末尾
obj= Series([4,np.nan, 7 ,np.nan,-3 ,2])
print  obj.order()
# 4    -3
# 5     2
# 0     4
# 2     7
# 1   NaN
# 3   NaN

#df上，通过一列或多列的值进行排序
frame = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print frame

print  frame.sort_index(by='b')
#    a  b
# 2  0 -3
# 3  1  2
# 0  0  4
# 1  1  7
#根据多列进行排序，传入名称的列表即可
print frame.sort_index(by=['a','b'])
#    a  b
# 2  0 -3
# 0  0  4
# 3  1  2
# 1  1  7
#排名(ranking)跟排序关系密切，会增设一个排名值（从1开始）.

obj= Series([7,-5,7,4,2,0,4])
print '-----------------------'
print obj.rank()
# 0    6.5
# 1    1.0
# 2    6.5
# 3    4.5
# 4    3.0
# 5    2.0
# 6    4.5
#根据值在原数据中出现的顺序给出排名
print  obj.rank(method='first')
# 0    6
# 1    1
# 2    7
# 3    4
# 4    3
# 5    2
# 6    5
print '-----------------------'
#按降序进行排名
print obj.rank(ascending = False, method='max')
# 0    2
# 1    7
# 2    2
# 3    4
# 4    5
# 5    6
# 6    4
#给出破坏平级关系的method ，df可以在行或列上计算排名
frame = DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})
print frame
#    a    b    c
# 0  0  4.3 -2.0
# 1  1  7.0  5.0
# 2  0 -3.0  8.0
# 3  1  2.0 -2.5

print frame.rank(axis=1)
#    a  b  c
# 0  2  3  1
# 1  1  3  2
# 2  2  1  3
# 3  2  3  1

####################################################################
obj = Series(range(5),index=['a','a','b','b','c'])
print  obj
# a    0
# a    1
# b    2
# b    3
# c    4

#使用索引的is_unique属性查看值是否唯一
print obj.index.is_unique
# False
#对于重复索引时，每一个索引对应多个值时，则会返回一个Series， 对应单值的返回一个标量
print obj['a']
# a    0
# a    1

print obj['c']

#DF
df = DataFrame(np.random.randn(4,3),index =['a','a','b','b'])
print  df
#           0         1         2
# a  0.365715  1.339864 -0.844242
# a  0.428636 -1.241557 -0.363611
# b -1.223827  0.311294 -0.225883
# b  0.335159  0.439591  1.777331
print df.ix['b']
#           0         1         2
# b -1.223827  0.311294 -0.225883
# b  0.335159  0.439591  1.777331


print '####################################################'
df = DataFrame([[1.4,np.nan],[7.1,-4.5],
                [np.nan,np.nan],[0.75,-1.3]],
               index =['a','b','c','d'],
               columns=['one','two'])


print  df
#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3

print df.sum()
# one    9.25
# two   -5.80

#按行进行求和运算
print df.sum(axis =1)
# a    1.40
# b    2.60
# c     NaN
# d   -0.55
#NA值会自动被排除，除非整个切片都是NA,通过skipna选项可以禁止此功能
print df.mean(axis=1, skipna =False)
# a      NaN
# b    1.300
# c      NaN
# d   -0.275

#idxmin 和idxmax返回达到最小值或最大值的索引
print df.idxmax()
# one    b
# two    d
#返回累计型数据
print df.cumsum()
#     one  two
# a  1.40  NaN
# b  8.50 -4.5
# c   NaN  NaN
# d  9.25 -5.8

#describe 返回多个汇总统计
print df.describe()
#             one       two
# count  3.000000  2.000000
# mean   3.083333 -2.900000
# std    3.493685  2.262742
# min    0.750000 -4.500000
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000

#非数值型数据，describe会产生另外一种汇总统计

obj = Series(['a','a','b','c'] * 4 )

print obj.describe()
# count     16
# unique     3
# top        a
# freq       8
print '#################################################################'

import pandas.io.data as web

# all_data ={}
# for ticker in ['AAPL','IBM','MSFT','GOOG']:
#     all_data[ticker] = web.get_data_yahoo(ticker,'1/1/2000','1/1/2010')
#
# print all_data
#
# price = DataFrame({tic:data['Adj Close'] for  tic ,data in all_data.iteritems()})
#
# volume =DataFrame({tic :data['Volume'] for tic ,data in all_data.iteritems()})
#
# #计算价格的百分数变化
# returns = price.pct_change()
# print returns.tail()
# #                AAPL      GOOG       IBM      MSFT
# # Date
# # 2009-12-24  0.034339  0.011117  0.004385  0.002587
# # 2009-12-28  0.012294  0.007098  0.013326  0.005484
# # 2009-12-29 -0.011861 -0.005571 -0.003477  0.007058
# # 2009-12-30  0.012147  0.005376  0.005461 -0.013699
# # 2009-12-31 -0.004300 -0.004416 -0.012597 -0.015504
# #Series的corr方法用于计算两个Series中重叠的，非NA的，按索引对齐的值的相关系数，cov用于计算协方差
# #计算相关性
# print returns.MSFT.corr(returns.IBM)
# # 0.495979626103
#
# print returns.MSFT.cov(returns.IBM)
# # 0.000215957600767
#
# #DF的corr和cov将以df形式返回完整的相关系数或协方差矩阵
#
# print returns.corr()
# #           AAPL      GOOG       IBM      MSFT
# # AAPL  1.000000  0.470676  0.410011  0.424305
# # GOOG  0.470676  1.000000  0.390689  0.443587
# # IBM   0.410011  0.390689  1.000000  0.495980
# # MSFT  0.424305  0.443587  0.495980  1.000000
#
# print returns.cov()
# #           AAPL      GOOG       IBM      MSFT
# # AAPL  0.001027  0.000303  0.000252  0.000309
# # GOOG  0.000303  0.000580  0.000142  0.000205
# # IBM   0.000252  0.000142  0.000367  0.000216
# # MSFT  0.000309  0.000205  0.000216  0.000516
# #用df的corrwith方法，计算列或行跟另外一个Series或df之间的相关系数，传入一个Series返回一个相关系数值Series（针对各列进行计算）
#
# print returns.corrwith(returns.IBM)
# # AAPL    0.410011
# # GOOG    0.390689
# # IBM     1.000000
# # MSFT    0.495980
#
# #传入df会按列名配对的相关系数
# print returns.corrwith(volume)
# AAPL   -0.057549
# GOOG    0.062647
# IBM    -0.007892
# MSFT   -0.014245

print '############################################'

obj = Series(['c','a','d','a','b','d','c','c'])
#返回Series中的唯一值 ，返回的结果未排序
uniques = obj.unique()
print uniques
# [c a d b]

uniques.sort()
print uniques
# [a b c d]
#value_counts 计算一个Series中各值出现的频率 ,默认按频率降序排序
print obj.value_counts()
# c    3
# d    2
# a    2
# b    1
#value_counts还是pandas的顶级方法，可以用于任何数组或序列
print pd.value_counts(obj.values, sort=False)
# a    2
# b    1
# c    3
# d    2

#isin 方法判断矢量化集合的成员资格，就是看看在不在传入的值序列中。

mask = obj.isin(['b','c'])
print mask
# 0     True
# 1    False
# 2    False
# 3    False
# 4     True
# 5    False
# 6     True
# 7     True

print  obj[mask]
# 0    c
# 4    b
# 6    c
# 7    c

#得打df中多个相关列的一张柱状图
data = DataFrame({'Qu1':[1,3,4,3,4],
                  'Qu2':[2,3,1,2,3],
                  'Qu3':[1,5,3,4,4],})

print data
#    Qu1  Qu2  Qu3
# 0    1    2    1
# 1    3    3    5
# 2    4    2    3
# 3    3    3    4
# 4    4    4    4

result = data.apply(pd.value_counts).fillna(0)
print result
#    Qu1  Qu2  Qu3
# 1    1    1    1
# 2    0    2    0
# 3    2    2    1
# 4    2    0    2
# 5    0    0    1

print '##################'

string_data = Series(['aardvark','atrichoke',np.nan,'avocado'])
print  string_data
# 0     aardvark
# 1    atrichoke
# 2          NaN
# 3      avocado

print string_data.isnull()
# 0    False
# 1    False
# 2     True
# 3    False
#python 内置的None 也会被当做NA处理

string_data[0]=None
print string_data
# 0         None
# 1    atrichoke
# 2          NaN
# 3      avocado

print string_data.isnull()
# 0     True
# 1    False
# 2     True
# 3    False

print '####################################'

from numpy import nan as NA

data  = Series([1, NA,3.5,NA,7])
print  data.dropna()
# 0    1.0
# 2    3.5
# 4    7.0

#也可以通过布尔型索引达到这个目的
print data[data.notnull()]
# 0    1.0
# 2    3.5
# 4    7.0


data =DataFrame([[1,6.5,3.],[1.,NA,NA],
                [NA,NA,NA],[NA,6.5,3.]])
print data
#     0    1   2
# 0   1  6.5   3
# 1   1  NaN NaN
# 2 NaN  NaN NaN
# 3 NaN  6.5   3
#dropna默认丢弃任何包含缺失值的行
clearned = data.dropna()
print  clearned
#    0    1  2
# 0  1  6.5  3

#丢弃全为NA的行
print data.dropna(how='all')
#     0    1   2
# 0   1  6.5   3
# 1   1  NaN NaN
# 3 NaN  6.5   3

data[4] = NA #增加一列全为NA

print data
#     0    1   2   4
# 0   1  6.5   3 NaN
# 1   1  NaN NaN NaN
# 2 NaN  NaN NaN NaN
# 3 NaN  6.5   3 NaN

#丢弃全为NA的列
print data.dropna(axis=1,how='all')
#     0    1   2
# 0   1  6.5   3
# 1   1  NaN NaN
# 2 NaN  NaN NaN
# 3 NaN  6.5   3


df = DataFrame(np.random.randn(7,3))

print df
#           0         1         2
# 0  0.620169  0.378666  0.013958
# 1  0.544203 -2.797935 -0.146667
# 2 -0.391113  0.118644  1.143877
# 3  0.043813 -1.352906 -0.669217
# 4  0.609801 -0.026924 -0.897324
# 5 -0.120746 -0.740429  1.873651
# 6 -1.869579  0.647781  0.847330

#修改df 的值
df.ix[:4,1] = NA
df.ix[:2,2] = NA

print df
#           0         1         2
# 0  0.620169       NaN       NaN
# 1  0.544203       NaN       NaN
# 2 -0.391113       NaN       NaN
# 3  0.043813       NaN -0.669217
# 4  0.609801       NaN -0.897324
# 5 -0.120746 -0.740429  1.873651
# 6 -1.869579  0.647781  0.847330
print df.dropna(thresh = 3)
#           0         1         2
# 5 -0.120746 -0.740429  1.873651
# 6 -1.869579  0.647781  0.847330

print  df.fillna(0)
#           0         1         2
# 0 -0.815721  0.000000  0.000000
# 1  0.731258  0.000000  0.000000
# 2 -0.353779  0.000000  0.000000
# 3 -0.615694  0.000000 -2.609451
# 4 -0.102512  0.000000 -0.262278
# 5 -1.299278 -0.644710  0.199023
# 6 -0.401930  0.222801  0.423307

#传入字典调用fillna 就可以实现不同咧填充不同的值
print df.fillna({1:0.5,3:-1})
#           0         1         2
# 0 -0.815721  0.500000       NaN
# 1  0.731258  0.500000       NaN
# 2 -0.353779  0.500000       NaN
# 3 -0.615694  0.500000 -2.609451
# 4 -0.102512  0.500000 -0.262278
# 5 -1.299278 -0.644710  0.199023
# 6 -0.401930  0.222801  0.423307


_ = df.fillna(0,inplace =True)

print df
#           0         1         2
# 0  0.327929  0.000000  0.000000
# 1  0.947866  0.000000  0.000000
# 2  0.500385  0.000000  0.000000
# 3  0.112684  0.000000  0.054383
# 4  0.936247  0.000000 -0.028059
# 5 -0.855149 -1.036161 -1.009728
# 6  0.709668 -0.716617  0.404419





df = DataFrame(np.random.randn(6,3))
#修改值，第1列的值从第3行往后；第3列的值从第5行往后
df.ix[2:,1]= NA ; df.ix[4:,2] =NA
print df
#         0         1         2
# 0  1.301645  0.138063  1.644963
# 1 -0.721405 -0.527435 -0.193673
# 2  1.021260       NaN  1.448817
# 3  0.052743       NaN -0.452761
# 4 -0.491144       NaN       NaN
# 5  1.189178       NaN       NaN

print df.fillna(method='ffill')
#           0         1         2
# 0  1.301645  0.138063  1.644963
# 1 -0.721405 -0.527435 -0.193673
# 2  1.021260 -0.527435  1.448817
# 3  0.052743 -0.527435 -0.452761
# 4 -0.491144 -0.527435 -0.452761
# 5  1.189178 -0.527435 -0.452761

print df.fillna(method='ffill',limit =2)
#           0         1         2
# 0  1.301645  0.138063  1.644963
# 1 -0.721405 -0.527435 -0.193673
# 2  1.021260 -0.527435  1.448817
# 3  0.052743 -0.527435 -0.452761
# 4 -0.491144       NaN -0.452761
# 5  1.189178       NaN -0.452761

data = Series([1.,NA,3.5,NA,7])
print data.fillna(data.mean())
# 0    1.000000
# 1    3.833333
# 2    3.500000
# 3    3.833333
# 4    7.000000


print '##################################'

data = Series(np.random.randn(10),index = [['a','a','a','b','b','b','c','c','d','d'],
                                           [1,2,3,1,2,3,1,2,2,3]])
#muitiIndex索引测Series的输出
print data
# a  1    0.858505
#    2    1.254640
#    3    0.594225
# b  1    0.223066
#    2   -1.367153
#    3    0.016382
# c  1   -0.132952
#    2   -0.195518
# d  2    0.183337
#    3   -0.997409
#输出索引
print data.index
# array([('a', 1L), ('a', 2L), ('a', 3L), ('b', 1L), ('b', 2L), ('b', 3L),
#        ('c', 1L), ('c', 2L), ('d', 2L), ('d', 3L)], dtype=object)
#选取数据集子集
print data['b']
# 1    0.223066
# 2   -1.367153
# 3    0.016382
print data['b':'d']
# b  1    0.223066
#    2   -1.367153
#    3    0.016382
# c  1   -0.132952
#    2   -0.195518
# d  2    0.183337
#    3   -0.997409
print data.ix[['b','d']]
# b  1    0.223066
#    2   -1.367153
#    3    0.016382
# d  2    0.183337
#    3   -0.997409

#根据内层索引进行选择
print data[:,2]
# a    1.254640
# b   -1.367153
# c   -0.195518
# d    0.183337

#使用unstack转成DF
print data.unstack()
#           1         2         3
# a  0.858505  1.254640  0.594225
# b  0.223066 -1.367153  0.016382
# c -0.132952 -0.195518       NaN
# d       NaN  0.183337 -0.997409
#unstack的逆运算是stack
print data.unstack().stack()
# a  1    0.858505
#    2    1.254640
#    3    0.594225
# b  1    0.223066
#    2   -1.367153
#    3    0.016382
# c  1   -0.132952
#    2   -0.195518
# d  2    0.183337
#    3   -0.997409

#DataFrame

frame = DataFrame(np.arange(12).reshape((4,3)),
                  index = [['a','a','b','b'],[1,2,1,2]],
                  columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
print  frame
#       Ohio       Colorado
#      Green  Red     Green
# a 1      0    1         2
#   2      3    4         5
# b 1      6    7         8
#   2      9   10        11

#为各层所有指定名称。
frame.index.names = ['key1','key2']

frame.columns.names=['state','color']
print frame
# state       Ohio       Colorado
# color      Green  Red     Green
# key1 key2
# a    1         0    1         2
#      2         3    4         5
# b    1         6    7         8
#      2         9   10        11

#使用列索引选取列分组

print frame['Ohio']
# color      Green  Red
# key1 key2
# a    1         0    1
#      2         3    4
# b    1         6    7
#      2         9   10

#单独创建MultiIndex可以复用。如：
#MultiIndex.from_arrays([['Ohio','Ohio','Colorado'],['Green','Red','Green']],
#                       names=['state','color'])

print '##############################################'

print frame
# state       Ohio       Colorado
# color      Green  Red     Green
# key1 key2
# a    1         0    1         2
#      2         3    4         5
# b    1         6    7         8
#      2         9   10        11
#互换级别
print frame.swaplevel('key1','key2')
# state       Ohio       Colorado
# color      Green  Red     Green
# key2 key1
# 1    a         0    1         2
# 2    a         3    4         5
# 1    b         6    7         8
# 2    b         9   10        11

#sortlevel根据单个级别中的值对数据进行排序。

#按key2排序
print frame.sortlevel(1)
# state       Ohio       Colorado
# color      Green  Red     Green
# key1 key2
# a    1         0    1         2
# b    1         6    7         8
# a    2         3    4         5
# b    2         9   10        11
print frame.swaplevel(0,1).sortlevel()
# state       Ohio       Colorado
# color      Green  Red     Green
# key2 key1
# 1    a         0    1         2
#      b         6    7         8
# 2    a         3    4         5
#      b         9   10        11

print'#########################'

#按key2来聚合行
print frame.sum(level ='key2')
# state   Ohio       Colorado
# color  Green  Red     Green
# key2
# 1          6    8        10
# 2         12   14        16

#按列聚合列
print frame.sum(level='color',axis = 1)
# key1 key2
# a    1         2    1
#      2         8    4
# b    1        14    7
#      2        20   10

print '######################################'

frame = DataFrame({'a':range(7),'b':range(7,0,-1),
                   'c':['one','one','one','two','two','two','two'],
                   'd':[0,1,2,0,1,2,3]})

print frame
#    a  b    c  d
# 0  0  7  one  0
# 1  1  6  one  1
# 2  2  5  one  2
# 3  3  4  two  0
# 4  4  3  two  1
# 5  5  2  two  2
# 6  6  1  two  3
#set_index函数将列转成行的索引，并创建一个新的df
frame2 = frame.set_index(['c','d'])

print frame2
#        a  b
# c   d
# one 0  0  7
#     1  1  6
#     2  2  5
# two 0  3  4
#     1  4  3
#     2  5  2
#     3  6  1

#默认转换后，列会从df中移除。但也可以保存下来

print frame.set_index(['c','d'],drop=False)
#        a  b    c  d
# c   d
# one 0  0  7  one  0
#     1  1  6  one  1
#     2  2  5  one  2
# two 0  3  4  two  0
#     1  4  3  two  1
#     2  5  2  two  2
#     3  6  1  two  3


#reset_index与set_index相反，层次或索的级别会被转移到列里面

print frame2.reset_index()
#      c  d  a  b
# 0  one  0  0  7
# 1  one  1  1  6
# 2  one  2  2  5
# 3  two  0  3  4
# 4  two  1  4  3
# 5  two  2  5  2
# 6  two  3  6  1


print  '#####################################'

ser = Series(np.arange(3.))
print ser
# 0    0
# 1    1
# 2    2
#print ser[-1]  #报错

ser2 =Series(np.arange(3.),index= ['a','b','c'])
print ser2
# a    0
# b    1
# c    2
#获取索引
print  ser2[-1]
# 2.0
print ser2['c']
# 2.0
print ser2[2]
# 2.0

#通过索引获取值
print ser.ix[:1]
# 0    0
# 1    1

#series的iget_value只基于位置的索引
ser3 = Series(range(3),index=[-5,1 ,3])
print ser3.iget_value(2)
# 2
#
frame = DataFrame(np.arange(6).reshape(3,2),index=[2,0,1])

print frame
#    0  1
# 2  0  1
# 0  2  3
# 1  4  5
#获取第一行
print  frame.irow(0)
# 0    0
# 1    1
# Name: 2









