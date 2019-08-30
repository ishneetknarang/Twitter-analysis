import json
from pprint import pprint
import nltk
import numpy as np
import re
from datetime import datetime
from collections import OrderedDict
import pandas as pd
from os import path
#from PIL import Image
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import codecs
from pprint import pprint
import re
from collections import Counter
from datetime import datetime
from itertools import cycle
import datetime
from email.utils import mktime_tz, parsedate_tz

import ast
import csv

import os
import operator
from nltk.corpus import stopwords
from nltk import download
download('stopwords') 

#from nltk.tag import StanfordPOSTagger
#from nltk.tag import StanfordNERTagger
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

# For connecting MongoDB
from pymongo import MongoClient

client = MongoClient()
db = client['eventstream']

def valuation_formula(x):
    x=x.lower().split()
    x = ' '.join([word for word in x if word not in stopwords.words("english")])

    return x


def normalize_text(text):
    try:
        text = text.encode('utf-8')
    except:
        pass
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(pic\.twitter\.com/[^\s]+))', '', text)  # removes urls
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
    text = re.sub('[\d]', '', text)
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
    text = text.replace("#\xec", ' ').replace("\#x8c", ' ')
    text = text.replace("\#xa0", ' ')
    text = text.replace("\#x9d\x92", ' ').replace("\#x9a\xaa\xf0\x9f\x94\xb5", ' ').replace(
        "#\xf0\x9f\x91\x8d\x87\xba\xf0\x9f\x87\xb8", ' ').replace("#\x9f", ' ').replace("#\x91\x8d", ' ')
    text = text.replace("\xf0\x9f\x87\xba\xf0\x9f\x87\xb8", ' ').replace("\xf0", ' ').replace('\xf0x9f', '').replace(
        "#\x9f\x91\x8d", ' ').replace("\x87\xba\x87\xb8", ' ')
    text = text.replace("#\xe2\x80\x94", ' ').replace("#\x9d\xa4", ' ').replace("#\x96\x91", ' ').replace(
        "#\xe1\x91\xac\xc9\x8c\xce\x90\xc8\xbb\xef\xbb\x89\xd4\xbc\xef\xbb\x89\xc5\xa0\xc5\xa0\xc2\xb8", ' ')
    text = text.replace("#\xe2\x80\x99s", " ").replace("#\xe2\x80\x98", ' ').replace("#\xe2\x80\x99", ' ').replace(
        "#\xe2\x80\x9c", " ").replace("#\xe2\x80\x9d", " ")
    text = text.replace("#\xe2\x82\xac", " ").replace("#\xc2\xa3", " ").replace("#\xc2\xa0", " ").replace("#\xc2\xab",
                                                                                                       " ").replace(
        "#\xf0\x9f\x94\xb4", " ").replace("#\xf0\x9f\x87\xba\xf0\x9f\x87\xb8\xf0\x9f", "")                                                                                                   


    return text





# Ques1. Show the collections in the TwitterStream database
print(db.collection_names())

# Ques2. Count the total number of tweets in the particular collection
print("total no of tweets")
print(db.eventdata.count())

# Ques3. Print the top document
#pprint(db.eventdata.find_one())

# Ques4. Print the fields of document
#print(db.eventdata.find_one().keys())

# Ques5. Print the text of top 10 tweets with posting time
tweetsCol = db.eventdata.find()
count=0
f= codecs.open("analysis.txt",'w','utf-8')
for tweet in tweetsCol:
	if count<80000:
		count+=1
		text = ''
		decoded_text = ""
		if 'extended_tweet' in tweet:
			text=tweet['extended_tweet']['full_text']
		else:
			if 'retweeted_status' in tweet:
				text= tweet['retweeted_status']['text']
			else:
				text=tweet['text']
		#print(text)
		for parts in text.split():
			print(parts)
			try:
				decoded_text= decoded_text+ parts.decode('utf-8')+' '
				print("hiii")
				f.write(decoded_text)
			except:
				pass 
		f.write(text)
		f.write('\n')
		text1 = normalize_text(decoded_text)
		print(text1)
		stop_words = stopwords.words('english')
		text=valuation_formula(text)

	#print(tweet['created_at'])
f.close()




# Ques6. Print the most popular 50 hashtags and plot the scattar, bar and wordcloud diagram to represent most popular hashtags.
'''tweetsCol1 = db.eventdata.find()
hashtag_list={}
sorted_hashtags={}
for tweet in tweetsCol1:
	hts = tweet['entities']['hashtags']
	for hinfo in hts:
            h = hinfo['text']
            # add hashtag to list
            hashtag_list[h] = 1 + hashtag_list.get(h,0)

sorted_hashtags=OrderedDict(sorted(hashtag_list.items(), key=lambda x:x[1], reverse=True))

names=[]
values=[]

c1=0

for ht in sorted_hashtags.items():
	
	if c1<50:
		c1+=1
		print("," + str(ht))
		names.append(ht[0])
		values.append(ht[1])
		


# Scattar plot
plt.scatter(list(range(50)), values, c='r', label='hashtags')
plt.savefig('scatter.png')
plt.show()

# Bar plot
plt.bar(range(50),values,tick_label=names)
plt.xticks(rotation=50)
plt.xlabel("hashtags")
plt.ylabel("frequency")
plt.savefig('bar.png')
plt.show()

#WordCloud plot
wordcloud=WordCloud(max_font_size=30, max_words=50, background_color="white").generate_from_frequencies(hashtag_list)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloud.png')
plt.show()


# Ques7. Print the top 50 retweeted tweets

tweetsCol1 = db.descember15.find()
retweets = {}
count=0
for tweet in tweetsCol1:
	#print(tweet['text'])
	if 'retweeted_status' in tweet:
		if(count<50):
			count+=1
			rt = tweet['retweeted_status']
			retweets[rt['id_str']] = rt
# convert to list
retweets = [retweets[w] for w in retweets.keys()]
    # sort by retweet count
retweets.sort(key=lambda x: -x['retweet_count'])
    # display top k retweets
for t in retweets:
	f.write(t['text'])
	#print(t['text']) 
	print(t['retweet_count']) 
	




# Ques8. Print the top 10 users
user_list={}
sorted_users={}
c=1
for tweet in tweetsCol1:
	u = tweet['user']['screen_name']
	user_list[u] = 1 + user_list.get(u, 0)
  
sorted_users=OrderedDict(sorted(user_list.items(), key=lambda x:x[1], reverse=True))
for ht in sorted_users.items():
	if c<10:
		c+=1
		print("," + str(ht))'''
    


						

							
							
							
						
							
							
							
											




						
									
									
								
								
								
								
		

