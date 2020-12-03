#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:38:28 2020

@author: nolanroosa
"""

topics = ['Python; Data Science', 'Data Analysis', 'Machine Learning', 'Deep Learning']

import json
import requests
import pandas as pd



def fetchBook(topic):
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(topic)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        pd.json_normalize (data['items'] )
    categoryi = []
    items = data['items']
    for i in items:
        i = dict(i)
        book = i['volumeInfo']
        booki = []
        if 'title' in book:
            booki.append(book['title'])
        else:
            booki.append(' ')
        if 'authors' in book:
            booki.append(book['authors'])
        else:
            booki.append(' ')
        categoryi.append(booki)
    return categoryi
    
bigTable = []
for category in topics:
    bigTable = bigTable + fetchBook(category)

print(bigTable)
bigTable = pd.DataFrame(bigTable, columns = ['TITLE', 'AUTHOR'])
print(bigTable)

print('\nTitle\t\t\t\t\t\t', 'Author')
for i in bigTable.index:
    print(bigTable['TITLE'][i][:25], '\t', bigTable['AUTHOR'][i])
    
    
    
    
    
    
