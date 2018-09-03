#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:58:29 2018

@author: halleh
"""

#from pandas import DataFrame
import pandas as pd
#import numpy as np


predicted = pd.read_table('predicted.txt', delimiter='|', names=('time', 'stock', 'price'))

actual=pd.read_table('actual.txt', delimiter='|', names=('time', 'stock', 'price'))
max_time=max(actual.time)
min_time=min(actual.time)
stock_name=pd.unique(actual.stock)
#stock_size=len(stock_name)

fileHandle = open('window.txt', 'r')
window=fileHandle.readlines()
window=int(window[0])
fileHandle.close()

output = open("comparison.txt", "w")

if (max_time-min_time>=window):
    for i in range(min_time, max_time-window+2):
        error=0
        counter=0
        #print(i)
        for j in range(i,i+window):
            #print(j)
            output.write(str(j)+'|')
            for k in stock_name:
                actual_point=actual.loc[(actual['time'] == j) & (actual['stock'] ==k)]
                predicted_point=predicted.loc[(predicted['time'] == j) & (predicted['stock'] ==k)]
                if len(predicted_point)!=0:
                    #print(k)
                    counter=counter+1
                    error=error+abs(float(actual_point.price)-float(predicted_point.price))
                    #print(error)
        error_av=error/counter
        output.write(str(error_av)+'\r\n')
        print(error/counter)            
output.close()