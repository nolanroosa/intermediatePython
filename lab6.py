#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:07:18 2020

@author: nolanroosa
"""

# Question 1
import pandas as pd
mydata = pd.read_csv("/Users/nolanroosa/Downloads/mydata.csv")

# Question 2
t1 = mydata[mydata.notnull()]
print(t1)
# Question 3
avgWeight= int(t1['Weight'].mean())
avgAge = int(t1['Age'].mean())

# Question 4
t2 = mydata.fillna({'Weight': avgAge}) 
print(t2)
# Question 5
t3 = mydata.fillna({'Age': avgAge})

# Question 6
t4 = t2.fillna({'Age': avgAge})

# Question 7
t5 = mydata.fillna(method='ffill')

# Question 8
t6 = t4.copy()
t6['Age'][t6['Age'] > 18.0] = '%5d' % (avgAge)

# Question 9
t7 = t6.copy()
t7['Weight'][t7['Weight'] >  150] = '%5d' % (avgWeight)
print(t7)

# Question 10
t8 = t7.astype({'Age' : int})

# Quetion 11
t9 = t8.fillna({'Name' : 'Barfy'})
t9['Name'] = t9['Name'].str.upper()
t9 = t9.rename(columns = {'Name':'Search Name'})

# Question 12
t10 = pd.concat([t9['Search Name'], t8], axis = 1)
print(t10)








