#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:43:57 2016

@author: Louie
"""
import stocks as st
import scipy as sci
import matplotlib.pyplot as plt

#1

def percent_of_mean (olist):    # A function accepts a list as input

    newList = olist/sci.mean(olist)     #new list equal to oldlist divide by the mean of oldlist
    
    return newList     #return new list
    
#2

plt.figure(1)
plt.plot(st.trading_days, percent_of_mean(st.nasdaq), 'r*--',label="NASDAQ")    # Plot Nasdaq vs trading days
plt.plot(st.trading_days, percent_of_mean(st.sp500), 'b*--',label= "S&P 500")   # Plot sp500 vs trading days
plt.plot(st.trading_days, percent_of_mean(st.djia),  'k*--',label= "Dow Jones")     # Plot Dow Jones vs trading days
plt.ylabel('Index in percentage of mean')   # labeling and titling 
plt.xlabel('Day')
plt.title('Indexes in percentage of mean', size = 20.0)
plt.legend(loc = 4)     #relocate legend to lower right corner.

#3

def num_days_big_percent_chg (olist, per):  # A function accepts a list and a percentage
    count = 0   # Set count as 0
    for i in range(1,len(olist)):   # loop "the number of list" time, but skipping 0
        if (abs((olist[i] - olist[i-1])/olist[i-1]) > per):     #If the absolute value of the persentage change of element i of the index larger than percentage input
            count += 1      #add 1 to count
    return count 


#4

'''
A function accepts a list, and use the list as an input to function 'num_days_big_percent_chg' with 5 different percentages, 
(0.002, 0.004, 0.006, 0.008, 0.001, then turn a 5 numbers to a new list. 
'''
def setList (olist): 
    newList = [None]*5 # create a new list with 5 elements
    k = 0.002   # K is a percentage, starting from 0.2%, will add 0.2% each time the loop runs
    for i in range(5): # A for loop that loop 5 times
        newList[i] = num_days_big_percent_chg (olist, k) #Add the number from 'num_days_big_percent_chg in percentage k' to newList
        k += 0.002  # Add 0.002 to k
    return newList

plt.figure(2)
plt.plot([0.002, 0.004, 0.006, 0.008, 0.01], setList(st.nasdaq), 'r*--',label="NASDAQ") # Plot x as percentage, y as number of days 
plt.plot([0.002, 0.004, 0.006, 0.008, 0.01], setList(st.sp500), 'b*--',label= "S&P 500")
plt.plot([0.002, 0.004, 0.006, 0.008, 0.01], setList(st.djia),  'k*--',label= "Dow Jones")
plt.ylabel('Number of days') # Labeling and titling 
plt.xlabel('Percentage')
plt.title('Number of days vs. Percentage', size = 20.0)
plt.legend()
plt.show() #shows all the graph 

#5

def ascending_trading_days(dlist, olist):   # Function that accepts two list, trading days and index
    days = list(dlist)      #Create a list equal to trading days list
    for j in range(len(olist)):     #First for loop, loop "length of the index list" time
        mini = olist[j]     #Set mininum value as element j of the index list
        for i in range(j,len(olist)): #Second for loop, looping from j to length of index list
            if olist[i] < mini:     # if the element i from the index is smaller than minium value
                mini = olist[i]     #minimum value will equal to element i from the index
                olist[i] = olist[j] #Switching element i and j from the index
                olist[j] = mini     
                tem = days[i]   #Switching element i and j from days list
                days[i] = days[j]
                days[j] = tem 
    return days
    
#6
print ('The five highest trading days for djia: ')
print (ascending_trading_days(st.trading_days, st.djia)[-5:]) #print the last 5 number from function ascending_trading_days function 
print ('The five highest trading days for nasdaq: ')
print (ascending_trading_days(st.trading_days, st.nasdaq)[-5:])
print ('The five highest trading days for sp500: ')
print (ascending_trading_days(st.trading_days, st.sp500)[-5:])
