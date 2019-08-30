from __future__ import print_function

import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
import os  # for os.path.basename

import matplotlib.pyplot as plt
import matplotlib as mpl



text_file = open("input.txt", "r")
corpus = text_file.read().split('\n')
#vectorizer = CountVectorizer(encoding='latin-1')
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
#print(corpus)
stopwords = nltk.corpus.stopwords.words('english')
#print stopwords[:10]

stemmer = SnowballStemmer("english")

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in corpus:
    allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
    
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print ('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
print(vocab_frame.head())


from sklearn.feature_extraction.text import TfidfVectorizer

#define vectorizer parameters
#tfidf_vectorizer = TfidfVectorizer(max_df=0.4, max_features=200000,min_df=0.1, stop_words='english',use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))
tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform(corpus) #fit the vectorizer to synopses

#print(tfidf_matrix.shape)


terms = tfidf_vectorizer.get_feature_names()
print(terms)

from sklearn.metrics.pairwise import cosine_similarity
dist = 1 - cosine_similarity(tfidf_matrix)

from scipy.cluster.hierarchy import ward, fcluster
from sklearn.cluster import AgglomerativeClustering

linkage_matrix = ward(dist) #define the linkage_matrix using ward clustering pre-computed distances
print(linkage_matrix)
clusters=fcluster(linkage_matrix, 1, criterion='distance')

idea={'Tweet':corpus, 'Cluster':clusters} #Creating dict having doc with the corresponding cluster number.
frame=pd.DataFrame(idea,index=[clusters], columns=['Tweet','Cluster']) # Converting it into a dataframe.

print("\n")
print(frame) #Print the doc with the labeled cluster number.
print("\n")
print(frame['Cluster'].value_counts()) #Print the counts of doc belonging to each cluster.
true_h=8
order_centroids = frame['Cluster'].value_counts().argsort()[:, ::-1]
print(order_centroids)
''''terms = vectorizer.get_feature_names()
for i in range(true_h):
    print("Cluster %d:" % i,)
    for ind in order_centroids[i, :50]:
        print('%s' % terms[ind],)
    print()'''