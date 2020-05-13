# Table of Contents
 [Introduction](README.md#introduction)
 [Approach](README.md#Approach)
 [Testing](README.md#Testing)



## Introduction

This repository is created in response of Insight Data Science challenge question. The question ask for calculating error moving average between two given files. The solution uses Python code to read input files, analyze and generate the required output file. 


## Approach

The code uses single python file to perform the requested task. The machine that the code was developed uses Python3 compiler. 

The code uses Panda package to manipulate the data as table, and OS package in order to navigate to the correct folder that meets the requested repository structure. 

Both files of “predicted.txt’ and ‘actual.txt’ have been read using panda as DataFrame (table). Although the files have no headers, I assigned following headers for the three columns:
'time', 'stock', 'price'

The ‘window.txt’ file contains only single integer number and hence was read using Python. 

In order to match the two table rows and eliminate the NA rows, the code merges the two tables using inner approach. This results in a DataFrame with ‘price_x’ and ‘price_y’ columns for actual and predicted prices, respectively. Next the absolute error between these two variable are calculated and the results is appended to the merged DataFRAME.

In order to calculate the moving average within given window, the code uses a for loop for each of the output lines. the correct number of loops is calculated using start time, end time and window length. This allows us to handle the codes that are not necessarily start from time 1. Moreover I check if the window length is not larger than available data duration, otherwise an empty file is outputed. within each loop the data within given time window are located and the average is calculated and written to output file with correct delimiter time spans.

Another corner condition checked is if no match between actual and predicted values in a time window was found. In this case the code outputs NA on that given line.

Finally all the data are written in output file and the file is closed.


## Testing

The code was run successfully. However it failed the provided ‘TestSuite’. When investigated, I realized that all the errors are due to 0.01 difference between generated and reference output. Based not the challenge details, this is acceptable results, although the ‘TestSuite’ failed the code. Further investigation finds that this error points happens when the average error is *.**5, which can be rounded up or down depending not he compiler. I used Python3 and 2 compilers and both rounded down. However, the reference file seems to be rounding up. 



 
