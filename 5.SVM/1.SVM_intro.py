#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



iris_feature =u'花萼长度',u'花萼宽度',u'花瓣长度',u'花瓣宽度'

if __name__ =="__main__":

    path = '../data/iris.data'
    data = pd.read_csv(path,header=None)
    x,y = data[range(4)],data[4]
    y = pd.Categorical(y).codes

    x = x[[0,1]]
    print x
    x_train,x_test,y_train,y_test = train_test_split(x, y, random_state=1, train_size=0.6)


    #分类器
    #C 指定超参松弛因子，C越大，中间区域越窄； kernel指定核函数；decision_function_shape :
    #decision_function_shape='ovr'时，为one v rest，即一个类别与其他类别进行划分，
    #decision_function_shape='ovo'时，为one v one，即将类别两两之间进行划分，用二分类的方法模拟多分类的结果。

    #clf = svm.SVC(C=0.1,kernel='linear',decision_function_shape='ovr')
    #核函数为高斯核函数时，gamma指定核函数的参数，当函数中的γ越大，锥形就越胖。
    clf = svm.SVC(C=20, kernel='rbf',gamma=20, decision_function_shape='ovr')

    clf.fit(x_train,y_train.ravel())

    print clf.score(x_train,y_train)
    print '训练集准确率', accuracy_score(y_train,clf.predict(x_train))

    print clf.score(x_test,y_test)
    print '测试集准确率：', accuracy_score(y_test,clf.predict(x_test))

    #decision_ function :计算样本点到分割超平面的函数距离,哪个大就属于哪个分类
    print 'decision_function:\n',clf.decision_function(x_train)
    print 'predict',clf.predict(x_train)

    #画图
    x1_min,x2_min = x.min()
    x1_max,x2_max = x.max()
    x1,x2 = np.mgrid[x1_min:x1_max:500j,x2_min:x2_max:500j] #s生成网络样本点
    print 'x1=\n',x1
    print 'x2=\n',x2
    grid_test = np.stack((x1.flat,x2.flat),axis=1) #转成两列矩阵
    print'grid_test=\n', grid_test

    grid_hat = clf.predict(grid_test)
    grid_hat = grid_hat.reshape(x1.shape)

    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False


    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g','r','b'])
    plt.figure(facecolor='w')
    plt.pcolormesh(x1,x2,grid_hat,cmap=cm_light)
    plt.scatter(x_train[0],x_train[1],c=y_train, edgecolors='k',s=50,cmap=cm_dark) #train
    plt.scatter(x_test[0],x_test[1], s=120,edgecolors='k', zorder=10,marker='*') #test
    plt.xlabel(iris_feature[0],fontsize = 13)
    plt.ylabel(iris_feature[1],fontsize = 13)
    plt.xlim(x1_min,x1_max)
    plt.ylim(x2_min,x2_max)
    plt.title(u'iris svm classification',fontsize = 16)
    plt.grid(b=True,ls=':')
    plt.tight_layout(pad=1.5) #边框布局
    plt.show()



















