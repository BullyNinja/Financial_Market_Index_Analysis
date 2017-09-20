#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:04:44 2016

@author: Louie
"""

import stocks as st
import scipy as sci
import matplotlib.pyplot as plt

#1
def myCorr (data1, data2):
    '''
    A function that take 2 time series data, and calculate
    the correlation coefficient between the two data. 
    '''
    sumData1 = 0
    sumData2 = 0
    for i in range(len(data1)): #using for loop calculate the sum of the data
        sumData1 += data1[i]
        sumData2 += data2[i]
    mean1 = sumData1/len(data1) #mean of data1
    mean2 = sumData2/len(data2) #mean of data2
    
    summ3 = 0
    summ4 = 0
    summ5 = 0
    for i in range(len(data1)): #calculate the Correlation coefficient
        summ3 += (data1[i] - mean1)**2
        summ4 += (data2[i] - mean2)**2
        summ5 += (data1[i] - mean1)*(data2[i] - mean2)
    std1 = (summ3/len(data1))**(1/2) #s.d. of data1
    std2 = (summ4/len(data2))**(1/2) #s.d. of data2
    cov12 = summ5/len(data1) #covariance of data1 and data2
    
    return cov12 / (std1*std2) #Correlation coefficient
    

print('Correlation between Nasdaq & Djia: ',myCorr(st.nasdaq, st.djia))
print('Correlation between Nasdaq & Sp500: ', myCorr(st.nasdaq, st.sp500))
print('Correlation between Sp500 & Djia: ', myCorr(st.sp500, st.djia))

#2
def myLag (oData, lag): 
    '''
    Taking two input: a time series data f(t) and the number of lag, 
    then calculates and return to the correlation between f(t) and f(t+lag).
    '''
    if lag == 0:
        return 1 #if lag is zero, oData is equal oData, and correlation is equal 1
    else:
        return myCorr(oData [:-lag], oData [lag:]) #correlation between f(t) and f(t+lag)
        
def setLag (oData, lag):
    '''
    Taking two input: a time series data f(t) and the number of lag
    then Calculates and return a list of lag autocorrelation in range(lag), 
    '''
    lagauto = [] 
    for i in range(lag):
        lagauto.append(myLag(oData,i)) 
    return lagauto 


#3

numLag = 20
plt.plot(range(numLag), setLag(st.djia,numLag),'b--',label = 'Djia')
plt.plot(range(numLag), setLag(st.nasdaq,numLag),'r--',label = 'Nasdaq')
plt.plot(range(numLag), setLag(st.sp500,numLag),'g--',label = 'Sp500')
plt.xlabel('Number of Lag')
plt.ylabel('correlation coefficient')
plt.title('f(t) vs. f(t+lag)')
plt.legend()
plt.show()

#4
'''
Y intercept is 1 because when lag day is zero, the two data is equal, and correlation is equal to 1
When the lag day increase, the correlation coefficient decrease, which means 
there are less relationship between f(t) and f(t+lag). Future index is 
less predictable by using today index when the time increase.  
'''
