#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:59:35 2020

@author: nolanroosa
"""
# Question 1

import pandas as pd
pop = pd.read_csv("/Users/nolanroosa/Desktop/Python/pop.csv")

def menu():
    print ('''
               Population Menu:    
           
               1. Display the entire table
               2. Display the total population of all the states
               3. Prompt for the name of a state. Display its population
               4. Display the table sorted by state name
               5. Dissplay the table grouped by region
               6. Display the table sorted by population, largest to smallest
               0. Quit
               ''')
    menuRequest = int(input('Enter a menu option: '))
    menuOption = []
    for i in range(0,7):
        menuOption.append(i)
    if menuRequest not in menuOption:
        print('\nEnter a valid menu item.')
    else:
        return(menuRequest)

def statereq():    
    stateRequest = input('Enter the name of a state: ')
    namedPop = pop.set_index('NAME')
    print('\nThe population of the entered state is', namedPop.loc[stateRequest][2])

def main():
    continueFlag = True
    while continueFlag:
        menuRequest = menu()
        if menuRequest == 1:
            print(pop)
        elif menuRequest == 2:
            print(pop['POPULATION'])
        elif menuRequest == 3:
            statereq()
        elif menuRequest == 4:
            print(pop.sort_values(by = 'NAME'))
        elif menuRequest == 5:
            print(pop.sort_values(by = 'REGION'))
        elif menuRequest == 6:
            print(pop.sort_values(by = 'POPULATION', ascending = False))
        elif menuRequest == 0:
            print("You have quit.")
            continueFlag = False
        
if __name__ == "__main__":
    main()
    
    
    
