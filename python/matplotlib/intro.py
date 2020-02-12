#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#matplotlib.pyplot是一个命令风格函数的集合，使matplotlib的机制更像 MATLAB
if __name__ == "__main__":
    #图片中指定中文
    mpl.rcParams['font.sans-serif'] = [u'SimHei']  #FangSong/黑体 FangSong/KaiTi
    mpl.rcParams['axes.unicode_minus'] = False


    #1.绘制正态分布函数密度函数
    # mu = 0
    # sigma = 1
    #
    # x = np.linspace(mu -3 *sigma,mu +3 * sigma ,51)
    #
    # y = np.exp(-(x - mu) ** 2/ (2 * sigma ** 2))/(math.sqrt(2 * math.pi) * sigma)
    #
    # print x.shape
    #
    # print 'x = \n', x
    # print y.shape
    # print 'y = \n' ,y
    # plt.figure(facecolor='w') #生成第一个图片，用于一次生成多张图片
    # plt.plot(x, y, 'ro-', linewidth=2)
    # plt.figure(facecolor='w') #生成第二个图片
    # plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8) #可以多次指定x，y的样式
    # plt.xlabel('X',fontsize = 15)
    # plt.xlabel('Y',fontsize = 15)
    # plt.title(u'高斯分布函数',fontsize=20)
    # plt.grid(True) #是否右网格
    # plt.show()



    #2.损失函数 ： Logistic 损失(-1,1)/ svm Hinge 损失/ 0/1损失

    # x = np.array(np.linspace(start = -2,stop = 3,num = 1001,dtype=np.float))
    #
    # y_logit = np.log(1 + np.exp(-x)) / math.log(2)
    # y_boost = np.exp(-x)
    # y_01 = x < 0
    # y_hinge= 1.0 - x
    # y_hinge[y_hinge <0] =0
    #
    # plt.plot(x,y_logit,'r-',label='Logistic Loss',linewidth =2)
    # plt.plot(x,y_01,'g-',label='0/1 Loss',linewidth=2)
    # plt.plot(x,y_hinge,'b-',label='Hinge Loss',linewidth = 2)
    # plt.plot(x,y_boost,'m--',label='Adaboost Loss', linewidth =2)
    #
    # plt.grid(True)
    # plt.legend(loc = 'upper right')
    # plt.savefig('1.png') #保存图片
    # plt.show()


    #3.验证中心极限定理
    # t = 1000
    # a = np.zeros(10000)
    # for i in range(t):
    #     a += np.random.uniform(-5, 5, 10000)
    # a /= t
    # plt.hist(a, bins=30, color='g', alpha=0.5, normed=True, label=u'均匀分布叠加') #画直方图
    # plt.legend(loc='upper left')
    # plt.grid()
    # plt.show()

    #4.Poisson分布

    # x = np.random.poisson(lam=5, size=10000)
    # print x
    # pillar = 15
    # a = plt.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
    # plt.grid()
    # plt.show()
    # print a
    # print a[0].sum()



 # 7. 绘制三维图像
    x, y = np.ogrid[-3:3:100j, -3:3:100j]
    # u = np.linspace(-3, 3, 101)
    # x, y = np.meshgrid(u, u)
    z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
    # z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm, linewidth=0.1)  #
    #ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.Accent, linewidth=0.5)
    plt.show()
    # cmaps = [('Perceptually Uniform Sequential',
    #           ['viridis', 'inferno', 'plasma', 'magma']),
    #          ('Sequential', ['Blues', 'BuGn', 'BuPu',
    #                          'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
    #                          'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
    #                          'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
    #          ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
    #                              'copper', 'gist_heat', 'gray', 'hot',
    #                              'pink', 'spring', 'summer', 'winter']),
    #          ('Diverging', ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
    #                         'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
    #                         'seismic']),
    #          ('Qualitative', ['Accent', 'Dark2', 'Paired', 'Pastel1',
    #                           'Pastel2', 'Set1', 'Set2', 'Set3']),
    #          ('Miscellaneous', ['gist_earth', 'terrain', 'ocean', 'gist_stern',
    #                             'brg', 'CMRmap', 'cubehelix',
    #                             'gnuplot', 'gnuplot2', 'gist_ncar',
    #                             'nipy_spectral', 'jet', 'rainbow',
    #                             'gist_rainbow', 'hsv', 'flag', 'prism'])]
