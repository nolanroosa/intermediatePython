# -*- coding: utf-8 -*-
"""
Sentiment Analysis
andrew ID: yuzhong2
@author: Yu Zhong
"""
import tweepy
from tweepy import OAuthHandler 
from textblob import TextBlob
import re

class Sentiment:
    
    def __init__(self, query, tweetCount, date):
        consumer_key = "b6H7GZ3ndWPMPRY5CGF27tUu8"
        consumer_secret = "j8rDKpiAd3fAAy90gwBlpn2TcYbybalcPq7mABXyfccF1LLnpv"
        access_token = "4854110831-67k4NbuSlo5i7H73oGVWyEaN2uzyQ3ExNgruZCG"
        access_token_secret = "ADFPh1XDzlpdocqJwEhCMycJVbwNCPFsu6cfGopkzDdXo"
        self.auth = OAuthHandler(consumer_key, consumer_secret) 
        self.auth.set_access_token(access_token, access_token_secret) 
        self.api = tweepy.API(self.auth) 
        self.query = query
        self.tweetCount = tweetCount
        self.date = date
    
    def setQuery(self, query):
        self.query = query
    
    def getQuery(self):
        return self.query
    
            
    def displaySentiment(self):
        sentiment = []
        results = tweepy.Cursor(self.api.search,q=self.query,
                               lang="en",since=self.date).items()
        #results = self.api.search(q = self.query, count=self.tweetCount)
        
        i=0
        for tweet in results:
            clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet.text).split())
            analysis = TextBlob(clean_tweet)
            if analysis.sentiment.polarity>0:
                sentiment.append('positive')
            elif analysis.sentiment.polarity < 0:
                sentiment.append('negative')
            else:
                sentiment.append('neutral')
            
            i+=1
            if i == self.tweetCount:
                break
            
        neg_tweet = [t for t in sentiment if t=='negative']
        po_tweet = [t for t in sentiment if t=='positive']
        nu_tweet = [t for t in sentiment if t=='neutral']
       
        print('Number of Tweets Selected: ',len(sentiment))
      
        print('Negative tweets:', len(neg_tweet)*100/self.tweetCount,'%')
        print('Positive tweets:', len(po_tweet)*100/self.tweetCount,'%')
        print('Neutral tweets:', len(nu_tweet)*100/self.tweetCount,'%')
        
        
        
        
        
        
        
        
        
        