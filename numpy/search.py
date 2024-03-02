import numpy as np

#search
np1 = np.array([1,2,3,4,5,6,7,8,9,10,3])

x = np.where(np1 == 3)
print(np1)
print(x[0]) #gives the index of the element


#return odd numbers
z = np.where(np1%2 == 1)
print(z)