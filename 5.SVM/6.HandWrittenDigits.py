#!/usr/bin/python
# -*- coding:utf-8 -*-




import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.colors
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import accuracy_score
import os
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from time import time

#s识别手写数字



if __name__ == "__main__":
    #每行代表一个8*8图片的像素，每行最后一个数字代表手写的数字
    data  = np.loadtxt('../data/optdigits.tra',dtype=np.float,delimiter=',')
    x,y = np.split(data,(-1,),axis=1)
    images = x.reshape(-1,8,8)
    y = y.ravel().astype(np.int)

    data = np.loadtxt('../data/optdigits.tes', dtype=np.float, delimiter=',')
    x_test, y_test = np.split(data, (-1,), axis=1)
    images_test = x_test.reshape(-1, 8, 8)
    y_test = y_test.ravel().astype(np.int)

    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(15,9),facecolor='w')

    for index,image in enumerate(images[:16]):
        plt.subplot(4,8,index+1)
        plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
        plt.title(u'训练图片：%i' % y[index])
    for index,image in enumerate(images_test[:16]):
        plt.subplot(4,8,index+17)
        plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
        plt.title(u'测试图片：%i' % y[index])

    plt.tight_layout()
    plt.show()


    model = svm.SVC(C=10,kernel='rbf',gamma = 0.001)
    t0 =time()
    model.fit(x,y)
    t1 = time()
    t = t1- t0
    print '训练耗时:%d分钟%.3f秒' % (int(t/60),t- 60* int (t/60))

    print '训练集准确率：', accuracy_score(y, model.predict(x))
    y_hat = model.predict(x_test)
    print '测试集准确率：', accuracy_score(y_test, model.predict(x_test))
    print y_hat
    print y_test

    #打印判断错误的图片

    err_images = images_test[y_test != y_hat]
    err_y_hat = y_hat[y_test != y_hat]
    err_y = y_test[y_test !=y_hat]

    print err_y_hat
    print err_y

    plt.figure(figsize=(10, 8), facecolor='w')
    for index, image in enumerate(err_images):
        if index >= 12:
            break
        plt.subplot(3, 4, index + 1)
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title(u'错分为：%i，真实值：%i' % (err_y_hat[index], err_y[index]))
    plt.tight_layout()
    plt.show()

















