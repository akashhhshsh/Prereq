import numpy as np

list1 = [1,2,3,4,5]
#print(list1)

#numpy - Numeric python
#ndarray - n-dimensional array

np1= np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

#range
np2 = np.arange(10)
print(np2)

#step
np3 = np.arange(0,10,2)
print(np3)

# Zeros
np4 = np.zeros(10)
print(np4)

#multi-dimensional zeros
np5 = np.zeros((2,10))
print(np5)

#full
np6 = np.full(10,7)
print(np6)

#multi=dimensional full
np7 = np.full((2,10),6)
print(np7)

#convert python lists to np
np8 = np.array(list1)
print(np8)

print(np8[0])