import codecs
import json
import nltk
import numpy as np
import fastcluster
import re
import math
from collections import Counter
from datetime import datetime
from itertools import cycle

import ast
import csv
#import dataset
from sqlalchemy.exc import ProgrammingError

import os
import scipy.cluster.hierarchy as sch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics.pairwise import pairwise_distances
from sklearn import metrics
from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora
from gensim import models
from gensim import similarities

from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize

import string
import sys
import time

texts_lda=[]

    

text_file = open("input.txt", "r")
documents = text_file.read().split('\n')
parts=[]
for line in documents:
    parts=line.split(' ')

    texts_lda.append(parts)
#print(texts_lda)

dictionary = corpora.Dictionary(texts_lda)

                # convert tokenized documents into a document-term matrix
corpus_lda = [dictionary.doc2bow(text_lda) for text_lda in texts_lda]                

# generate LDA model
ldamodel = models.ldamodel.LdaModel(corpus_lda, num_topics = 8, id2word = dictionary, passes = 10)
#print(ldamodel.print_topics(num_topics=ntopics, num_words=5))
lda_corpus = ldamodel[corpus_lda]

#get the keywords list for each topic
print("\n\nTopics generated using LDA----")
keywords_topics = []
count1 = 0 #TODO:: Remove count1 variable later
'''for num,topic in ldamodel.topics(num_topics = 8, num_words = 30):
#for num,topic in ldamodel(num_topics = 8, num_words = 15):
    try:
        pp=topic.encode('utf-8').strip()
        print (pp)
    except:
        print("Error in printing topic due to character encoding")
        pass
    token_list = []
    token = topic.split("+")
    for word in token:
        word1 = word[word.index('"')+1:word.rindex('"')]
        num = word[:word.index('*')]
        if num.strip() == "0.000":
            break
        token_list.append(word1)
    keywords_topics.append(token_list)
    count1 += 1

print ("\nAssert" + str(count1) + " :: " + str(8) )'''


f=open("abc.txt","+w")
topics = ldamodel.print_topics(num_words=30)
for topic in topics:
    f.write(topic)
f.close()