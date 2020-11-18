#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:52:15 2020

@author: nolanroosa
"""

#Question 1a
import math
dir(math)

#1b
degree = input('Enter an angle in degrees: ')
degree = float(degree)
theta = math.radians(degree)
print(theta)

#1c
left = (math.sin(theta)*math.sin(theta)) + (math.cos(theta)*math.cos(theta))
right = 1
if left == right:
    print('Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
else:
    print('Not Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)

left = math.tan(theta)
right = math.sin(theta) / math.cos(theta)
if left == right:
    print('Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
else:
    print('Not Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
    
left = math.cos(theta)
right = math.sin((math.pi/2) - theta)
if left == right:
    print('Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
else:
    print('Not Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)

left = math.cos(2*theta)
right = (math.cos(theta)*math.cos(theta)) - (math.sin(theta)*math.sin(theta))
if left == right:
    print('Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
else:
    print('Not Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
    
left = math.sin((theta/2))
right = math.sqrt((1-math.cos(theta))/2)
if left == right:
    print('Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)
else:
    print('Not Equal')
    print('%3.18f' % left)
    print('%3.18f' % right)

#The variables can be unequal due to differences in rounding around the 16 or 17 decimal place point





#Question 2a
sentence = "Assign the string variable sentence as this sentence. Display it, then display it in all capitals."
print(sentence)
print(sentence.upper())

#2b
print(sentence.split(' '))

#2c
print(sentence.split('s'))

#2d
print(sentence.find('ten'))
print(sentence.find('ten', 31))

#2e
tabby = sentence.replace(' ', '\t')
print(tabby)




#Question 3a
speed = float(input('Enter a speed in MPH: '))
mps = speed/(1/.447)
print('%3.2f mph = %3.2f m/s' % (speed, mps))

#3b
if speed >= 25:
    print('Fast')
elif speed < 5:
    print('Slow')
else:
    print('Meh')

#3c
pounds = float(input('Enter the weight of an object in pounds: '))
kg = pounds/(1/.4536)
print('%3.2f pounds = %3.2f kg' % (pounds, kg))


#3d
if kg > 200:
    print('Heavy')
elif kg < 100:
    print('Light')
else:
    print('Medium')
    




#Question 4
#4a,b,c
f = open('gradebook.txt', 'r')
name = []
id = []
grade = []
count = 0
total = 0
lettergrade = []
for line in f:
    x = line.split(',')
    name.append(x[0])
    id.append(x[1])
    grade.append(int(x[2]))
    count  += 1
    total += int(x[2])
    
    if int(x[2])> 90:
        lettergrade.append('A')
    elif int(x[2]) > 80:
        lettergrade.append('B')
    elif int(x[2]) > 70:
        lettergrade.append('C')
    elif int(x[2]) > 60:
        lettergrade.append('D')
    else:
        lettergrade.append('F')
f.close()

#4b
print('\nThe class roster:', name, '\n')
print('The student ids:', id, '\n')
print('Student grades:', grade, '\n')

#4c
avg = total/count
print('The average score was: %3.2f percent\n' % (avg))

#4d
print('The letter grades were: ', lettergrade)


















