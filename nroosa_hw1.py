#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:22:55 2020

@author: nolanroosa
"""

# Problem 1
with open('/Users/nolanroosa/Desktop/Python/pop.csv', 'r') as pop:
    headers = pop.readline()
    headers = headers.split(',')
    popdata = []
    for line in pop:
        x = line.split(',')
        x[0] = int(x[0])
        x[1] = int(x[1])
        x[-1] = int(x[-1])
        popdata.append(x)
for x in headers:
    print(x,'\t') 

print('\n{}\t{}\t{}\t\t\t\t{}'.format(*headers))
print('_ ' * 23, '\n')
for state in popdata:
    print('{}\t\t{}\t{:<22}{}'.format(*state))

#Question 2
byRegion = {}
with open('/Users/nolanroosa/Desktop/Python/pop.csv', 'r') as pop:
    pop.readline()
    for line in pop:
        x = line.split(',')
        if x[0] not in byRegion:
            byRegion[x[0]] = [x[2]]
        else:
            byRegion[x[0]].append([x[2]])
                
for x in sorted(byRegion.keys()):
    print('Region', x, ':')
    for name in byRegion[x]:
        if isinstance(name,str): 
            print('\t', name)
        else:
            print('\t',name[0])
        
# Question 3
with open('/Users/nolanroosa/Desktop/Python/pop.csv', 'r') as pop:
    popdata = []
    pop.readline()
    for line in pop:
       x = line.split(',')
       popdata.append((x[2], int(x[3])))

populations = []
for tup in popdata:
    populations.append(tup[1])
print('The minimum population is: ', min(populations), 'people.')
print('The maximum population is: ', max(populations), 'people.')

total = 0
count = 0
for i in populations:
    total += i
    count += 1
print('The average population is %7.2f' % (total/count),'people.')

continueFlag = True
stateNames = []
for tup in popdata:
    stateNames.append(tup[0])

while continueFlag:
    request = input('Enter the name of a state: ')
    if request == 'quit':
        continueFlag = False
        print('You have quit.')
    elif request not in stateNames:
        print('That is not a valid state. Enter another state: ')
    else:
        idx = stateNames.index(request)
        print(popdata[idx][0], popdata[idx][1])
          
# Question 4
x = 100
y = 1000
f = float(input('Enter the fox growth rate: '))
c = float(input('Enter the chicken growth rate: '))
e = float(input('Enter the eat-chicken rate: '))
k = -float(input('Enter the kill rate: '))
n = int(input('Enter the number of times to run the experiment: '))

import numpy as np
a = np.array([[f,e], [k,c]])
b = np.array([x,y])

print('\nTime Period\t','# Foxes\t', '# Chickens')
for i in range(n):
    b = np.matmul(a,b)
    if b[0] < 0:
        print('The Foxes have died out')
        break
    elif b[1] < 0:
        print('The chickens have died out')
        break
    else: 
        print('{:<11}\t{:<9}\t{}'.format(i, b[0], b[1]))
    
    
    
