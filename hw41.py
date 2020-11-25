#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:55:00 2020

@author: nolanroosa
"""

with open('/Users/nolanroosa/Desktop/Python/pop.csv', 'r') as pop:
    states = []
    pop.readline() 
    for line in pop:
        line = line.strip('\n')
        states.append(line)      
print(states)

import re
# 1.01
p = 'Oregon'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))

# 1.02
p = 'O'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))

# 1.03
p = r'[op]'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))
            
# 1.04
p = r'^1'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))
            
# 1.05
p = r'0$'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))

# 1.06
p = r'[s-zS-Z]'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))

# 1.07
p = r'[0*]'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, state))

# 1.08
p = r'5.*4.*3.*'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \n Result: %s\n' % (p, state))

# 1.09
p = r' '
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \n Result: %s\n' % (p, state))

#1.10
p = '[Ii].*[Ii]'
for state in states:
    if re.search(p, state) != None:
            print('\nSearch Pattern: %s \n Result: %s\n' % (p, state))


