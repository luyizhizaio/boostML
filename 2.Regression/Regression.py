#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np

#案例：实现回归算法



#1.线性回归L2正则实现
def regressionL2(data,alpha,lamda):
    n = len(data[0]) - 1
    theta = np.zeros(0) #初始theta值为0
    for times in range(100):
        for d in data:
            x = d[:-1]
            y = d[-1]
            g = np.dot(theta,x) -y
            theta = theta - alpha * g * x + lamda * theta
        print times, theta
    return theta
