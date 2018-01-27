# -*- coding: utf-8 -*-
import jieba
from loadData import load_articles
from myStopWords import get_stop_words
from gensim import corpora,models

articles=load_articles()

docs=articles.text

docs_sep=[]
for doc in docs:
    segs=jieba.cut(doc,cut_all=False)
    words=list(set(list(segs)))
    if(len(words))>5:
        docs_sep.append(words)

docs_clean=[]
stop_words=get_stop_words()
for d in docs_sep:
    docs_clean.append([i for i in d if not i in stop_words])

dictionary = corpora.Dictionary(docs_clean)
corpus=[dictionary.doc2bow(doc) for doc in docs_clean]
print 'corpus ok'
ldamodel = models.ldamodel.LdaModel( num_topics=10, id2word=dictionary)


