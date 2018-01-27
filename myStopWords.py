# -*- coding: utf-8 -*-
def get_stop_words():
    stopwords=[line.strip().decode('utf-8') for line in open('stop_words.txt','r').readlines()]
    return stopwords


