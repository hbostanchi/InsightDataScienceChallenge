import pandas as pd

actual=pd.read_table('actual.txt', delimiter='|', names=('time', 'stock', 'price')) #load actual file
max_time=max(actual.time) #find max time within actual data
min_time=min(actual.time) # find min time using actual data, in case it does not start from 1

predicted = pd.read_table('predicted.txt', delimiter='|', names=('time', 'stock', 'price')) #load predicted file

fileHandle = open('window.txt', 'r') #load window value
window=fileHandle.readlines()
window=int(window[0])
fileHandle.close()

output = open("comparison.txt", "w") #opening an empty output file

if (max_time-min_time>=window): #check if window is smaller than the data range
    for i in range(min_time, max_time-window+2): #looping for every line in the output
        actual_subset=actual.loc[actual['time'].isin(range (i,i+window)) ]   #  locating all actual data within this window
        predicted_subset=predicted.loc[predicted['time'].isin(range (i,i+window)) ] #  locating all predicted data within this window
        error_subset=pd.merge(actual_subset, predicted_subset, on=['time','stock'], how='inner') #merging actual and predicted value and drop nan value
        error_av=sum(abs(error_subset.price_x-error_subset.price_y))/len(error_subset) #calculating error average for htis window 
        error_av=round(error_av,2) #rounding data to match example values
        for j in range(i,i+window): #writing the averaging window with pipe delimiter
            output.write(str(j)+'|')
        output.write(str(error_av)+'\r\n') #writing the error for this window
        #print(error_av)                
output.close()