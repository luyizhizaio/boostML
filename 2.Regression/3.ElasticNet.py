#!/usr/bin/python
# -*- coding:utf-8 -*-

#数据集特征升维测试，pipeline使用



import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,RidgeCV,LassoCV,ElasticNetCV
from sklearn.model_selection import GridSearchCV
from pprint import pprint
import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.pipeline import  Pipeline
from sklearn.preprocessing import PolynomialFeatures


def xss(y, y_hat):
    y = y.ravel()
    y_hat = y_hat.ravel()
    # Version 1
    tss = ((y - np.average(y)) ** 2).sum()
    rss = ((y_hat - y) ** 2).sum()
    ess = ((y_hat - np.average(y)) ** 2).sum()
    r2 = 1 - rss / tss
    # print 'RSS:', rss, '\t ESS:', ess
    # print 'TSS:', tss, 'RSS + ESS = ', rss + ess
    tss_list.append(tss)
    rss_list.append(rss)
    ess_list.append(ess)
    ess_rss_list.append(rss + ess)
    # Version 2
    # tss = np.var(y)
    # rss = np.average((y_hat - y) ** 2)
    # r2 = 1 - rss / tss
    corr_coef = np.corrcoef(y, y_hat)[0, 1]
    return r2, corr_coef


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    np.set_printoptions(suppress=True)

    warnings.filterwarnings(action='ignore',category=ConvergenceWarning)

    #根据一元二次方程，造9个点x; y并加上一点噪声。
    np.random.seed(0)
    np.set_printoptions(linewidth=1000)
    N = 9
    x = np.linspace(0,6,N) +np.random.rand(N)
    x = np.sort(x) #对x排序
    y = x**2-4*x -3 +np.random.randn(N)

    x.shape=-1,1
    y.shape = -1,1

    #model

    models = [
        Pipeline([
        ('poly',PolynomialFeatures()), #PolynomialFeatures用于多项式特征升维，[a, b], the degree-2 polynomial features are [1, a, b, a^2, ab, b^2]
        ('linear',LinearRegression(fit_intercept=False))
        ]),
        Pipeline([
            ('poly',PolynomialFeatures()),
            ('linear',RidgeCV(alphas=np.logspace(-3,2,50),fit_intercept=False))
        ]),
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', LassoCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))
        ]),
        Pipeline([
            ('poly', PolynomialFeatures()),
            ('linear', ElasticNetCV(alphas=np.logspace(-3, 2, 50), fit_intercept=False))
        ])
    ]

    plt.figure(figsize=(18,12),facecolor='w')
    d_pool=np.arange(1,N,1) #阶数
    m = d_pool.size
    clrs=[] #颜色
    for c in np.linspace(16711680,255,m):
        clrs.append('#%06x' % c)

    line_width = np.linspace(5,2,m)
    titles = u'线性回归',u'Ridge回归',u'LASSO',U'ElasticNet'
    tss_list=[]
    rss_list=[]
    ess_list=[]
    ess_rss_list=[]
    #遍历训练每个model
    for t in range(4):
        model = models[t]
        plt.subplot(2,2,t+1)
        plt.plot(x, y, 'ro',ms=10,zorder=N)
        for i,d in enumerate(d_pool):
            model.set_params(poly__degree=d) #给pipeline中poly 设置degree
            model.fit(x,y.ravel()) #训练模型 ,ravel:将多维数组转换为一维数组
            lin = model.get_params('linear')['linear'] #从pipeline中获取线性回归函数
            output = u'%s：%d阶，系数为：' % (titles[t], d)
            if hasattr(lin,'alpha_'):
                idx = output.find(u'系数')
                output= output[:idx] +( u'alpha=%.6f,'% lin.alpha_) +output[idx:]
            if hasattr(lin,'l1_ratio_'): # 根据交叉验证结果，从输入l1_ratio(list)中选择的最优l1_ratio_(float)
                idx = output.find(u'系数')
                output = output[:idx] + (u'l1_ratio=%.6f,' % lin.l1_ratio_) + output[idx:]
            print output,lin.coef_.ravel()

            #测试数据
            x_hat = np.linspace(x.min(),x.max(),num=100)
            x_hat.shape =-1 ,1
            y_hat = model.predict(x_hat)
            s= model.score(x,y)
            r2, corr_coef = xss(y, model.predict(x))

            z= N-1 if(d ==2) else 0
            label = u'%d阶，$R^2=%.3f' %(d,s)
            if hasattr(lin ,'l1_ratio_'):
                label += u' ,L1 ratio=%.2f' % lin.l1_ratio_
            plt.plot(x_hat,y_hat,color=clrs[i],lw = line_width[i],alpha=0.75,label=label,zorder=z)
        plt.legend(loc ='best')
        plt.grid(True)
        plt.title(titles[t],fontsize=18)
        plt.xlabel('X',fontsize=18)
        plt.ylabel('Y',fontsize=18)
    plt.tight_layout(1,rect=(0,0,1,0.95))
    plt.suptitle(u'多项式曲线拟合比较',fontsize=22)
    plt.show()

    y_max = max(max(tss_list), max(ess_rss_list)) * 1.05
    plt.figure(figsize=(9, 7), facecolor='w')
    t = np.arange(len(tss_list))
    plt.plot(t, tss_list, 'ro-', lw=2, label=u'TSS(Total Sum of Squares)')
    plt.plot(t, ess_list, 'mo-', lw=1, label=u'ESS(Explained Sum of Squares)')
    plt.plot(t, rss_list, 'bo-', lw=1, label=u'RSS(Residual Sum of Squares)')
    plt.plot(t, ess_rss_list, 'go-', lw=2, label=u'ESS+RSS')
    plt.ylim((0, y_max))
    plt.legend(loc='center right')
    plt.xlabel(u'实验：线性回归/Ridge/LASSO/Elastic Net', fontsize=15)
    plt.ylabel(u'XSS值', fontsize=15)
    plt.title(u'总平方和TSS=？', fontsize=18)
    plt.grid(True)
    plt.show()










