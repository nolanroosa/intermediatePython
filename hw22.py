#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:52:15 2020

@author: nolanroosa
"""

import pandas as pd
allPop = pd.read_csv('/Users/nolanroosa/Downloads/nstData.csv')

# a
allPop.head(2)
allPop.tail()

# b
allPop.describe()
allPop['ESTIMATESBASE2010'].describe()
allPop['ESTIMATESBASE2010'].describe()[1]

# c
states = allPop['NAME']
print(states)
states = states[5:]
print(states)

# d
newPop = allPop[allPop["STATE"] != 0]
states2 = newPop['NAME']
states == states2

# e
#populate with the correct columns
myPop = pd.DataFrame()
myPop["REGION"] = allPop["REGION"]
myPop["STATE"] = allPop["STATE"]
myPop["NAME"] = allPop["NAME"]
myPop["POPULATION"] = allPop["POPESTIMATE2010"]

#remove regions
myPop = myPop[5:]

#reindex
newindex = range(0, 52)
myPop = myPop.reset_index()
myPop = myPop.drop('index', axis = 1)

#puerto rico
myPop = myPop.replace('X', '5')

#region to int
myPop['REGION'] = pd.to_numeric(myPop['REGION'])
print(myPop)

#check
pop = pd.read_csv("/Users/nolanroosa/Desktop/Python/pop.csv")
print(pop)
pop == myPop
