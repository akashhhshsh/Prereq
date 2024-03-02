import numpy as np

#slicing numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])

#return 2,3,4,5
print(np1[1:5])

#returning something till the end of the array
#4-9
print(np1[3:])

#return negative slices
#7,8
print(np1[-3:-1])

#steps
print(np1[1:5])  #2-5
print(np1[1:5:2])  #2-5 in steps of 2


#step of 2 on the entire array
print(np1[::2]) 

#slice a 2-D array
np2 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]])

#pull out a single item
print(np2[1,2]) #1,2 is index of 8

#slice 2-D array
print(np2[0:1,1:3]) 
#here 0:1 means 0th element till 1st element but not 1st element and secons is to access 0th element 

print(np2[0:2,1:3])
