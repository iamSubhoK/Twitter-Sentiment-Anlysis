import tweepy
from textblob import TextBlob

consumer_key = 'WZrFdXplH5lg5qsEglwnKhh3j'
consumer_secret = '01iXX5V8tp5nNmOozuaF6qpgE5SA97W22bxONvVlRMbMuWKLFz'

access_token = '817989761419853825-SjetiEjTZGVPXi07QlL3VgC4W4RsHS4'
access_token_secret = 'VsPCvnvyGWGu68eT8zJ9Nc67461w3Qq6pIC3TzyTjdZfS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Modi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)