#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:00:27 2020

@author: nolanroosa
"""

#question 1a
import pandas as pd
a = pd.Series([i for i in range(5,1,-1)])
b = pd.Series([i for i in range(10,14)])
c = pd.Series([-1, -1, 0, 0])
print(a)
print(b)
print(c)

#1b
print(a+b)
print(b-a)
print(3*c)
print(a/b)
print(a/c)

#1c
print(a.rename({0:2, 1:3, 2:4, 3:5}))

#1d
print(a.rename({0:2, 1:3, 2:4, 3:5}, inplace = True))

#1e - now we have alot of NAN
print(a+b)
print(b-a)
print(3*c)
print(a/b)
print(a/c)

#question 2a
a.index
i = a.index
print(i)
b[:2]
c[-2:]

#2b the corresponding values for index 3 and 4 are NaN
d = b.reindex(a.index)
print(d)

#2c
pd.isnull(d)
pd.notnull(d)

#2d
e = a[pd.notnull(a)]
print(e)

#question 3a
week1 = pd.Series([50.0, 25.75, 10.0, 32.5, 15.8], index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
week2 = pd.Series([70.0, 5.8, 2.2, 17.1, 31.1], index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
print(week1)
print(week2)

#3b
week1 = week1.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Total'])
week1.loc['Total'] = week1.sum()
print(week1)

week2 = week2.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Total'])
week2.loc['Total'] = week2.sum()
print(week2)

#3c
week1 = week1.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Total', 'diff'])
week2 = week2.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Total', 'diff'])
week1.loc['diff'] = week1.sum() - week2.sum()
week2.loc['diff'] = week2.sum() - week1.sum()
print(week1)
print(week2)

#3d
week1.iloc[:2]
week2.iloc[2:-2]

#question 4a
states = pd.read_csv('/Users/nolanroosa/Desktop/Python/states.csv', index_col=0)
print(states)
#4b
print(states.index)
#4c
print(states.index[15])
print(states.iloc[15])
print(states.loc['Iowa'])
