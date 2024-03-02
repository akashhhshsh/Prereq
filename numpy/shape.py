import numpy as np

#Create 1-D Numpy array and get shape
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(np1.shape)

#Create 2-D Numpy array and get shape, (rows/column)
# np2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(np2.shape)

#Reshape 2-D
# np3 = np1.reshape(3,4)
# print(np3)
# print(np3.shape)

#Reshape 3-D
np4 = np1.reshape(2,3,2)    #2 row 3 column and 2 elements
print(np4) 
print(np4.shape)

#flatten to 1-D
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)