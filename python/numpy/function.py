#!/usr/bin/python
# -*- coding:utf-8 -*-
import matplotlib as mpl

import numpy as np

#一.函数创建数组
#1.arange
#arange函数类似于python的range函数：指定起始值、终止值和步长来创建数组
# 和Python的range类似，arange同样不包括终值；但arange可以生成浮点类型，而range只能是整数类型

# [[ 0  1  2  3  4  5]
#  [10 11 12 13 14 15]
#  [20 21 22 23 24 25]
#  [30 31 32 33 34 35]
#  [40 41 42 43 44 45]
#  [50 51 52 53 54 55]]
a = np.arange(0,60,10).reshape(-1,1) + np.arange(6)
#print a

b = np.arange(5,10,0.2).reshape(5,-1)
print b

#2.linspace
#等差数列
# linspace函数通过指定起始值、终止值和元素个数来创建数组，缺省包括终止值

a = np.linspace(2,16,8).reshape(-1,2)
print a

# # 可以通过endpoint关键字指定是否包括终值
b = np.linspace(0, 10, 10, endpoint=False)
print 'b=', b

#3.logspace
# # # 和linspace类似，logspace可以创建等比数列

#起始值为3^1终止值3^4 四个元素，base基数 默认为10
a = np.logspace(1,4,4,endpoint=True ,base=3)
print a

b = np.logspace(0,5,6,endpoint=True)
print b


#4.使用 frombuffer, fromstring, fromfile等函数可以从字节序列创建数组

s = 'abcdefgh'
#字符串转成数字
a = np.fromstring(s,dtype=np.int8)
print a

#二.存取，切片
#1.常规办法：数组元素的存取方法和Python的标准方法相同
#切片数据是原数组的一个视图，与原数组共享内容空间，可以直接修改元素值
a = np.arange(10)
print a
#获取某个元素
print a[4]
# 切片[3,5)，左闭右开
print a[3:5]
# 省略开始下标，表示从0开始
print a[:6]
# 下标为负表示从后面算下标。左闭右开
print a[-5:-1]
# # 步长为2
print a[1:9:2]
# 步长为-1，即翻转
# 步长为-1，即翻转
print a[::]
print a[::-1]


#2 整数/布尔数组存取

#2.1. 根据整数数组存取：当使用整数序列对数组元素进行存取时，
    # 将使用整数序列中的每个元素作为下标，整数序列可以是列表(list)或者数组(ndarray)。
    # 使用整数序列作为下标获得的数组不和原始数组共享数据空间。

a = np.logspace(0,9,10 ,base = 2)
print a

i = np.arange(0,10,2)
# i作为小标从a中取元素
b = a[i]
print b

#2.2. 使用布尔数组i作为下标存取数组a中的元素：返回数组a中所有在数组b中对应下标为True的元素
#生成10个满足[0,1)中均匀分布的随机数
a = np.random.rand(10)
print a
# 大于0.5的元素索引
#[False  True  True False False False False False  True False]
print a > 0.5

#获取大于0.5的元素
b = a[a > 0.5]
print b

# 将原数组中大于0.5的元素截取成0.5
a[a> 0.5] = 0.5
print a

#3.二维数组切片
