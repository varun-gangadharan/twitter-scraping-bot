import tweepy
import pandas as pd
import time
from textblob import TextBlob

consumer_key = "HozeqvZWWHUvaWqAPCKQn8d44"
consumer_secret = "M3cWR0eKpLeKmsdZQG4j62QWy5qoI34hDlvd5scKi3Hyz9ZeqA"
access_token = "3000357167-0K9NhtpyFDHL3Mvd2XiUGTBp10We5mhXVgS0uax"
access_token_secret = "NCB9GFzSosztjxR7nk280xqSGlH4ZNaCAiEsoeJM7lAaK"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweet_list = []

subject = 'kanyewest'
tweets_num = 100
feeling = ''
sentiment_score = 0

def tweets_to_csv(subject,tweets_num):
    sentiment_score = 0
    for tweet in api.user_timeline(id=subject, count=tweets_num):
        edu = TextBlob(tweet.text)
        sentiment_val = edu.sentiment.polarity
        if sentiment_val < 0:
            feeling = 'negative'
            sentiment_score -= 1
        if sentiment_val == 0:
            feeling = 'neutral'
        if sentiment_val > 0 and sentiment_val <=1:
            feeling = 'positive'
            sentiment_score += 1
        tweet_list.append((tweet.created_at,tweet.id,tweet.text, feeling))
        df = pd.DataFrame(tweet_list,columns=['Date', 'Tweet_ID', 'Message', 'Feeling'])
        df.to_csv('scraped_tweets.csv')
    print(sentiment_score)
    if sentiment_score > 0:
        print("Based on analysis of ", tweets_num, " tweets, we can conclude that people have a positive sentiment regarding ", subject, ".")
    if sentiment_score == 0:
        print("Based on analysis of ", tweets_num, " tweets, we can conclude that people have a neutral sentiment regarding ", subject, ".")
    if sentiment_score < 0:
        print("Based on analysis of ", tweets_num, " tweets, we can conclude that people have a negative sentiment regarding ", subject, ".")

tweets_to_csv(subject, tweets_num)


