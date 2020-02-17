# /usr/bin/python
# -*- encoding:utf-8 -*-



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from numpy import interp
from sklearn import metrics

import pydotplus

#鸢尾花决策树分类

#
iris_feature_E = 'sepal length','sepal width','patal length','petal width'
iris_feature = u'花萼长度',u'花萼宽度',u'花瓣长度',u'花瓣长度'
iris_class = 'Iris-setosa','Iris-versicolor','Iris-virginica'

if __name__ =='__main__':

    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    path ='../data/iris.data'
    data = pd.read_csv(path,header=None)

    x = data[range(4)]
    y = pd.Categorical(data[4]).codes

    x = x.iloc[:,:2]
    x_train ,x_test,y_train,y_test = train_test_split(x,y,train_size=0.7 ,random_state=1)
    print y_test.shape

    #决策树参数
    # min_samples_split = 10：如果该结点包含的样本数目大于10，则(有可能)对其分支
    # min_samples_leaf = 10：若将某结点分支后，得到的每个子结点样本数目都大于10，则完成分支；否则，不进行分支
    model = DecisionTreeClassifier(criterion='entropy') #采用信息增益作为评判标准
    model.fit(x_train,y_train)
    y_test_hat = model.predict(x_test)

    y_score = model.predict_proba(x_test)

    # 验证模型
    c_number = np.unique(y).size #分类数量
    y_one_hot = label_binarize(y_test, classes=np.arange(c_number))  # 二值化类别

    fpr, tpr, thresholds = metrics.roc_curve(y_one_hot.ravel(), y_score.ravel())
    auc = metrics.auc(fpr, tpr)
    print 'auc=',auc


    #1.保存决策树的图
    with open('iris.dot','w') as f:
        tree.export_graphviz(model,out_file=f)

    #2.输出到pdf格式
    # dot_data = tree.export_graphviz(model, out_file=None,feature_names=iris_feature_E,class_names=iris_class,
    #                          filled =True,rounded=True,special_characters=True)
    # graph = pydotplus.graph_from_dot_data(dot_data)
    # graph.write_pdf('iris.pdf')
    # f = open('iris.png','wb')
    # f.write(graph.create_png())
    # f.close()


    #画图
    N,M = 50 ,50 #横纵样本点数
    x1_min,x2_min = x.min() #返回两列的最小值
    x1_max,x2_max = x.max()
    t1 = np.linspace(x1_min,x1_max,N)
    t2 = np.linspace(x2_min,x2_max,M)
    print t1
    print t2
    x1 ,x2 = np.meshgrid(t1,t2) #转成多行
    print x1
    print x2

    x_show = np.stack((x1.flat,x2.flat),axis =1) #flat压平,stackc成两列
    print x_show.shape

    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    y_show_hat =model.predict(x_show)
    print y_show_hat.shape
    print y_show_hat
    y_show_hat = y_show_hat.reshape(x1.shape) # 使之与输入的形状相同
    print y_show_hat
    plt.figure(facecolor='w')
    plt.pcolormesh(x1,x2,y_show_hat,cmap=cm_light)
    plt.scatter(x_test[0],x_test[1],c=y_test.ravel(),edgecolors='k',s=150,zorder=10,cmap=cm_dark,marker='*')
    plt.scatter(x[0],x[1],c=y.ravel(),edgecolors='k',s =40,cmap=cm_dark)

    plt.xlabel(iris_feature[0], fontsize=15)
    plt.ylabel(iris_feature[1], fontsize=15)
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    plt.grid(True)
    plt.title(u'鸢尾花数据的决策树分类', fontsize=17)
    plt.show()









