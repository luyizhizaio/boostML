__author__ = 'dayue'
#-*-coding:utf-8 -*-

import pandas as pd

unames = ['user_id','gender','age','occupation','zip']

#读取数据到DataFrame
#1::F::1::10::48067
users = pd.read_table('F:/GitHub/pydata-book/ch02/movielens/users.dat' ,
                      sep='::',header=None,names=unames)

rnames = ['user_id','movie_id','rating','timestamp']

ratings = pd.read_table('''F:/GitHub/pydata-book/ch02/movielens/ratings.dat''',
                        sep='::',header=None,names=rnames)



mnames = ['movie_id','title','genres']
movies = pd.read_table('F:/GitHub/pydata-book/ch02/movielens/movies.dat',
                       sep='::',header=None,names=mnames)

print users[:5]

print ratings[:5]
#    user_id  movie_id  rating  timestamp
# 0        1      1193       5  978300760

print movies[:5]

print ratings

#1.根据性别和年龄计算某部电影的平均得分

#合并,会根据列名的重叠情况判断那一列是连接键
data = pd.merge(pd.merge(ratings,users),movies)

print data

# Data columns:
# user_id      1000209  non-null values
# movie_id     1000209  non-null values
# rating       1000209  non-null values
# timestamp    1000209  non-null values
# dtypes: int64(4)
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 3 entries, 0 to 2
# Data columns:
# user_id       3  non-null values
# movie_id      3  non-null values
# rating        3  non-null values
# timestamp     3  non-null values
# gender        3  non-null values
# age           3  non-null values
# occupation    3  non-null values
# zip           3  non-null values
# title         3  non-null values
# genres        3  non-null values
# dtypes: int64(6), object(4)
#
print data.ix[0]
# user_id                                 1
# movie_id                                1
# rating                                  5
# timestamp                       978824268
# gender                                  F
# age                                     1
# occupation                             10
# zip                                 48067
# title                    Toy Story (1995)
# genres        Animation|Children's|Comedy
# Name: 0
#

#按性别计算每部电影的平均得分
mean_ratings = data.pivot_table('rating',rows='title',
                                cols='gender',aggfunc='mean')


print mean_ratings[:5]


# gender                                F         M
# title
# $1,000,000 Duck (1971)         3.375000  2.761905
# 'Night Mother (1986)           3.388889  3.352941
# 'Til There Was You (1997)      2.675676  2.733333
# 'burbs, The (1989)             2.793478  2.962085
# ...And Justice for All (1979)  3.828571  3.689024

#分组计数
ratings_by_title = data.groupby('title').size()

print ratings_by_title[:5]
# title
# $1,000,000 Duck (1971)            37
# 'Night Mother (1986)              70
# 'Til There Was You (1997)         52
# 'burbs, The (1989)               303
# ...And Justice for All (1979)    199
print '----------'
#过滤掉评分数据不够250条的电影
active_titles = ratings_by_title.index[ratings_by_title >=250]
print active_titles

# array(['burbs, The (1989), 10 Things I Hate About You (1999),
#        101 Dalmatians (1961), ..., Young Sherlock Holmes (1985),
#        Zero Effect (1998), eXistenZ (1999)], dtype=object)
#


mean_ratings = mean_ratings.ix[active_titles]

print mean_ratings

#了解女性最喜欢的电影

top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)

print top_female_ratings[:10]

# gender                                                         F         M
# title
# Close Shave, A (1995)                                   4.644444  4.473795
# Wrong Trousers, The (1993)                              4.588235  4.478261
# Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)           4.572650  4.464589


###########################################################
#2.计算男女分歧最大的电影

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_index(by='diff')

print sorted_by_diff[:5]
# gender                            F         M      diff
# title
# Dirty Dancing (1987)       3.790378  2.959596 -0.830782
# Jumpin' Jack Flash (1986)  3.254717  2.578358 -0.676359
# Grease (1978)              3.975265  3.367041 -0.608224
# Little Women (1994)        3.870588  3.321739 -0.548849
# Steel Magnolias (1989)     3.901734  3.365957 -0.535777

#对行反序，并取出前5行

print sorted_by_diff[::-1][:15]
# gender                                         F         M      diff
# title
# Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351
# Kentucky Fried Movie, The (1977)        2.878788  3.555147  0.676359
# Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
# Longest Day, The (1962)                 3.411765  4.031447  0.619682
# Cable Guy, The (1996)                   2.250000  2.863787  0.613787


#计算分歧最大的电影，可以计算得分数据标准差
rating_std_by_title = data.groupby('title')['rating'].std()
#根据active_titles进行过滤
rating_std_by_title = ratings_by_title.ix[active_titles]

#降序排列
print ratings_by_title.order(ascending=False)[:5]

# title
# American Beauty (1999)                                   3428
# Star Wars: Episode IV - A New Hope (1977)                2991
# Star Wars: Episode V - The Empire Strikes Back (1980)    2990
# Star Wars: Episode VI - Return of the Jedi (1983)        2883
# Jurassic Park (1993)                                     2672


