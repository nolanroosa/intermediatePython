#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:28:05 2020

@author: nolanroosa
"""

# 1
# a: any vowel
# b: ends with a vowel
# c: starts with a vowel
# d: a number, and then as many repeating of a number
# e: 0 or more occurances of a single integer from 0-9
# f: starts with b, followed by a digit, and then a possible repeating digit, ends with b
# g: repeating digit, two 0-9 in the middle, and ends with repeatindigit
# h: any uper or lowercase letter, repeating letter or number
# i: plus or minus sign option match, repeating digit, repeating digit
# j: any repeating or non repeating number?
# k: a single repeating or non repeating number?

with open ('/Users/nolanroosa/Downloads/lab9.txt', 'r') as f:
    lab9 = []
    for line in f:
        line = line.strip('\n')
        lab9.append(line)

pats =  [r'[aeiou]',  r'[aeiou]$', r'^[aeiou]',  r'[0-9][0-9]*',  r'[0-9]*', r'\b([0-9][0-9]*)\b', r'[^0-9]*[0-9][0-9]*[^0-9]*',  r'[_a-zA-Z][_a-zA-Z0-9]*', r'[\+\-]?[0-9]*\.[0-9]*',  r'\([0-9]+\)', r'\[[0-9]+\]']

import re
for p in pats:
    for line in lab9:
        if re.search(p, line) != None:
            print('Pattern: %s word: %s' % (p, line))

# it looks like j returns a string where k returns a int?
#still unsure about the decimal point

pats2 = [r'[0]', r' [0-9][0-9] ', r'^\+', r'\+$', r'\([0-9][0-9]\)', r'[0-9]', r'\/', r'^[a]', r'^a']
for p in pats2:
    for line in lab9:
        if re.search(p, line) != None:
            print('Pattern: %s word: %s' % (p, line))