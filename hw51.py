#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:20:51 2020

@author: nolanroosa
"""

# 1
import pandas as pd
weather = pd.read_csv("/Users/nolanroosa/Downloads/homework5/weather5.csv")
print(weather)


print("\nWeather Table Columns: ")
for col in weather.columns:
    print(col)
    
numberColumns = 0    
for col in weather.columns:
    numberColumns += 1
print("\nNumber of Weather Columns: {}".format(numberColumns))

numberRows = 0
for i in weather["Temperature"]:
    numberRows += 1
print("\nNumber of Temperature Entries: {}".format(numberRows))

weather = weather.dropna()
numberRows = 0
for i in weather["Temperature"]:
    numberRows += 1
print("\nNumber of Temperature Entries (CLEANED): {}".format(numberRows))


def filter(i):
    if i > 100:
        i = 100
    elif i < 0:
        i = 0
    else:
        i = i
    return i

weather["Humidity"] = weather["Humidity"].apply(filter)
print(weather)


# 2
def toTime(i):
    x = i.split(":")
    hour = int(x[0])
    minute = int(x[1])
    if hour > 12:
        hour = hour - 12
        amPm = 'PM'
    else:
        amPm = 'AM'
    return "{}:{:02}".format(hour, minute), amPm

x = []
y = []
for i in weather['Time']:
    i = toTime(i)
    x.append(i[0])
    y.append(i[1])

weather['12-hour'] = x
weather['AM-PM'] = y

weather = weather[['Time', '12-hour', 'AM-PM', 'Temperature', 'Humidity', 'Wind', 'Clouds']]
print(weather)

# 3
def toMinutes(i):
    x = i.split(":")
    hour = int(x[0])
    minute = int(x[1])
    total = ((hour*60) + minute)
    return total

z = []
for i in weather['Time']:
    i = toMinutes(i)
    z.append(i)
weather['Elapsed'] = z
weather = weather[['Time', '12-hour', 'AM-PM', 'Elapsed', 'Temperature', 'Humidity', 'Wind', 'Clouds']]
print(weather)

# 4
import matplotlib.pyplot as plt

columns = weather.columns

plt.title('Temperature Data')
plt.xlabel(columns[3])
plt.ylabel(columns[4])
plt.scatter(weather['Elapsed'], weather['Temperature'])

# 5
import seaborn as sns
plt.title('Humidity Data')
sns.lineplot(x = weather['Elapsed'], y = weather['Humidity']) 

# 6
plt.title('Wind')
plt.hist(weather['Wind'], bins = 5)

# 7
plt.title('Temperature Data')
plt.xlabel(columns[3])
plt.ylabel(columns[4])
plt.ylim(0, max(weather['Temperature'])+1)
plt.scatter(weather['Elapsed'], weather['Temperature'])

# 8
corr = weather.corr()
print(corr)
tempHumidCor = round(corr['Temperature'][2], 2)
plt.title('Temperature X Humidity Regression')
plt.annotate('Correlation =  '+ str(tempHumidCor), xy=(0.5,0.1), xycoords= 'axes fraction')
sns.regplot(x = 'Temperature', y = 'Humidity', data = weather)

# 9
sns.relplot(data = weather, x= 'Elapsed', y= 'Temperature', col="AM-PM", 
            size = 'Temperature', sizes = (20,200))

sns.relplot(data = weather, x= 'Elapsed', y= 'Temperature', col="Clouds", 
            size = 'Temperature', sizes = (20,200))

# 10
sns.factorplot(data = weather, x= 'Clouds', y= 'Temperature', col="AM-PM")
sns.boxplot(data = weather, x= 'Clouds', y= 'Temperature')

