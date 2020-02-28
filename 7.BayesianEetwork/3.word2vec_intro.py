# etc/bin/python
# -*- encoding: utf-8 -*-

from time import time
from gensim.models import Word2Vec
import sys #引入系统
import os #引入平台



reload(sys) #重新加载模块
sys.setdefaultencoding('utf-8')

class LoadCorpora(object):
    def __init__(self, s):
        self.path = s

    def __iter__(self):
        f = open(self.path,'r')
        for line in f:
            yield line.split(' ')
def print_list(a):
    for i, s in enumerate(a):
        if i != 0:
            print '+',
        print s,



if __name__ =="__main__":
    if not os.path.exists('news.model'):
        sentences = LoadCorpora('news.dat')
        t_start = time()
        model = Word2Vec(sentences,size=200,min_count=5,workers=8)  # 词向量维度为200，丢弃出现次数少于5次的词;workers指定线程数
        model.save('news.model')
        print 'ok:',time()- t_start

    model = Word2Vec.load('news.model')
    # print '词典中词的个数：',model.vocabulary.size()

    # for i ,word in enumerate(model.vocabulary):
    #     print word,
    #     if i % 25 ==24:
    #         print
    # print



    intrested_words = ('中国', '手机', '学习', '人民', '名义')
    print '特征向量：'
    for word in intrested_words:
        print word, len(model[word]), model[word]  #词和向量

    for word in intrested_words:
        result = model.most_similar(word)  #返回最相似的词语，相似度。
        print '与', word, '相近的词：'
        for w,s in result:
            print '\t',w,s

    words = ('中国','祖国','毛泽东','人民')
    for i in range(len(words)):
        w1 = words[i]
        for j in range(i+1,len(words)):
            w2 = words[j]
            print '%s 和%s 的相似度为：%.6f' % (w1,w2,model.similarity(w1,w2))



    #离群词
    print '========================'
    opposites = ((['中国', '城市'], ['学生']),
                 (['男', '工作'], ['女']),
                 (['俄罗斯', '美国', '英国'], ['日本']))
    for positive, negative in opposites:
        #支持词语的加减运算
        result = model.most_similar(positive=positive, negative=negative)
        print_list(positive)
        print '-',
        print_list(negative)
        print '：'
        for word, similar in result:
            print '\t', word, similar

    print '========================'
    words_list = ('苹果 三星 美的 海尔', '中国 日本 韩国 美国 北京',
                  '医院 手术 护士 医生 感染 福利', '爸爸 妈妈 舅舅 爷爷 叔叔 阿姨 老婆')
    for words in words_list:
        print words, '离群词：', model.doesnt_match(words.split(' '))

