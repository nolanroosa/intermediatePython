#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:07:42 2020

@author: nolanroosa
"""
#%%  Imports
from sentiment_function import Sentiment
import pandas as pd
from IPython.core.display import HTML
from bs4 import BeautifulSoup 
import requests
from pytrends.request import TrendReq
import numpy as np
import matplotlib.pyplot as plt


#%% CSV imports
dfCovid = pd.read_csv("united_states_covid19_cases_and_deaths_by_state.csv", skiprows=3)
dfCovid = dfCovid.drop(columns = ["Cases in Last 7 Days", "Deaths in Last 7 Days", "Case Rate per 100000 in Last 7 Days", "Death Rate per 100K in Last 7 Days"])
#print(dfCovid)

#%% Main Menu
def menu():
    print ('''
            Welcome to the main Menu:    
           
            1. Election Comparison (past 5 elections)
            
            This option will produce an HTML file that will be downloaded 
            to you local directory. The file will compare elections 
            by state and whether they went blue or red during 
            that election year.
               
            2. Display sentiments: 
            
            This function will return the proportion of tweets that are 
            negative, postive and neutral. User must define keyword,
            number of query and date to query after.
                                 
            3. View State COVID Data
            
            4. View Trending Election Google Searches
            
            This will provide a bar graph showing the top 25 trending topics
            relative to the Election, how many times each topic is searched, 
            and will highlight any search results concerning a state by 
            changing the bar color to red.
               
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

#%% Tweets
def tweet():
    query = input('Choose a keyword, such as covid, election, Biden, Trump...: ')
    tweetCount = int(input('Choose a value between 0-1000: '))
    while tweetCount <=0 or tweetCount>1000:
        print('Error! Number out of bounds')
        tweetCount = int(input('Choose a value between 0-1000: '))
    date = input('Choose a date in the past 7 days, and type in format 2020-12-14: ')
    tweet =  Sentiment(query, tweetCount,date)
    tweet.displaySentiment()


#%% COVID Option
def covid():
    stateRequest = input('Enter the name of a state: ')
    
    continueTest = True
    while continueTest:
        if stateRequest in dfCovid["State/Territory"].tolist():
            continueTest = False
        else:
            stateRequest = input('Enter a valid State: ')
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

#%% Election Comparison
pd.options.mode.chained_assignment = None  # default='warn'
#function that return a blue or red square dependening on presidential candidate
def pic(row):
    if row == 'R':
        val = 'https://cdn.pixabay.com/photo/2017/09/06/13/29/red-2721467_1280.jpg'
    else:
        val = 'https://cdn.pixabay.com/photo/2017/09/04/22/57/diagonal-2715840_1280.jpg'
    return val

us_state_abbrev = {
    'alabama': 'AL',
    'alaska': 'AK',
    'american Samoa': 'AS',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'washington DC': 'DC',
    'florida': 'FL',
    'georgia': 'GA',
    'guam': 'GU',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new-hampshire': 'NH',
    'new-jersey': 'NJ',
    'new-mexico': 'NM',
    'new-york': 'NY',
    'north-carolina': 'NC',
    'north-dakota': 'ND',
    'northern-moriana-islands':'MP',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'puerto-ico': 'PR',
    'rhode-island': 'RI',
    'south-carolina': 'SC',
    'south-dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virgins-ilands': 'VI',
    'virginia': 'VA',
    'washington': 'WA',
    'west-virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'
}
#################################################################################
 #2020 DATA
#################################################################################

#Scrapping state results for general election (POLITICO)
#Going to parse through each state data and pull:
    #% of votes
    #number of votes
#for each candidate

States = ['alabama', 'alaska' ,'arizona', 'arkansas','california', 'colorado','connecticut', 
          'delaware', 'florida','georgia','hawaii','idaho', 'illinois',
          'indiana','iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland',
          'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana',
          'nebraska', 'nevada', 'new-hampshire', 'new-jersey', 'new-mexico', 'new-york',
          'north-carolina','north-dakota','ohio','oklahoma','oregon','pennsylvania',
          'rhode-island','south-carolina','south-dakota', 'tennessee','texas','utah','vermont',
          'virginia', 'washington','west-virginia','wisconsin','wyoming']

state_data = []

for s in States:
    url = 'https://www.politico.com/2020-election/results/' + s + '/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tb = soup.find(id = '__next')
    state = tb.find(class_ = 'jsx-2085888330 results-table')
    data = []
    for row in state.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
                text = column.get_text()
                data.append(text)
    while("" in data) : 
        data.remove("") 
    state_info= []
    for i in data:
        state_info.extend(i.split('%'))
    state_info.insert(0, s)  
    state_data.append(state_info)

#changing the order of the lists
#the order the data pulled varied depending who the candidate that won that state
state_data_cleaned= []

for i in state_data:    
    if i[1] == 'Trump*gop':
        order = [0,4,5,6,1,2,3]
        update = [i[t] for t in order]
        state_data_cleaned.append(update)
    else:
        state_data_cleaned.append(i)
        
#creating a dataframe form the elections 2020 data
election_2020 = pd.DataFrame(state_data_cleaned, columns =['State','dem_candidate', 'dem_percent','dem_num', 'rep_candidate', 'rep_percent', 'rep_num']) 
   

#DETERMINING WINNING PARTY AND ADDING NEW COLUMN
def party(row):
    if row['dem_percent'] > row['rep_percent']:
        val = 'D'
    else:
        val = 'R'
    return val

    if row['dem_percent'] > row['rep_percent']:
        val = 'Dem'
    else:
        val = 'Trump'
    return val
election_2020['PARTY'] = election_2020.apply(party, axis = 1)


#SELECT VARIABLES OF INTEREST
results_2020 = election_2020[['State', 'PARTY']]
#ADDING IMAGE WITHIN DATAFRAME
results_2020['Election_2020'] = results_2020['PARTY'].apply(lambda x: pic(x))

#ADDING STATE ABREVIATIONS WITH SELECTION AND REORDERING OF COLUMNS
results_2020['STATE ABBREVIATION'] = results_2020['State']
results_2020.replace({"STATE ABBREVIATION": us_state_abbrev}, inplace = True)
results_2020.drop('State', axis=1, inplace = True)
results_2020 = results_2020[['STATE ABBREVIATION', 'Election_2020']]

#################################################################################
 #2016 DATA
 #SOURCE: https://www.fec.gov/introduction-campaign-finance/election-and-voting-information/
#################################################################################

#DOWNLOADING 2016 DATA 
url = 'https://www.fec.gov/documents/1890/federalelections2016.xlsx'
election_2016 = pd.read_excel(url, '2016 Pres General Results')


#FILTERING FOR DATA FOR THE WINNER OF EACH STATE
#REMOVING WASHINGTON DC
election_2016 = election_2016[election_2016['WINNER INDICATOR']=='W']
election_2016.reset_index(drop=True, inplace=True)


election_2016.drop(election_2016.index[8], inplace = True)
election_2016.reset_index(drop=True, inplace=True)

#CHANGING CODE FOR PARTY
def party(row):
    if row['PARTY'] == 'REP':
        val = 'R'
    else:
        val = 'D'
    return val

election_2016['PARTY'] = election_2016.apply(party, axis = 1)


#ADDING IMAGE WITHIN DATAFRAME
results_2016 = election_2016[['STATE ABBREVIATION', 'PARTY']]
results_2016['Election_2016'] = results_2016['PARTY'].apply(lambda x: pic(x))
results_2016 = results_2016[['STATE ABBREVIATION', 'Election_2016']]

#JOINS
results_full= pd.merge(results_2020, results_2016, on = 'STATE ABBREVIATION', how='inner')


#################################################################################
#DOWNLOADING 2012 DATA 
#################################################################################


url = 'https://www.fec.gov/documents/1684/2012pres.xls'
election_2012 = pd.read_excel(url, '2012 Pres General Results')


#FILTERING FOR DATA FOR THE WINNER OF EACH STATE
election_2012 = election_2012[election_2012['WINNER INDICATOR']=='W']
election_2012.reset_index(drop=True, inplace=True)

#DROPPING DC
election_2012.drop(election_2016.index[8], inplace = True)
election_2012.reset_index(drop=True, inplace=True)

#CHANGING CODE FOR PARTY
def pres_party(row):
    if row['FIRST NAME'] == 'Mitt':
        val = 'R'
        return val
    if row['FIRST NAME'] == 'Barack':
        val = 'D'
        return val

election_2012['PARTY'] = election_2012.apply(pres_party, axis = 1)

#ADDING IMAGE WITHIN DATAFRAME
results_2012 = election_2012[['STATE ABBREVIATION', 'PARTY']]
results_2012['Election_2012'] = results_2012['PARTY'].apply(lambda x: pic(x))
results_2012 = results_2012[['STATE ABBREVIATION', 'Election_2012']]


#JOINS
results_full= pd.merge(results_full, results_2012, on = 'STATE ABBREVIATION', how='inner')

#################################################################################
#DOWNLOADING 2008 DATA
#################################################################################

url = 'https://www.fec.gov/documents/1661/2008pres.xls'
election_2008 = pd.read_excel(url, '2008 PRES GENERAL RESULTS')


#FILTERING FOR DATA FOR THE WINNER OF EACH STATE

election_2008 = election_2008[((election_2008['PARTY'] == 'R')  |  (election_2008['PARTY'] == 'D'))]
election_2008 = election_2008.loc[election_2008.groupby("STATE ABBREVIATION")["GENERAL %"].idxmax()]
election_2008.reset_index(drop=True, inplace=True)

#REMOVE DC
election_2008.drop(election_2008.index[7], inplace = True)
election_2008.reset_index(drop=True, inplace=True)


#ADDING IMAGE WITHIN DATAFRAME
results_2008 = election_2008[['STATE ABBREVIATION', 'PARTY']]
results_2008['Election_2008'] = results_2008['PARTY'].apply(lambda x: pic(x))
results_2008 = results_2008[['STATE ABBREVIATION', 'Election_2008']]

#JOIN
results_full= pd.merge(results_full, results_2008, on = 'STATE ABBREVIATION', how='inner')



#################################################################################
#DOWNLOADING 2008 DATA
#################################################################################

url = 'https://www.fec.gov/documents/1628/2004pres.xls'
election_2004 = pd.read_excel(url, '2004 PRES GENERAL RESULTS')


#FILTERING FOR DATA FOR THE WINNER OF EACH STATE

election_2004 = election_2004[((election_2004['PARTY'] == 'R')  |  (election_2004['PARTY'] == 'D'))]
election_2004 = election_2004.loc[election_2004.groupby("STATE ABBREVIATION")["GENERAL %"].idxmax()]
election_2004.reset_index(drop=True, inplace=True)

#REMOVE DC
election_2004.drop(election_2004.index[7], inplace = True)
election_2004.reset_index(drop=True, inplace=True)


#ADDING IMAGE WITHIN DATAFRAME
results_2004 = election_2004[['STATE ABBREVIATION', 'PARTY']]
results_2004['Election_2004'] = results_2004['PARTY'].apply(lambda x: pic(x))
results_2004 = results_2004[['STATE ABBREVIATION', 'Election_2004']]

#JOIN
results_full= pd.merge(results_full, results_2004, on = 'STATE ABBREVIATION', how='inner')


#OUTPUT HTML TABLE
def path_to_image_html(path):
    return '<img src="'+ path + '" width="60" >'

#%% Topic Model
def tmodel():
    pytrend = TrendReq()

#Query Google Trends API

    pytrend.build_payload(kw_list=['election results'])

    related_queries = pytrend.related_queries()

    states = ['alabama','alaska','arizona','arkansas','california','colorado',
          'connecticut','deleware','florida','georgia','hawaii','idaho',
          'illinois','indiana','iowa','kansas','kentucky','louisiana','maine',
          'maryland','massachusetts','michigan','minnesota','mississippi',
          'missouri','montana','nebraska','nevada','new hampshire',
          'new jersey','new mexico','new york','north carolina','north dakota',
          'ohio','oklahoma','oregon','pennsylvania','rhode island',
          'south carolina','south dakota','tennessee','texas','utah','vermont',
          'virginia','washington','west virginia','wisconsin','wyoming']

    colors = ['blue','blue','blue','blue','blue','blue','blue','blue','blue',
          'blue','blue','blue','blue','blue','blue','blue','blue','blue',
          'blue','blue','blue','blue','blue','blue','blue']
    count = 0

#Check each row of results for state names, change the color corresponding to
#that result in the bar chart
    for value in related_queries['election results']['rising']['query']:
        for s in states:
            if s in value:
                colors[count]='red'
        count += 1

#Construct Graph
    sn = np.arange(related_queries['election results']['rising'].size)

    plt.title('Trending Election Topics',fontsize=20)

    plt.xlabel('Topics',fontsize=15)
    plt.ylabel('Searches',fontsize=15)

    plt.ticklabel_format(style='plain',axis = 'y')
    plt.annotate('Red Columns are Results About States', xy=(0.75,0.75),
                 xycoords = 'axes fraction',fontsize=20)
    plt.xticks(sn, related_queries['election results']['rising']['query'], 
               rotation=45, fontsize=12)
    plt.yticks(np.arange(0,1000000,step=100000),['0','100,000','200,000','300,000',
               '400,000','500,000','600,000','700,000','800,000','900,000',
               '1,000,000'],fontsize=15)

    plt.bar(related_queries['election results']['rising']['query'], 
            related_queries['election results']['rising']['value'], color=colors)
    plt.show()


#%% Program 
def main():
    continueFlag = True
    while continueFlag:
        menuRequest = menu()
        if menuRequest == 1:
            results_full.to_html(escape=False, formatters=dict(Election_2020=path_to_image_html, Election_2016=path_to_image_html, Election_2012=path_to_image_html, Election_2008=path_to_image_html, Election_2004=path_to_image_html))
            HTML(results_full.to_html(escape=False,formatters=dict(Election_2020=path_to_image_html, Election_2016=path_to_image_html, Election_2012=path_to_image_html, Election_2008=path_to_image_html, Election_2004=path_to_image_html)))
            results_full.to_html('ElectionComparison.html',escape=False, formatters=dict(Election_2020=path_to_image_html, Election_2016=path_to_image_html, Election_2012=path_to_image_html, Election_2008=path_to_image_html, Election_2004=path_to_image_html))
            TGREEN =  '\033[32m' # Green Text
            ENDC = '\033[m' # reset to the defaults
            print (TGREEN + "Election Comparison HTML file has been downloaded! Check current directory" , ENDC)
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
            covid()
        elif menuRequest == 4:
            tmodel()
        elif menuRequest == 0:
            print("You have quit.")
            continueFlag = False
    
    
if __name__ == "__main__":
    main()
    
    
    
    