from __future__ import division
from __future__ import print_function
import codecs
import json
from pprint import pprint
import nltk
import numpy as np
import fastcluster
import re
from collections import Counter
from datetime import datetime
from itertools import cycle
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import datetime
#from email.utils import mktime_tz, parsedate_tz
import ast
import csv
#import dataset
#from sqlalchemy.exc import ProgrammingError
import os
import json
#import scipy.cluster.hierarchy as sch
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn import preprocessing
#from sklearn.metrics.pairwise import pairwise_distances
#from sklearn import metrics
#import gensim.models.keyedvectors as word2vec
#from sklearn.metrics.pairwise import cosine_similarity
import operator
import pandas as pd
#import networkx as nx
#from pyemd import emd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import download
download('stopwords') 
from nltk.tag import StanfordPOSTagger
from nltk.tag import StanfordNERTagger
from nltk import word_tokenize
import string
import sys
import time
import sys  
import math
import re
from decimal import*
import pandas
import webbrowser
from pandas import read_csv
from pandas.compat import StringIO
import codecs



# set the system proxy
#os.environ['http_proxy'] = "http://edcguest:edcguest@172.31.100.25:3128/"
#os.environ['https_proxy'] = "https://edcguest:edcguest@172.31.100.25:3128/"

from pymongo import MongoClient

client = MongoClient()
db = client['eventstream']

def document_vector(model, doc):
    doc = [word for word in doc if word in model.vocab]
    return np.mean(model[doc], axis=0)

def valuation_formula(x):
    x=x.lower().split()
    x = ' '.join([word for word in x if word not in stopwords.words("english")])

    return x


def normalize_text(text):
    try:
        text = text.encode('utf-8')
    except:
        pass
    ''' text = re.sub('((www.[^s]+)|(https?://[^s]+)|(pic.twitter.com/[^s]+))', '', text)  # removes urls
    #text = re.sub('@[^\s]+', '', text)  # removes user mentions
    #text = re.sub('#([^\s]+)', '', text)  # removes hashtags
    text = re.sub('@', '', text)  # removes user mentions
    text = re.sub('#', '', text)  # removes hashtags
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'',text)
    text = re.sub('[d]', '', text)
    text = text.replace(".", '')
    text = text.replace("'", ' ')
    text = text.replace("\"", ' ')
    text = text.replace(":", ' ')
    text = text.replace("?", ' ')
    text = text.replace("-", ' ')
    text = text.replace("RT", ' ')
    text = text.replace(",", ' ')
    text = text.replace("_", ' ')
    text = text.replace("(", ' ')
    text = text.replace(")", ' ')


    # normalize utf8 encoding
    text = text.replace("\x9d", ' ').replace("\x8c", ' ')
    text = text.replace("\xa0", ' ')
    text = text.replace("\x9d\x92", ' ').replace("\x9a\xaa\xf0\x9f\x94\xb5", ' ').replace(
        "\xf0\x9f\x91\x8d\x87\xba\xf0\x9f\x87\xb8", ' ').replace("\x9f", ' ').replace("\x91\x8d", ' ')
    text = text.replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8", ' ').replace("\xf0", ' ').replace('\xf0x9f', '').replace(
        "\x9f\x91\x8d", ' ').replace("\x87\xba\x87\xb8", ' ')
    text = text.replace("\xe2\x80\x94", ' ').replace("\x9d\xa4", ' ').replace("\x96\x91", ' ').replace(
        "\xe1\x91\xac\xc9\x8c\xce\x90\xc8\xbb\xef\xbb\x89\xd4\xbc\xef\xbb\x89\xc5\xa0\xc5\xa0\xc2\xb8", ' ')
    text = text.replace("\xe2\x80\x99s", " ").replace("\xe2\x80\x98", ' ').replace("\xe2\x80\x99", ' ').replace(
        "\xe2\x80\x9c", " ").replace("\xe2\x80\x9d", " ")
    text = text.replace("\xe2\x82\xac", " ").replace("\xc2\xa3", " ").replace("\xc2\xa0", " ").replace("\xc2\xab",
                                                                                                       " ").replace(
        "\xf0\x9f\x94\xb4", " ").replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f", "")
     # normalize utf8 encoding
    text = text.replace("#\xec", ' ').replace("#x8c", ' ')
    text = text.replace("#xa0", ' ')
    text = text.replace("#x9d\x92", ' ').replace("#x9a\xaa\xf0\x9f\x94\xb5", ' ').replace(
        "#\xf0\x9f\x91\x8d\x87\xba\xf0\x9f\x87\xb8", ' ').replace("#\x9f", ' ').replace("#\x91\x8d", ' ')
    text = text.replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8", ' ').replace("\xf0", ' ').replace('\xf0x9f', '').replace(
        "#\x9f\x91\x8d", ' ').replace("\x87\xba\x87\xb8", ' ')
    text = text.replace("#\xe2\x80\x94", ' ').replace("#\x9d\xa4", ' ').replace("#\x96\x91", ' ').replace(
        "#\xe1\x91\xac\xc9\x8c\xce\x90\xc8\xbb\xef\xbb\x89\xd4\xbc\xef\xbb\x89\xc5\xa0\xc5\xa0\xc2\xb8", ' ')
    text = text.replace("#\xe2\x80\x99s", " ").replace("#\xe2\x80\x98", ' ').replace("#\xe2\x80\x99", ' ').replace(
        "#\xe2\x80\x9c", " ").replace("#\xe2\x80\x9d", " ")
    text = text.replace("#\xe2\x82\xac", " ").replace("#\xc2\xa3", " ").replace("#\xc2\xa0", " ").replace("#\xc2\xab",
                                                                                                       " ").replace(
        "#\xf0\x9f\x94\xb4", " ").replace("#\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f", "") '''                                                                                                  


    return text


