# !/usr/bin/python
# -*- coding:utf-8 -*-

from gensim import corpora,models, similarities
from pprint import pprint


if __name__ == '__main__':

  f = open('LDA_test.txt')
  stop_list = set('for a of the and to in'.split())
  texts = [[word for word in line.strip().lower().split() if word not in stop_list] for line in f]
  print 'Text:'
  pprint(texts)

  #创建一个词库
  dictionary = corpora.Dictionary(texts)
  print dictionary
  V = len(dictionary)


  #计算词频
  corpus = [dictionary.doc2bow(text) for text in texts]  # doc2bow返回 第一个值表示词在参数text的编号，第二个值表示出现在dict中词在参数text中的次数
  print corpus

  #计算tf-idf
  corpus_tfidf = models.TfidfModel(corpus)[corpus]
  print 'corpus_tfidf=\n',corpus_tfidf
  #corpus_tfidf = corpus

  print 'TF-IDF'
  for c in corpus_tfidf:
    print c

  print 'LSI Model'
  lsi = models.LsiModel(corpus_tfidf,num_topics=2,id2word=dictionary)
  topic_result = [a for a in lsi[corpus_tfidf]]
  pprint(topic_result)

  print 'LSI Topics:'
  pprint (lsi.print_topics(num_topics=2,num_words=5))
  similarity = similarities.MatrixSimilarity(lsi[corpus_tfidf])
  print 'Similarity：'
  pprint(list(similarity))







