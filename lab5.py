#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 08:59:16 2020

@author: nolanroosa
"""

import pandas as pd

# Question 1a
a = pd.DataFrame({'Index': ['Fido', 'Barfy', 'Lassy'],
                   'Age': [7,3,17], 'Breed':["Mix", "Corgi", "Collie"]})

myList = [['Fido',7,'Mix'], ['Barfy', 3, 'Corgi'], ['Lassie', 17, 'Collie']]
b = pd.DataFrame(myList, columns = ['Name', 'Age', 'Breed'])

c = pd.DataFrame(b)
c.rename(index = {0: 'Fido', 1:'Barfy', 2:'Lassie'}, inplace = True)
print(a)
print(b)
print(c)

# 1b
a.iloc[0:]['Index']
b.iloc[1]
c.loc['Lassie']

# 1c
a.iloc[1]['Index']
b.iloc[0][1]
c.iloc[2][0]

# 1d
a.rename(index = {0: 'Fido', 1:'Barfy', 2:'Lassie'}, inplace = True)
print(a)

# 1e
b = b.append({'Name': ' ', 'Age':' ', 'Breed': 'Pitbull'}, ignore_index = True)
print(b)

# 1f
c['Weight'] = [20, 15, 35]
print(c)

# Question 2a
salesData = pd.DataFrame({'Sales':[2000.43, 1887.58, 2729.10, 2555.55, 4208.15], 'Profit': [234.12, 184.45, 302.14, 289.75, 441.12]})
salesData.rename(index = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}, inplace = True)
print(salesData)

# 2b
salesData.iloc[0:]['Sales']
salesData.loc['Wednesday']
salesData.loc['Wednesday'][1]

# 2c 
salesData['#Customers'] = [12,10,8,11,22]
print(salesData)

# 2d
salesData.loc['Saturday'] = [1793.00, 184.57, 9]
print(salesData)

# 2e
print(salesData['Sales'].sum())
print(salesData['Profit'].sum())

print('\nThe weekly sales total was {}\n'.format(salesData['Sales'].sum()))
print('The weekly profit total was {}\n'.format(salesData['Profit'].sum()))
print('The weekly number of customers was {}'.format(salesData['#Customers'].sum()))


# 2f
print(salesData['Sales'].mean())
print(salesData['Profit'].mean())

print(salesData.idxmax(axis = 0)[0])
print(salesData.idxmax(axis = 0)[1])

print(salesData.loc[salesData.idxmax(axis = 0)[0]])
print(salesData.loc[salesData.idxmax(axis = 0)[1]])