def process_json_tweet(text, fout, debug, tweet):
    features = []
    needed_entry = {}
    needed_entry['text']=tweet['text']
    
    
    if len(text.strip()) == 0:
        return []
    text = normalize_text(text)
    
    print(text)
    print('\n')

     
    needed_entry['hashtags']= tweet['entities']['hashtags'] 
    hashtags = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
       

    if 'retweeted_status' in tweet:
        needed_entry['retweeted_count']=tweet['retweeted_status']['retweet_count']
        #fout.write(':'+str(tweet['retweeted_status']['retweet_count']))
    else:
        needed_entry['retweeted_count']=tweet['retweet_count']
        #fout.write(':'+str(tweet['retweet_count']))
    if 'followers_count' in tweet['user']:
        needed_entry['followers_count']=tweet['user']['followers_count'];
        #fout.write(':'+str(tweet['user']['followers_count']));
    csvwriter.writerow([tweet['id'], text, hashtags, needed_entry['retweeted_count'], needed_entry['followers_count']])

    #fout.write('\n')
    

    return needed_entry





def parse_datetime(value):
    time_tuple = parsedate_tz(value)
    timestamp = mktime_tz(time_tuple)

    return datetime.datetime.fromtimestamp(timestamp)
'''start main'''


if __name__ == "__main__":
    
    #fout = codecs.open("foutfile.txt", 'w', 'utf-8')
    fout1=codecs.open("raw_tweet.txt", 'w', 'utf-8')
    start_time = time.time()
    
    header = ['id', 'text', 'tweet', 'hashtags', 'retweets', 'followers']
    
    
    debug = 1
   
    
    tweet_unixtime_old = -1
    
    tempcol = {}
    total_tweets=0
    needed_entry = {}
    start_time = time.time()
    
    tweetsCol = db.eventdata.find()
    
    #count=0
    
    print('total number of tweets in whole corpus')
    
    print(db.eventdata.count())

    df = pd.DataFrame(columns=['id', 'text', 'tweet', 'retweets'])

    for tweet in tweetsCol:
        #count+=1
    	#tweet_gmttime = tweet['created_at']
        #x=str(parse_datetime(tweet_gmttime))


        
        
       
        #if(count<10000):
            
            
            
        tweet_id = tweet['id']
        if tweet_id in tweet:
            fout.write('tweet_id:'+ str(tweet_id)+'')
        text = ''
        decoded_text = ""
        
        if 'extended_tweet' in tweet:
            
            text=tweet['extended_tweet']['full_text']
                
        else:
           
            if 'retweeted_status' in tweet:
                text= tweet['retweeted_status']['text']
            else:
                text=tweet['text']
            
        
   

        if 'retweeted_status' in tweet:
            retweeted_count=tweet['retweeted_status']['retweet_count']
            #fout.write(':'+str(tweet['retweeted_status']['retweet_count']))
        else:
            retweeted_count=tweet['retweet_count']
            #fout.write(':'+str(tweet['retweet_count']))
        
    
        
        for parts in text.split():
            try:
                decoded_text= decoded_text+ parts.decode('utf-8')+' '
                
            except:
                pass 
        
        text = normalize_text(decoded_text)
        #stop_words = stopwords.words('english')
        #text=valuation_formula(text)
        #print(text)
       
        #df = df.append({'id': tweet_id, 'text': text, 'tweet': decoded_text , 'retweets': retweeted_count}, ignore_index=True)
        fout1.write(text)
        fout1.write('\n')
        #np.savetxt('raw_tweet.txt', df1, fmt="%s")
        
            
            
    print("--- %s seconds ---" % (time.time() - start_time))      
    fout1.close()

    


            
            
            

        

