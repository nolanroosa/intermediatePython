#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:58:09 2020

@author: nolanroosa
"""

#Question 1a
a = [i for i in range(50,101)]

#1b
b = [i for i in range(1,21)]
b.append([i**2 for i in range(1,21)])
b.append([i**3 for i in range(1,21)])

#1c
c = [chr(i) for i in range(65, 91)]

#1d
d = [[c[j] for j in range(i)] for i in range(1,len(c))]



#Question 2a
def myInts():
    numbers = []
    for i in range(50,101):
        numbers.append(i)
    return numbers
newlist = myInts()
print(newlist)

#2b
def partb():
    newnumbers = []
    for i in range(1,21):
        newnumbers.append(i)
    for i in range(1,21):
        newnumbers.append(i**2)
    for i in range(1,21):
        newnumbers.append(i**3)
    return newnumbers
newlistb = partb()
print(newlistb)

#2c
def capitals():
    alphabet = []
    for i in range(65, 91):
        alphabet.append(chr(i))
    return alphabet
newlistc = capitals()
print(newlistc)

#2d
def subCaps(alphabet):
    bigalphabet = []
    for i in range(0,len(alphabet)):
        littlelist = []
        for j in range(i+1):
            littlelist.append(alphabet[j])
        bigalphabet.append(littlelist)
    return bigalphabet
print(subCaps(capitals()))

        
#Question 3a
k = {1:'dog', 2:'cat', 3:'gopher', 4:'hyrax', 5:'capybara'}
print(k)

#3b
ksearch = int(input('Enter an Integer: '))
if ksearch in k:
    print(k[ksearch])
else:
    print('Error')

#3c
k[6] = 'badger'
k[7] = 'groundhog'
k[8] = 'mole rat'
print(k)

#3d
loopsearch = 0
while loopsearch != -1:
    loopsearch = int(input('Enter an Integer: '))
    if loopsearch in k:
        print(k[loopsearch])
    else:
        print('Error')

#Question 4a
setA = {i for i in range(0,6)}
setB = {i for i in range(3,11)}
print(setA)
print(setB)

#4b
setC = setA & setB
print(setC)
    
#4c
setD = setA | setB
print(setD)

#4d
setE = setB - setA
print(setE)
    
