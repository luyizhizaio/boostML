__author__ = 'dayue'
#-*-coding:utf-8 -*-


import numpy as np

#
data1 = [6,7.5,8,1,0]

arr1 = np.array(data1)

print arr1
# [ 6.   7.5  8.   1.   0. ]

#多维数组
data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

print arr2

# [[1 2 3 4]
#  [5 6 7 8]]

print arr2.ndim
# 2
print arr2.shape
# (2,4)
print arr2.dtype
# int32

#zeros

print np.zeros(10)
# [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
print np.zeros((3,6))
# [[ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  0.  0.  0.  0.]]

#empty ,返回未初始化的垃圾值
print np.empty((2,3,2))
# [[[  2.32025378e-298   6.91207026e-307]
#   [  6.91304808e-307   6.91217891e-307]
#   [  6.91326537e-307   6.94037259e-307]]
#
#  [[  6.94023679e-307   6.91402589e-307]
#   [  6.91652476e-307   6.91663340e-307]
#   [  2.57753414e-297   2.57762746e-297]]]

#arange

print np.arange(15)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

print(np.eye(3,3))
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
#

#转换数据类型
arr = np.array([1,2,3,4,5])
print arr.dtype
# int32
float_arr = arr.astype(np.float64)
print float_arr.dtype
# float64

#
arr = np.array([2.3,12,3.4,66.34])
print arr
# [  2.3   12.     3.4   66.34]
print arr.astype(np.int32)
# [ 2 12  3 66]

numeric_strings = np.array(['23.4','1.3','3.5','4.5'],dtype=np.string_)
print(numeric_strings.astype(float))
# [ 23.4   1.3   3.5   4.5]




int_array  = np.arange(10)

calibers = np.array([1.2,3.4],dtype=np.float64)
print int_array.astype(calibers.dtype)
# [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]

empt_uint32 = np.empty(8,dtype='u4')

print empt_uint32

##############################################
#1.3
#################
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
print arr
# [[ 1.  2.  3.]
#  [ 4.  5.  6.]]
print arr * arr
# [[  1.   4.   9.]
#  [ 16.  25.  36.]]
print arr - arr
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

###########################################

arr = np.arange(10)
print arr
# [0 1 2 3 4 5 6 7 8 9]

print arr[5]
# 5
print arr[5:8]
# [5 6 7]

arr[5:8]=12

print arr
# [ 0  1  2  3  4 12 12 12  8  9]
arr_slice = arr[5:8]
print arr_slice
# [12 12 12]
arr_slice[1]=12345
print arr
# [    0     1     2     3     4    12 12345    12     8     9]

arr_slice[:] =64

print arr
# [ 0  1  2  3  4 64 64 64  8  9]


arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr2d[2]
# [7 8 9]

print arr2d[0][2]
# 3
print arr2d[0,2]
# 3

##########################

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print arr3d
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
print arr3d[0]
# [[1 2 3]
#  [4 5 6]]


old_values = arr3d[0].copy()

arr3d[0] =42

print arr3d
# [[[42 42 42]
#   [42 42 42]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
arr3d[0]=old_values
print arr3d
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print arr3d[1,0]
# [7 8 9]


print arr2d

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

#取前两行
print arr2d[:2]
# [[1 2 3]
#  [4 5 6]]

#取前两行，第二列开始去到最后一列
print arr2d[:2,1:]
# [[2 3]
#  [5 6]]

#获取低维,获取第二行，
print arr2d[1,:2]
# [4 5]

print arr2d[2,:1]
# [7]

print arr2d[:,:1]
# [[1]
#  [4]
#  [7]]


#################################################
#1.4
########################
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

#random 7 row,4 column
data=np.random.randn(7,4)

print names
# ['Bob' 'Joe' 'Will' 'Bob' 'Will' 'Joe' 'Joe']

print data

# [[-0.31400713  0.4284348   0.08883076 -2.25661448]
#  [-0.19626483  0.71538327 -0.32030563 -0.19724369]
#  [-0.67603714  0.72262333 -0.691133    0.56022726]
#  [ 0.96009114  0.27392395 -0.15204699  0.2911856 ]
#  [-0.86629122  0.4426488  -1.70531403  1.14644169]
#  [-1.72510475  0.58747375  0.02791025 -1.01970017]
#  [-1.68373068  0.65263205  0.09392008  0.16927648]]

print names =='Bob'
# [ True False False  True False False False]

