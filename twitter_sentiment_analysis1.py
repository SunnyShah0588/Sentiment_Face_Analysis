import tweepy
from textblob import TextBlob
import csv

consumer_key = 'h6aFAIpCkslOfBWCRETJKgnsK'
consumer_secret = 'w8WjVsav35RqkVkJt2x54HkVRAOK64DiXDetQPle7SneVXH5WV'

access_token = '1857719946-yilEsjQIRQ0XME9hoEW7VUUaDgeXgxIynrImjO8'
access_token_secret = 'ma9E2Lvyhfg3rlr2Oj1AqxHLqxkhIsqh0kPZaSOVvMCAz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('iphone')


'''with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable) '''

for tweet in public_tweets:
	print (public_tweets)
	print(" ")

   # print(tweet.text)
   # analysis = TextBlob(tweet.text)
   # print(analysis.sentiment)
    

