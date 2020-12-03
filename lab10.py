#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:50:38 2020

@author: nolanroosa
"""

# 1

with open('/Users/nolanroosa/Downloads/lab10.txt', 'r') as lab:
    lab10 = []
    for line in lab:
        line = line.strip('\n')
        lab10.append(line)      
print(lab10)

import re

(a.) r'a+a*'
(b.) r'[aeiou]?'
(c.) r'(ae)[ae]'
(d.) r'[0-9]+[0-9]?'
(e.) r'(09){2}'
(f.) r'0|9'
(g.) r'[0-9]{3}-[0-9]{4}'
(h.) r'\([0-9]{3}\)[0-9]{3}-[0-9]{4}'
(i.) r'[0-9]{5}'
(j.) r'[0-9]{3}-[0-9]{2}-[0-9]{4}'
(k.) r'^[aeiou]+(aeiou)+[aeiou]*[aeiou]$'

def search(p):
    for i in lab10:
        if re.search(p, i) != None:
            print('\nSearch Pattern: %s \nResult: %s\n' % (p, i))


p =  r'^[aeiou]+(aeiou)+[aeiou]*[aeiou]$'
search(p)
            
# 2a
p =  r'hte|eht|the|teh'
search(p)
    
# 2b
p =  r'\.'
search(p)

# 2c
p =  r'\('
search(p)

# 2d
p =  r'[a]+[e]'
search(p)
            
# 2e
p =  r'[a+e]'
search(p)
# 2f
p =  r'\*'
search(p)

# 2g
p =  r'(.csv)'
search(p)

# 2h
p = r'[01]\-+[0-9]{2,7}\-+[0-9]{1,6}\-+[X0-9]'
search(p)
            
# 
isbnList = []
def search(p):
    for i in lab10:
        if re.search(p, i) != None:
            isbnList.append(i)
p = r'[01]\-+[0-9]{2,7}\-+[0-9]{1,6}\-+[X0-9]'
search(p)           
print(isbnList)          

for i in isbnList:
    if len(i) == 10+3:
        index = 0
        modulo = 10
        checkSum = 0
        while index < 10:
            checkSum += (int(i[index]) % modulo)
            index += 1
            modulo -= 1
        if checkSum > 0:
            print('ISBN: {} is not valid.'.format.i)
        else:
            print('ISBN: {} is valid.'.format.i)
            
            
            
            
            
            
            
        
            
            
            
            
            