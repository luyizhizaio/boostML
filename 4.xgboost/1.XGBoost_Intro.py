# /usr/bin/python
# -*- encoding:utf-8 -*-



#xgboost 的简单使用

import xgboost as xgb
import numpy as np

# 1、xgBoost的基本使用
# 2、自定义损失函数的梯度和二阶导
# 3、binary:logistic/logitraw
# /usr/bin/python
# -*- encoding:utf-8 -*-

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split   # cross_validation


def log_reg(y_hat,y):
    p = 1.0/(1.0 + np.exp(-y_hat))
    g = p - y.get_label()
    h = p * (1.0-p)
    return g, h
def error_rate(y_hat, y):
    return 'error', float(sum(y.get_label() != (y_hat > 0.5))) / len(y_hat)




if __name__ =="__main__":

    #读取数据，稀疏矩阵
    data_train=xgb.DMatrix('../data/agaricus_train.txt')
    data_test=xgb.DMatrix('../data/agaricus_test.txt')
    print data_train
    print type(data_train)

    #设置参数:max_depth 指定最大深度，eta：为了防止过拟合，更新过程中用到的收缩步长。 objective:指定算法一阶，二阶导的计算方式
    param = {'max_depth':3,'eta':1,'silent':1,'objective':'binary:logistic'}
    wacthlist = [(data_test,'eval'),(data_train,'train')] #检测训练效果
    n_round=7
    #num_boost_round：迭代次数； obj :Customized objective function. feval :Customized evaluation function.
    #bst = xgb.train(param,data_train,num_boost_round=n_round,evals=wacthlist)
    bst = xgb.train(param, data_train, num_boost_round=n_round, evals=wacthlist,obj =log_reg , feval=error_rate )


    y_hat = bst.predict(data_test)
    y = data_test.get_label()

    print 'y_hat=\n',y_hat
    print 'y=\n',
    error = sum(y!=(y_hat > 0.5))
    error_rate = float(error)/len(y_hat)
    print '样本总数：\t', len(y_hat)
    print '错误数目：\t%4d' % error
    print '错误率：\t%.5f%%' % (100 * error_rate)













