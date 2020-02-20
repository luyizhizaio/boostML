# /usr/bin/python
# -*- coding:utf-8 -*-

import xgboost as xgb
import numpy as np
import scipy.sparse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#读取稀疏矩阵的数据
def read_data(path):
    y = []
    row=[]
    col=[]
    values = []
    r =0
    for d in open(path):
        d = d.strip().split() # strip:移除字符串头尾指定的字符。
        y.append(int(d[0]))
        d =d[1:]
        for c in d:
            key,value = c.split(':')
            row.append(r)
            col.append(int(key))
            values.append(float(value))
        r+=1
    x = scipy.sparse.csr_matrix((values,(row,col))).toarray() #读取稀疏矩阵转成正常的矩阵
    y = np.array(y)
    return x,y



if __name__ == '__main__':
    x,y=read_data('../data/agaricus_train.txt')

    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,train_size=0.6)

    #Logistic 回归
    lr = LogisticRegression(penalty='l2')
    lr.fit(x_train,y_train.ravel())
    y_hat = lr.predict(x_test)
    print 'lr auc',accuracy_score(y_test,y_hat)

    #xgboost
    data_train = xgb.DMatrix(x_train,label=y_train)
    data_test = xgb.DMatrix(x_test,label=y_test)
    watch_list = [(data_test, 'eval'), (data_train, 'train')]
    param = {'max_depth': 3, 'eta': 1, 'silent': 0, 'objective': 'multi:softmax', 'num_class': 3}
    bst = xgb.train(param, data_train, num_boost_round=4, evals=watch_list)
    y_hat = bst.predict(data_test)
    print 'XGBoost正确率：', accuracy_score(y_test, y_hat)



