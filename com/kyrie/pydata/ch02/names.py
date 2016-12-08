__author__ = 'dayue'
#-*-coding:utf-8 -*-

import pandas as pd
import numpy  as np

#name,sex,number
#读取文本

names1880 = pd.read_csv('F:/GitHub/pydata-book/ch02/names/yob1880.txt',names=['name','sex','births'])

#计算男女出生数
print names1880.groupby('sex').births.sum()
# sex
# F       90993
# M      110493
# Name: births

years = range(1880,2011)
pieces =[]
colums = ['name','sex','births']

for year in years:
    path ='F:/GitHub/pydata-book/ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path,names=colums)
    frame['year'] = year
    pieces.append(frame)
# Concatenate everything into a single DataFrame
names = pd.concat(pieces,ignore_index = True)

print names.head(5)
# Name: births
#         name sex  births  year
# 0       Mary   F    7065  1880
# 1       Anna   F    2604  1880

print names
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 1690784 entries, 0 to 1690783
# Data columns:
# name      1690784  non-null values
# sex       1690784  non-null values
# births    1690784  non-null values
# year      1690784  non-null values
# dtypes: int64(2), object(2)


#1.在year和sex上聚合births
total_births = names.pivot_table('births',rows='year',
                                  cols='sex',aggfunc=sum)

print total_births.tail()
# sex         F        M
# year
# 2006  1896468  2050234
# 2007  1916888  2069242
# 2008  1883645  2032310
# 2009  1827643  1973359
# 2010  1759010  1898382

total_births.plot(title='Total birhts by sex and year')


def add_prop(group):
    #分子转成float型
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)

print names

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 1690784 entries, 0 to 1690783
# Data columns:
# name      1690784  non-null values
# sex       1690784  non-null values
# births    1690784  non-null values
# year      1690784  non-null values
# prop      1690784  non-null values
# dtypes: float64(1), int64(2), object(2)

#检查分组的prop之和是否为1
print np.allclose(names.groupby(['year','sex']).prop.sum(),1)
#True

#2.取出每对sex/year组合的前1000个名字

def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)

print top1000[:10]

#                  name sex  births  year      prop
# year sex
# 1880 F   0       Mary   F    7065  1880  0.077643
#          1       Anna   F    2604  1880  0.028618
#          2       Emma   F    2003  1880  0.022013
#          3  Elizabeth   F    1939  1880  0.021309
#          4     Minnie   F    1746  1880  0.019188

#方法二：取出每对sex/year组合的前1000个名字

pieces =[]
for year ,group in names.groupby(['year','sex']):
    pieces.append(group.sort_index(by='births',ascending=False)[:1000])

top1000 = pd.concat(pieces,ignore_index=True)

print top1000[:5]
# 0       Mary   F    7065  1880  0.077643
# 1       Anna   F    2604  1880  0.028618
# 2       Emma   F    2003  1880  0.022013
# 3  Elizabeth   F    1939  1880  0.021309
# 4     Minnie   F    1746  1880  0.019188


#3.分析命名趋势

boys = top1000[top1000.sex =='M']

girls = top1000[top1000.sex =='F']

#生成按year和name统计的总出生数透视图
total_births = top1000.pivot_table('births',rows='year',cols='name',
                                   aggfunc=sum)

print total_births

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 131 entries, 1880 to 2010
# Columns: 6865 entries, Aaden to Zuri
# dtypes: float64(6865)

subset = total_births[['John','Kyrie','Mary']]

subset.plot(subplots=True,figsize=(12,10),grid=False,
            title='Number of births per year')

#4.估计命名多样性的增长

#计算最流行的100个名字所占比例
table = top1000.pivot_table('prop',rows='year',
                            cols='sex',aggfunc=sum)

table.plot(title='sum of table1000.prop by year and sex',
           yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
#计算占总出口人数前50%的不同名字的数量

df =boys[boys.year ==2010]

print df

prop_cumsum = df.sort_index(by='prop',ascending =False).prop.cumsum()

print prop_cumsum[:10]
# 260877    0.011523
# 260878    0.020934
# 260879    0.029959
# 260880    0.038930
# 260881    0.047817



print prop_cumsum.searchsorted(0.5)
#116


df = boys[boys.year ==1900]
in1900 = df.sort_index(by='prop', ascending=False).prop.cumsum()


print in1900.searchsorted(0.5) + 1
#25


def get_quantile_count(group ,q=0.5):
    group= group.sort_index(by='prop',ascending=False)
    return group.prop.cumsum().searchsorted(q) +1

diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

print diversity.head()
# sex    F   M
# year
# 1880  38  14
# 1881  38  14
# 1882  38  15
# 1883  39  15
# 1884  39  16

diversity.plot(title='Number of popular names in top 50%')










