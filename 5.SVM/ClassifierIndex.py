#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, fbeta_score
from sklearn.metrics import precision_recall_fscore_support, classification_report



#分类评估指标
if __name__ == "__main__":

    y_true= np.array((1,1,1,1,0,0))
    y_hat= np.array((1,0,1,1,1,1))

    print 'accuracy:\t',accuracy_score(y_true,y_hat)



    precision = precision_score(y_true,y_hat)
    print 'precision\t',precision

    recall = recall_score(y_true,y_hat)
    print 'recall\t',recall

    print 'f1 score:\t',f1_score(y_true,y_hat)
    print 2 * (precision * recall) /(precision+recall)

    print 'F-beta:'
    for beta in np.logspace(-3,3,num=7,base=10):
        fbeta = fbeta_score(y_true,y_hat,beta=beta)
        print '\tbeta=%9.3f\tF-beta=%.5f' % (beta,fbeta)

    print precision_recall_fscore_support(y_true, y_hat, beta=1) #为每个类计算precision, recall, F-measure 和 support
    print classification_report(y_true, y_hat) #在报告中显示每个类的精确度，召回率，F1值等信息













