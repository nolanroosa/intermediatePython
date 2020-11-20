#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:02:13 2020

@author: nolanroosa
"""

import requests
from bs4 import BeautifulSoup
# 1a
latitude = input('Enter a Latitude: ')
longitude = input('Enter a Longitude: ')
httpString ='https://forecast.weather.gov/MapClick.php?textField1={}&textField2=-{}'.format(latitude, longitude)
page = requests.get(httpString)

# 1b
soup = BeautifulSoup(page.content, 'html.parser')
conditions = soup.find(id="current-conditions")
condition_items = conditions.find_all(class_ = "text-right")
print(condition_items)

# this is from piazza, I was trying to index conditionitems[i] but was just getting
# the words and not the values

for i in range (len(condition_items)):
    print (condition_items[i].text,':', condition_items[i].find_next('td').text)


# 2a
import pandas as pd
column_names = ['Author', 'Title', 'Published Date']
list = []
pythonLibrary = pd.DataFrame(list, columns = column_names)

# 2b
import json
import requests

def fetchBook(isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'.format(isbn)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
    items = dict(data['items'][0])
    book = items['volumeInfo']
    booki = []
    if 'title' in book:
        booki.append(book['title'])
    else:
        booki.append(' ')
    if 'authors' in book:
        booki.append(book['authors'])
    else:
        booki.append(' ')
    if 'publishedDate' in book:
        booki.append(book['publishedDate'])
    else:
        booki.append(' ')
    list.append(booki)

# 2c
fetchBook(9780323552295)
fetchBook(1449340377)
fetchBook(9781491912058)
fetchBook(1687159106)


pythonLibrary.to_json('pythonLibrary.json')
newTable = pd.read_json('pythonLibrary.json')






