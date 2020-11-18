#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:54:48 2020

@author: nolanroosa
"""
# 1
import sqlite3
connection = sqlite3.connect('/Users/nolanroosa/Downloads/db/dogsdb.sqlite3')

# 2
c = connection.cursor()
cursor = c.execute('SELECT * FROM dogs')
table = cursor.fetchall()
type(table)
for row in table:
    print(row)
    
# 3
print(cursor.description)
print(i[0] for i in cursor.description)
colnames = []
for i in cursor.description:
    colnames.append(i[0])
print(colnames)

# 4
import pandas as pd
dogsDF = pd.DataFrame(table, columns = colnames)
print(dogsDF)

# 5
breeds = [ ['Mutt', 'Mangy and skinny'], ['Boxer', 'Short, always looks grumpy'], ['Pekingese', 'Not really a dog'], ['Basset', 'So much skin'],
['Beagle', 'Cute-ish'], ['Irish_Setter', 'Drinks your whiskey'], ['Terrier',
'Fetch, boy'], ['Whippet', 'Whippet good'], ['Yorkie', 'Cute'], ['Gread Dane',
'So huuuge'], ['Akita', 'or is it Atika?'], ['Great Dane', 'Not that great']]

# 6
table = """CREATE TABLE IF NOT EXISTS Breeds(
BREED           VARCHAR(20) PRIMARY KEY,
DESCRIPTION     VARCHAR(40));"""
                                                                 
cursor.execute(table)                                                      

query = 'INSERT INTO Breeds VALUES(?,?)'
cursor.executemany(query, breeds)

# 7
cursor.execute('SELECT * FROM Breeds')
cursor.fetchall()

# 8
joinQuery = 'SELECT DISTINCT * FROM Breeds JOIN dogs ON breed'
cursor.execute(joinQuery)
cursor.fetchall()

# 9
ageQuery = 'SELECT DISTINCT Name, Age FROM Breeds JOIN dogs WHERE age >= 5'
cursor.execute(ageQuery)
cursor.fetchall()

# 10
avgAgeQuery = 'SELECT AVG(dogs.Age) FROM dogs JOIN Breeds'
cursor.execute(avgAgeQuery)
avg = cursor.fetchall()

print("{} is the average age of the dogs".format(avg))









                                                                 
                                                                 