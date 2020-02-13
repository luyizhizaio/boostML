#!/usr/bin/python
# -*- coding:utf-8 -*-

#广告预测案例

import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pprint import pprint



if __name__ == "__main__":
    #1.读取数据
    path = 'data/Advertising.csv'

    #pandas读入
    data =pd.read_csv(path)
    #x = data[['TV','Radio','Newspaper']]
    x = data[['TV','Radio']]
    y = data['Sales']
    print x
    print y

    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    #2.绘图
    #特征与结果相关图
    plt.figure(facecolor='w')
    plt.plot(data['TV'],y,'ro',label='TV')
    plt.plot(data['Radio'],y,'g^',label='Radio') #绿色上三角
    plt.plot(data['Newspaper'],y,'mv',label='Newspaper') #紫色下三角
    plt.legend(loc='lower right')
    plt.xlabel(u'广告花费',fontsize=16)
    plt.ylabel(u'销售额',fontsize=16)
    plt.title(u'广告花费与销售额对比数据',fontsize=20)
    plt.grid()
    plt.show()

    #每个特征与y的子图
    plt.figure(facecolor='w',figsize=(9,10))

    plt.subplot(311)#创建子图,3行1列第1个图
    plt.plot(data['TV'],y,'ro')
    plt.title('TV')
    plt.grid()

    plt.subplot(312)
    plt.plot(data['Radio'],y,'g^')
    plt.title('Radio')
    plt.grid()

    plt.subplot(313)
    plt.plot(data['Newspaper'],y,'b*')
    plt.title('Newspaper')
    plt.grid()

    plt.tight_layout()
    plt.show()


    #3.模型训练
    #切分测试集和训练集 。random_state指定随机种子保证每次随机结果相同。
    x_train, x_test,y_train,y_test =train_test_split(x,y,train_size=0.8,random_state=1)
    print type(x_test)
    print x_train.shape, x_train.shape

    linreg = LinearRegression()
    model = linreg.fit(x_train,y_train)
    print model
    # linreg.coef_ :为特征前面的系数theta; linreg.intercept_ 为系数theta0
    print linreg.coef_,linreg.intercept_

    order = y_test.argsort(axis=0) #argsort函数返回的是数组值从小到大的索引值
    print 'order=\n',order
    y_test = y_test.values[order] #按order 排序
    x_test = x_test.values[order,:] #行按order 排序
    y_hat = linreg.predict(x_test)

    mse = np.average((y_hat - np.array(y_test)) **2) #Mean Squared Error
    rmse = np.sqrt(mse) #Root Mean Squared Error

    print 'MSE = ',mse
    print 'RMSE = ',rmse
    #R2:评估拟合效果好坏，一般越大越好。
    print 'R2 = ',linreg.score(x_train,y_train)
    print 'R2 = ',linreg.score(x_test,y_test)


    plt.figure(facecolor='w')
    t = np.arange(len(x_test))
    plt.plot(t,y_test,'r-',linewidth=2,label=u'真实数据')
    plt.plot(t,y_hat,'g-',linewidth=2,label=u'预测数据')
    plt.legend(loc='upper right')
    plt.title(u'线性回归预测销量',fontsize=18)
    plt.grid(b=True)
    plt.show()




