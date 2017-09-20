#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:19:57 2016

@author: Louie
"""

import numpy as np
import stocks as st
import scipy as sci
import matplotlib.pyplot as plt

arrayDjia = np.array(st.djia)
arraySp500 = np.array(st.sp500)
arrayNasdaq = np.array(st.nasdaq)
arrayTD = np.array(st.trading_days)

#1

def percent_of_mean (oData):    
    """
    This fuction accepts a 1-D array, are calculate each element
    of the array as a percent of the mean value, then return to 
    a new list 
    """

    nData = (oData/np.mean(oData))*100     
    
    return nData     

#2
plt.figure(1)
plt.plot(arrayTD, percent_of_mean(arrayNasdaq), 'r*--',label="NASDAQ")    # Plot Nasdaq vs trading days
plt.plot(arrayTD, percent_of_mean(arraySp500), 'b*--',label= "S&P 500")   # Plot sp500 vs trading days
plt.plot(arrayTD, percent_of_mean(arrayDjia),  'k*--',label= "Dow Jones")     # Plot Dow Jones vs trading days
plt.ylabel('Index in percentage of mean')   # labeling and titling 
plt.xlabel('Day')
plt.title('Indexes in percentage of mean', size = 20.0)
plt.legend(loc = 4)     #relocate legend to lower right corner.

#3
def num_days_big_percent_chg (oData, per):
    '''
    The fuction accepts a 1-d array and a percentage, then calculates the percentage
    change of each element of the array compare with input percent. Count the time of 
    number of percentage change of each element larger than input percent,
    and return to the total number 
    '''
    
    nData = abs((oData[1:] - oData[:-1]) / oData[:-1]) #calculate the absolute value of percentage change compare pervious day
    return np.sum(nData>per) #return the sum of a list that contain: if the array element is larger than per, return true(1), else false(0) 

#4
def setList (oData): 
    """
    A function accepts a list, and use the list as an input to function 'num_days_big_percent_chg',
    with 5 different percentages, (0.002, 0.004, 0.006, 0.008, 0.001,
    then turn a 5 numbers to a new list. 
    """
    
    newData = [None]*5 # create a new list with 5 elements
    k = 0.002   # K is a percentage, starting from 0.2%, will add 0.2% each time the loop runs
    for i in range(5): 
        newData[i] = num_days_big_percent_chg (oData, k) #Add the number from 'num_days_big_percent_chg in percentage k' to newList
        k += 0.002  # Add 0.002 to k
    return newData


plt.figure(2)
plt.plot([0.2, 0.4, 0.6, 0.8, 1], setList(arrayNasdaq), 'r*--',label="NASDAQ") 
plt.plot([0.2, 0.4, 0.6, 0.8, 1], setList(arraySp500), 'b*--',label= "S&P 500")
plt.plot([0.2, 0.4, 0.6, 0.8, 1], setList(arrayDjia),  'k*--',label= "Dow Jones")
plt.ylabel('Number of days')
plt.xlabel('Percentage')
plt.title('Number of days vs. Percentage', size = 20.0)
plt.legend()


#5

def moving_average (oData):
    '''
    This function accepts a 1-D array, 
    averaging the elements of the array for the last three element 
    and returns a list of three-day simple moving average. 
    '''
    
    return (oData[:-2] + oData[1:-1] + oData[2:])/3


#6
plt.figure(3)
plt.plot(arrayTD,arrayNasdaq, 'b-', label = 'Nasdaq') # Plot Nasdaq vs trading days
plt.plot(arrayTD[2:], moving_average(arrayNasdaq), 'r--', label = 'SMA(3)') #Plot 3 days average vs trading days starting from day 3
plt.ylabel('Index')
plt.xlabel('day')
plt.title('Nasdaq Simple Moving Average', size = 20.0)
plt.legend(loc = 4)

plt.figure(4)
plt.plot(arrayTD,arraySp500, 'b-', label = 'Sp500') # Plot Sp500 vs trading days
plt.plot(arrayTD[2:], moving_average(arraySp500), 'r--', label = 'SMA(3)') #Plot 3 days average vs trading days starting from day 3
plt.ylabel('Index')
plt.xlabel('day')
plt.title('Sp500 Simple Moving Average', size = 20.0)
plt.legend(loc = 4)

plt.figure(5)
plt.plot(arrayTD,arrayDjia, 'b-', label = 'Djia') # Plot Djia vs trading days
plt.plot(arrayTD[2:], moving_average(arrayDjia), 'r--', label = 'SMA(3)') #Plot 3 days average vs trading days starting from day 3
plt.ylabel('Index')
plt.xlabel('day')
plt.title('Djia Simple Moving Average', size = 20.0)
plt.legend(loc = 4)
plt.show()

