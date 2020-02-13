#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

from scipy.special import cbrt


if __name__ == "__main__":

    #1.特殊函数
    # #立方根函数
    res = cbrt([1000,27,8,23])
    print res

    #2.线性代数

    #线性方程组求解
    from scipy import linalg

    a = np.array([[1,3,5],[2,5,1],[2,3,8]])
    b= np.array([10,8,3])
    x = linalg.solve(a,b)
    print x
    #计算行列式
    A = np.array([[3,4],[7,8]])
    x = linalg.det(A)
    print x
    #求特征值与特征向量
    ##scipy.linalg.eig 函数可用于计算特征值与特征向量，函数返回特征值和特征向量
    A = np.array([[3, 6], [4, 8]])
    l,v = linalg.eig(A)
    print '特征值',l
    print '特征向量',v

    #SVD奇异值分解
    A = np.random.randn(3,2)+ 1.j *np.random.randn(3,2)
    print '原矩阵=\n',A

    U,s,Vh = linalg.svd(A)
    print '奇异值分解'
    print 'U=\n',U
    print 'Vh=\n',Vh
    print 's=\n',s

    #2.优化
    #优化是指在某些约束条件下，求解目标函数最优解的过程。机器学习、人工智能中的绝大部分问题都会涉及到求解优化问题。
    #SciPy的optimize模块提供了许多常用的数值优化算法，一些经典的优化算法包括线性回归、函数极值和根的求解以及确定两函数交点的坐标等。

    from scipy import optimize

    #2.1使用bfgs算法求函数极小值

    def f(x):
        return x ** 2 + 2*x +9

    x = np.arange(-10,10,0.1)
    plt.plot(x, f(x))
    #plt.show()
    #计算该函数最小值的有效方法之一是使用带起点的BFGS算法。
    # 该算法从参数给定的起始点计算函数的梯度下降，并输出梯度为零、二阶导数为正的极小值。
    # BFGS算法是由Broyden，Fletcher，Goldfarb，Shanno四个人分别提出的，故称为BFGS校正。

    #注意：fmin_bfgs有个问题，当函数有局部最小值，该算法会因起始点不同，找到这些局部最小而不是全局最小。

    # 第一个参数是函数名，第二个参数是梯度下降的起点。返回值是函数最小值的x值(ndarray数组)
    xopt= optimize.fmin_bfgs(f,0)

    xmin = xopt[0]  # x值
    ymin = f(xmin)  # y值，即函数最小值
    print('xmin: ', xmin)
    print('ymin: ', ymin)

    # 画出最小值的点, s=20设置点的大小，c='r'设置点的颜色
    plt.scatter(xmin,ymin,s=20,c='r')
    plt.show()


    #2.2 拟合
    #假设有一批数据样本，要创建这些样本数据的拟合曲线/函数，可以使用Scipy.optimize模块的curve_fit()函数。

    #函数模型用于生成数据
    def g(x,a,b):
        return a * np.cos(x) +b

    #产生含有噪声的样本数据
    x_data = np.linspace(-5,5,100) #样本点
    y_data = g(x_data,50 ,2) + 5*np.random.randn(x_data.size) #加入随机数作为噪声

    # 使用curve_fit()函数来估计a和b的值
    variables, variables_covariance = optimize.curve_fit(g,x_data,y_data)

    #输出结果：
    print '求出系数a,b:',variables
    print 'variables_covariance:',variables_covariance

    #绘图
    y = g(x_data,variables[0],variables[1])

    plt.figure()
    plt.plot(x_data,y_data,'o',color='green', label='Sample')
    plt.plot(x_data,y,'-',color='red',label= 'Fit')
    plt.legend(loc='best')
    plt.show()


    #2.3. 最小二乘法 leastsq()
    #最小二乘法是非常经典的数值优化算法，通过最小化误差的平方和来寻找最符合数据的曲线。

    #optimize.leastsq(func, x0, args=())
    #func 计算误差的函数
    #x0 是计算的初始参数值
    #args 是指定func的其他参数


    # 样本数据
    X = np.array([160, 165, 158, 172, 159, 176, 160, 162, 171])
    Y = np.array([58, 63, 57, 65, 62, 66, 58, 59, 62])


    # 偏差函数, 计算以p为参数的直线和原始数据之间的误差
    def residuals(p):
        k,b = p
        return Y -(k * X +b)

    # leastsq()使得residuals()的输出数组的平方和最小，参数的初始值为[1, 0]
    ret = optimize.leastsq(residuals,[1,10])
    k,b = ret[0]
    print 'k= ', k , 'b= ', b
    #绘图

    #画样本点
    plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
    plt.scatter(X,Y,color='green',label='Sample',linewidth=2)

    #画拟合直线
    x= np.linspace(150,190,100)
    y = k*x + b
    plt.plot(x,y,color='red',label='Fit',linewidth=2)
    plt.legend()
    plt.show()





