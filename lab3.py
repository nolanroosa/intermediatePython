#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:20:38 2020

@author: nolanroosa
"""
#question 1
numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
with open('numbers.txt', 'w') as f:
    for i in numbers:
        f.write('%d\n' % (i))

#question 2
with open('numbers.txt', 'r') as f:
    myNums = []
    for i in f:
        i = int(i)
        myNums.append(i)
print(numbers == myNums)

#question 3
import pickle as p
data = [('Fido', 12), ('Barfy', 8), ('Spot', 5), ('Yeller', 15)]
f = open('mydata.bin', 'wb')
p.dump(data, f)
f.close()

#question 4
j = open('mydata.bin', 'rb')
newdata = p.load(j)
j.close
print(data == newdata)

#question 5a
import numpy as np
x = np.arange(1, 3, 0.5)
x = x.reshape(4,1)
y = [-1.0, 1.0, -1.0, 1.0]
y = np.array(y)
y = y.reshape(4,1)
N = [[0, 1, 1, 0], [3, 2, 1, 0]]
N = np.array(N)
I = np.identity(4)

#5b
print(x)
print(y)
print(N)
print(I)

#5c
x.shape
y.shape
N.shape
I.shape

#5d
x.ndim
y.ndim
N.ndim
I.ndim

#5e
N[0, :]

#5f
N[: ,0]


#Question 6
#6a yes
x+y

#6b yes
x*y

#6c NO
x.dot(y)

#6d yes
(x.T).dot(y)

#6e yes
x.dot(y.T)

#6f yes
N*N

#6g NO
x*N

#6h NO
x.dot(N)

#6i NO
(x.T).dot(N)

#6j yes
N.dot(x)




