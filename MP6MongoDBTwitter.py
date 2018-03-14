import tweepy
import json
from pymongo import MongoClient
import datetime
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#Set MongoDB host and collection
mongohost = 'mongodb://localhost/twitter'
client = MongoClient(mongohost)
db = client.twitter

#Set Twitter Authorization keys
consumerkey = 'YYniyLymm1DgqlK56O62ULd6k'
consumersecret = 'PJbIDGA9F1XwhXgEXqUoPP2Ehqz0ovavqwIbI0KQfnLYnYFO5c'
accesstoken = '317808881-JBm1BthQLHhW69LFy2xearYHfMhD5rnMHhv3OLLt'
accesstokensecret = 'XMSDlELI3av9rFpmIepF38f2SrTIENAgfIo8CD1nvgcIr'

#Authenticate to Twitter through Tweepy API
auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret)
api = tweepy.API(auth)

#Create list of twitter accounts to mind for Texas A&M Football Tweets
accounts = ['@aggiefblife', '@GBHunting', '@KyleField_12th', '@_TaylorHamm', '@CoachSumlin', '@BrentZwerneman', '@TexAgs', '@AggieFootball']

#set start and end date range for tweets
start = datetime.datetime(2017, 11, 11, 0, 0, 0)
end = datetime.datetime(2017, 11, 19, 0, 0, 0)

#Initialization
counter = 0
db.aggiefootball.delete_many({})
textfile = []
wordfile = []

#Retrieve tweets for each account and write relevant columns to MongoDB
for acct in accounts:
    print acct
    tmptweets = api.user_timeline(acct)
    for tweet in tmptweets:
        if tweet.created_at > start and tweet.created_at < end:
            counter = counter + 1
            print counter
            inserttweet = {'screenname':tweet.user.screen_name, 'text':tweet.text, "created":tweet.created_at}
            db.aggiefootball.insert(inserttweet)
            textfile.append(tweet.text)

#Create list of individual words in all tweets
for line in textfile:
    for word in line.split():
        if 'https' not in word and '@' not in word and 'RT' not in word:
            wordfile.append(word)

#Create Word Cloud
word_string = ' '.join(wordfile)
word_string = word_string.strip("u'")
word_string = word_string.replace('amp', '&')

wordcloud = WordCloud(stopwords=STOPWORDS).generate(word_string)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()