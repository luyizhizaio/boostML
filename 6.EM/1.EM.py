# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from scipy.stats import multivariate_normal
from sklearn.mixture import GaussianMixture
from mpl_toolkits.mplot3d import Axes3D #画3d图库
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances_argmin


mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False



#EM算法介绍，em算法实现



if __name__ =="__main__":

    style='self'
    np.set_printoptions(suppress=True)
    #造数据
    np.random.seed(0)
    mu1_fact =(0,0,0) #均值
    cov1_fact = np.diag((1,2,3)) #方差对角阵
    data1 = np.random.multivariate_normal(mu1_fact,cov1_fact,400) #生成多元正态数据
    print data1

    mu2_fact = (2,2,1)
    cov2_fact=np.array(((1,1,3,), (1,2,1), (0,0,1)))
    data2 = np.random.multivariate_normal(mu2_fact,cov2_fact,100)

    data = np.vstack((data1,data2))
    y = np.array([True] * 400 + [False] * 100)

    if style == 'sklearn': #sklearn 提供的em算法
        #参数：n_components:类别个数；covariance_type
        #2. covariance_type:协方差类型，包括{‘full’,‘tied’, ‘diag’, ‘spherical’}四种，分别对应完全协方差矩阵（元素都不为零），相同的完全协方差矩阵（HMM会用到），对角协方差矩阵（非对角为零，对角不为零），球面协方差矩阵（非对角为零，对角完全相同，球面特性），默认‘full’ 完全协方差矩阵
        #3. tol：EM迭代停止阈值，默认为1e-3.
        #4. reg_covar:协方差对角非负正则化，保证协方差矩阵均为正，默认为0
        #5. max_iter:最大迭代次数，默认100
        g = GaussianMixture(n_components=2,covariance_type='full',tol=1e-6,max_iter=1000)
        g.fit(data)

        print '类别概率：\t',g.weights_ #两个分类的概率
        print '均值：\t',g.means_,'\n'
        print '方差：\t',g.covariances_,'\n'

        mu1,mu2 = g.means_
        sigma1,sigma2 = g.covariances_
    else: #手动实现GM
        num_iter=100
        n,d = data.shape

        #设置初始均值，方差
        mu1 = data.min(axis=0)
        mu2 = data.max(axis=0)
        sigma1 = np.identity(d)
        sigma2 = np.identity(d)
        pi = 0.5
        #EM 迭代
        for i in range(num_iter):
            # E Step
            norm1 = multivariate_normal(mu1, sigma1)
            norm2 = multivariate_normal(mu2, sigma2)
            tau1 = pi * norm1.pdf(data)
            tau2 = (1 - pi) * norm2.pdf(data)
            gamma = tau1 / (tau1 + tau2)

            # M Step
            mu1 = np.dot(gamma, data) / np.sum(gamma)
            mu2 = np.dot((1 - gamma), data) / np.sum((1 - gamma))
            sigma1 = np.dot(gamma * (data - mu1).T, data - mu1) / np.sum(gamma)
            sigma2 = np.dot((1 - gamma) * (data - mu2).T, data - mu2) / np.sum(1 - gamma)
            pi = np.sum(gamma) / n
            print i, ":\t", mu1, mu2
        print '类别概率:\t', pi
        print '均值:\t', mu1, mu2
        print '方差:\n', sigma1, '\n\n', sigma2, '\n'

    #预测分类
    #根据预测的均值，方差
    norm1 = multivariate_normal(mu1, sigma1) #返回分布对象。
    print 'norm1=\n',norm1
    norm2 = multivariate_normal(mu2, sigma2)
    tau1 = norm1.pdf(data) #返回数据属于此分布的概率
    tau2 = norm2.pdf(data)

    print 'tau1=\n',tau1


    fig = plt.figure(figsize=(13, 7), facecolor='w')
    ax = fig.add_subplot(121, projection='3d') #指定为3d图像
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='b', s=30, marker='o', depthshade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(u'原始数据', fontsize=18)
    ax = fig.add_subplot(122, projection='3d')

    #pairwise_distances_argmin使用欧几里得距离,返回的是X距离Y最近点的index，
    order = pairwise_distances_argmin([mu1_fact, mu2_fact], [mu1, mu2], metric='euclidean')
    print order
    if order[0] == 0:
        c1 = tau1 > tau2 #tau 返回的是属于各分类的概率
    else:
        c1 = tau1 < tau2
    c2 = ~c1 #取反

    acc = np.mean(y == c1) #返回条件成立的占比
    print u'准确率：%.2f%%' % (100 * acc)
    #第一个分类点
    ax.scatter(data[c1, 0], data[c1, 1], data[c1, 2], c='r', s=30, marker='o', depthshade=True)
    #第二个分类点
    ax.scatter(data[c2, 0], data[c2, 1], data[c2, 2], c='g', s=30, marker='^', depthshade=True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(u'EM算法分类', fontsize=18)
    plt.suptitle(u'EM算法的实现', fontsize=21)
    plt.subplots_adjust(top=0.90)
    plt.tight_layout()
    plt.show()

