#获取names中为true对应的行
print data[names == 'Bob']
# [[ 0.96365619  1.39912012 -1.35650884 -0.28537048]
#  [ 1.06931292 -1.00216848 -0.36198363  1.35166752]]

#names='Bob'的两行中，从第3列取到最后
print data[names =='Bob',2:]
# [[-1.35650884 -0.28537048]
#  [-0.36198363  1.35166752]]

#names='Bob'的两行中，取第4列
print data[names=='Bob' ,3]
# [-0.28537048  1.35166752]

print names!='Bob'
# [False  True  True False  True  True  True]

#除Bob以外的其他数据 用-号，！= 判断
print data[-(names =='Bob')]
# [[ 0.3609646  -1.25176737  0.66481004  1.18104394]
#  [ 0.54353436 -0.91161098  1.03672862  1.25544859]
#  [-1.17713971 -0.63433009  1.40112267  2.02060903]
#  [ 1.97176004  0.06045939  1.09896991 -2.38654367]
#  [-2.00025146 -1.20368311 -0.30211953 -0.68584022]]

#names 中=Bob或等于will,   &表示与，|表示或
mask = (names =='Bob')| (names =='Will')

print mask
# [ True False  True  True  True False False]


print data[mask]
# [[ 1.97362277  0.42078822 -0.76105234 -0.78686712]
#  [ 0.54353436 -0.91161098  1.03672862  1.25544859]
#  [ 0.2868479   0.71385537 -0.42802694 -0.70474016]
#  [-1.17713971 -0.63433009  1.40112267  2.02060903]]
#赋值， 报错
# print data[data < 0 ] =0
# print data[names !='Joe'] =7
#################################################################
#1.6.花式索引
###################

print '###########################################'

arr = np.empty((8,4))


for i in range(8):
    arr[i] = i

print arr
# [[ 0.  0.  0.  0.]
#  [ 1.  1.  1.  1.]
#  [ 2.  2.  2.  2.]
#  [ 3.  3.  3.  3.]
#  [ 4.  4.  4.  4.]
#  [ 5.  5.  5.  5.]
#  [ 6.  6.  6.  6.]
#  [ 7.  7.  7.  7.]]

#特定顺序选取行子集,指定行号

print arr[[4,3,0,6]]
# [[ 4.  4.  4.  4.]
#  [ 3.  3.  3.  3.]
#  [ 0.  0.  0.  0.]
#  [ 6.  6.  6.  6.]]

print arr[[-3,-5, -7]]
# [[ 5.  5.  5.  5.]
#  [ 3.  3.  3.  3.]
#  [ 1.  1.  1.  1.]]

#
arr = np.arange(32).reshape((8,4))

print arr
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  [24 25 26 27]
#  [28 29 30 31]]

print arr[[1,5,7,2],[0,3,1,2]]

# [ 4 23 29 10]

#np.ix_函数就是在输入的两个列表间产生笛卡尔积映射关系：
print arr[np.ix_([1,5,7,2],[0,3,1,2])]
# [[ 4  7  5  6]
#  [20 23 21 22]
#  [28 31 29 30]
#  [ 8 11  9 10]]
############################################################################

arr = np.arange(15).reshape((3,5))
print arr
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

print arr.T

# [[ 0  5 10]
#  [ 1  6 11]
#  [ 2  7 12]
#  [ 3  8 13]
#  [ 4  9 14]]

#利用 np.dot计算矩阵内积XTX
arr =np.random.randn(6,3)

print np.dot(arr.T,arr)
# [[ 6.79574455  0.40137859  3.70773797]
#  [ 0.40137859  3.95496915  1.48774406]
#  [ 3.70773797  1.48774406  9.88648052]]



arr = np.arange(16).reshape((2,2,4))
print arr
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]
#
#  [[ 8  9 10 11]
#   [12 13 14 15]]]

print arr.transpose((1,0,2))
# [[[ 0  1  2  3]
#   [ 8  9 10 11]]
#
#  [[ 4  5  6  7]
#   [12 13 14 15]]]
#

print  arr
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]
#
#  [[ 8  9 10 11]
#   [12 13 14 15]]]
print arr.swapaxes(1,2)
# [[[ 0  4]
#   [ 1  5]
#   [ 2  6]
#   [ 3  7]]
#
#  [[ 8 12]
#   [ 9 13]
#   [10 14]
#   [11 15]]]








































