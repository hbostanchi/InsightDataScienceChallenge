#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:51:58 2018

@author: halleh
"""


import pandas as pd
import os

#os.chdir('..')
path=os.getcwd()

actual=pd.read_table(path+'/input/actual.txt', delimiter='|', names=('time', 'stock', 'price')) #load actual file
max_time=max(actual.time) #find max time within actual data
min_time=min(actual.time) # find min time using actual data, in case it does not start from 1

predicted = pd.read_table(path+'/input/predicted.txt', delimiter='|', names=('time', 'stock', 'price')) #load predicted file

fileHandle = open(path+'/input/window.txt', 'r') #load window value
window=fileHandle.readlines()
window=int(window[0])
fileHandle.close()

output = open(path+'/output/comparison.txt', 'w') #opening an empty output file

merged_table=pd.merge(actual, predicted, on=['time','stock'], how='inner') #merging actual and predicted value and drop nan value
error_table=abs(merged_table.price_x-merged_table.price_y) #calculating absolute error for all points
merged_table['error']=error_table #adding the error coloumn to the merged table

if (max_time-min_time>=window): #check if window is smaller than the data range
    for i in range(min_time, max_time-window+2): #looping for every line in the output
        for j in [i,i+window-1]: #writing the averaging window with pipe delimiter
            output.write(str(j)+'|')
        error_subset=merged_table.loc[merged_table['time'].isin(range (i,i+window)) ]   #  locating all actual data within this window                
        if len(error_subset)!=0:
            error_av=sum(error_subset.error)/len(error_subset) #calculating error average for this window if the data within this window is non-zero 
            output.write("{0:.2f}".format(error_av)+'\n')
           # print(error_av) 
        else:
            output.write('NA\n')    #writing NA for non-existant data               
output.close()