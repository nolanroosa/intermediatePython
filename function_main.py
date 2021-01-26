# -*- coding: utf-8 -*-
"""
main function

@author: zhong
"""
from sentiment_function import Sentiment

def menu():
    print('5. display sentiments: this function will return the proportion of tweets\
          that are negative, postive and neutral. User must define keyword,\
              number of query and date to query after.')
    choice = int(input('Enter your choice: '))
    
    return choice

def main():
    choice = menu()
    if choice == 5:
        query = input('choose a keyword, such as covid, election...: ')
        tweetCount = int(input('choose a value between 0-1000: '))
        while tweetCount <=0 or tweetCount>1000:
            print('error! number out of bound')
            tweetCount = int(input('choose a value between 0-1000: '))
        date = input('choose a date in the past 7 date, and type in format 2020-12-14: ')
        tweet =  Sentiment(query, tweetCount,date)
        tweet.displaySentiment()
        
        
if __name__ == '__main__':
    main()