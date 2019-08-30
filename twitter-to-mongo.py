# ===============================================
# twitter-to-mongo.py v1.0 Created by Sam Delgado
# ===============================================
from pymongo import MongoClient as Connection
#from pymongo import MongoClient
import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import os
import time
start_time = time.time()



#os.environ['http_proxy'] = "http://edcguest:edcguest@172.31.100.14:3128/"
#os.environ['https_proxy'] = "https://edcguest:edcguest@172.31.100.14:3128/"

# The MongoDB connection info. This assumes your database name is TwitterStream, and your collection name is tweets.

connection = Connection('localhost', 27017)
#db = client['TwitterStream']
#db.tweets.ensure_index("id", unique=True, dropDups=True)
db = connection.TwitterStream
# Add the keywords you want to track. They can be cashtags, hashtags, or words.

#keywords = [ '#AshokGehlot', '#SachinPilot', '#Rajasthan', '#CMOfRajasthan', 'CM of Rajasthan', '#Rafaledeal', '#RafaleVerdict', '#ModiWinsOnRafale', '#AUSvIND', '#INDvAUS', '#OdishaHockeyWorldCup2018', '#AnilAmbani', 'Anil Ambani', 'Deputy CM', '#IshaAmbaniReception']
# Optional - Only grab tweets of specific language
language = ['en']

# You need to replace these with your own values that you get after creating an app on Twitter's developer portal.

consumer_key = "bIYhgB5sP8fWnzPshEWqJwUYW"
consumer_secret = "YKZBw6gKSv9tKfuRvoBnjVyf1N3pUN7wcvFDLuKjDb9LXwDcb5"
access_token = "1143388510864334848-hp7gICErJ9uoYfb3W0rSJkrO71HOst"
access_secret = "hOPSRRzTYuCC1kHQEpJtsVNgDrpJnyFOUvOY45u06ginF"
# The below code will get Tweets from the stream and store only the important fields to your database
class StdOutListener(StreamListener):

    def on_data(self, data):

        # Load the Tweet into the variable "t"
            datajson = json.loads(data)

        # Pull important data from the tweet to store in the database.
            created_at = datajson['created_at']

                # print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))

                # insert the data into the mongoDB into a collection called tweets
                # if tweets doesn't exist, it will be created.
            db.december15.insert(datajson)
            print("--- %s seconds ---" % (time.time() - start_time))

            return True

    # Prints the reason for an error to your console
    def on_error(self, status):
        print (status)



# Some Tweepy code that can be left alone. It pulls from variables at the top of the script
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    data = api.trends_place(1)  # get all the tweets posted by Indian users
    global keywords, my_dic
    keywords = []
    my_dic = {}
    for my_dic in data[0]['trends']:
        keywords.append(my_dic.get("name", "none"))
    print(keywords)

    stream = Stream(auth, l)
    stream.filter(track=keywords, languages=language)
