#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:07:42 2020

@author: nolanroosa
"""

from sentiment_function import Sentiment
import pandas as pd
dfCovid = pd.read_csv("united_states_covid19_cases_and_deaths_by_state.csv", skiprows=3)
dfCovid = dfCovid.drop(columns = ["Cases in Last 7 Days", "Deaths in Last 7 Days", "Case Rate per 100000 in Last 7 Days", "Death Rate per 100K in Last 7 Days"])
print(dfCovid)

def menu():
    print ('''
            Welcome to the main Menu:    
           
            1. Explore previous election data
               
            2. Display sentiments: 
            
            This function will return the proportion of tweets that are 
            negative, postive and neutral. User must define keyword,
            number of query and date to query after.
                  
            3. Check New York Times 2020 Election Results
               
            4. View State COVID Data
               
            0. Quit
               ''')
    menuRequest = int(input('Enter a menu option: '))
    menuOption = []
    for i in range(0,5):
        menuOption.append(i)
    if menuRequest not in menuOption:
        print('\nEnter a valid menu item.')
    else:
        return(menuRequest)

def tweet():
    query = input('Choose a keyword, such as covid, election, Biden, Trump...: ')
    tweetCount = int(input('Choose a value between 0-1000: '))
    while tweetCount <=0 or tweetCount>1000:
        print('Error! Number out of bounds')
        tweetCount = int(input('Choose a value between 0-1000: '))
    date = input('Choose a date in the past 7 days, and type in format 2020-12-14: ')
    tweet =  Sentiment(query, tweetCount,date)
    tweet.displaySentiment()

tweet()

def covid():
    stateRequest = input('Enter the name of a state: ')
    namedState = dfCovid.set_index('State/Territory')
    
    dataRequest = int(input('''
    Which Data would you like to view?
                        
    1. Total Cases
    2. Confirmed Cases
    3. Total Deaths
    0. Return to menu
    
    '''))
    covidOption = []
    for i in range(0,4):
        covidOption.append(i)
    if dataRequest not in covidOption:
        print('\nEnter a valid menu item.')
    elif dataRequest == 1:
        print('\nTotal Cases in', stateRequest,':', namedState.loc[stateRequest][0])
    elif dataRequest == 2:
        print('\nTotal Cases in', stateRequest, ':', namedState.loc[stateRequest][1])
    elif dataRequest == 3:
        print('\nTotal Cases in', stateRequest, ':', namedState.loc[stateRequest][5])
    elif dataRequest == 0:
        print('\nYou have choosen to return to the menu.')

    
def main():
    continueFlag = True
    while continueFlag:
        menuRequest = menu()
        if menuRequest == 1:
            break
        elif menuRequest == 2:
            tweet()
            continueQ = input('Would you like to check another keyword? Y/N: ')
            if continueQ == 'Y':
                tweet()
            elif continueQ == 'N':
                print('You will now return to the main Menu')
                menu()
            else:
                print('Invalid Entry: Please enter Y or N')
        elif menuRequest == 3:
            break
        elif menuRequest == 4:
            covid()
        elif menuRequest == 0:
            print("You have quit.")
            continueFlag = False
    
    
if __name__ == "__main__":
    main()
    
    
    
    