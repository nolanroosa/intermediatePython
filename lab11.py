#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:38:02 2020

@author: nolanroosa
"""

# 1
import pandas as pd
data = pd.read_csv("/Users/nolanroosa/Downloads/popAreaHousing.csv")
print(data)

# 2
corr = data.corr()
x = round(corr['Population'][1],2)
y = round(corr['Population'][2],2)
z = round(corr['Area'][2],2)
print(x)
print(y)
print(z)

# 3
import matplotlib.pyplot as plt

plt.title('Pop X Area')
plt.xlabel(data.columns[1])
plt.ylabel(data.columns[2])
plt.annotate('Correlation =  '+ str(x), xy=(0.5,0.1), xycoords= 'axes fraction')
plt.scatter(data['Population'], data['Area'], marker = '*', color = 'Blue')

# 4
plt.title('Pop X Housing Units')
plt.xlabel(data.columns[1])
plt.ylabel(data.columns[3])
plt.annotate('Correlation =  '+ str(y), xy=(0.6,0.1), xycoords= 'axes fraction')
plt.scatter(data['Population'], data['Housing Units'], marker = '*', color = 'darkgreen')

# 5
plt.title('Area X Population')
plt.xlabel(data.columns[2])
plt.ylabel(data.columns[1])
plt.annotate('Correlation =  '+ str(z), xy=(0.5,0.1), xycoords= 'axes fraction')
plt.scatter(data['Area'], data['Population'], marker = '*', color = 'red')

# 6
plt.pie(data['Population'], labels = data['State'])

# 7
plt.xticks([]) 
plt.bar(data['State'], data['Population'])

# 8
import seaborn as sns
plt.title('Pop X Area')
plt.annotate('Correlation =  '+ str(x), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.lineplot(x = 'Population', y = 'Area', marker = '*', data = data)

plt.title('Linear Regression Pop X Area')
plt.annotate('Correlation =  '+ str(x), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.regplot(x = 'Population', y = 'Area', marker = '*', data = data)

# 9
plt.title('Pop X Housing Units')
plt.annotate('Correlation =  '+ str(y), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.lineplot(x = 'Population', y = 'Housing Units', color = 'darkgreen', marker = '*', data = data)

plt.title('Linear Regression Pop X Housing Units')
plt.annotate('Correlation =  '+ str(y), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.regplot(x = 'Population', y = 'Housing Units', color = 'darkgreen', marker = '*', data = data)

# 10
plt.title('Area X Housing Units')
plt.annotate('Correlation =  '+ str(z), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.lineplot(x = 'Area', y = 'Housing Units', color = 'red', marker = '*', data = data)

plt.title('Linear Regression Area X Housing Units')
plt.annotate('Correlation =  '+ str(z), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.regplot(x = 'Area', y = 'Housing Units', color = 'red', marker = '*', data = data)

# 11
sns.pairplot(data=data)

# 12
#command line
# conda install -c plotly plotly-orca

import plotly.io as pio
pio.renderers
pio.renderers.default='png'

import plotly.express as px
fig = px.scatter_3d(data, x = 'Population', y = 'Area', z = 'Housing Units')
fig.show()














