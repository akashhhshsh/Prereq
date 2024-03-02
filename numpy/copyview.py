import numpy as np

#copy vs view
np1 = np.array([0,1,2,3,4,5])

#Create a view
# np2 = np1.view()
#In case of view changes in one will affect other
# print(f'Original NP1 {np1}')
# print(f'Orifginal NP2 {np2}')

# np1[0] = 41

# print(f'Changed NP1 {np1}')
# print(f'Orifginal NP2 {np2}')

np2 = np1.copy()
#In case of copy changes in one will not affect other
print(f'Original NP1 {np1}')
print(f'Orifginal NP2 {np2}')

np1[0] = 41

print(f'Changed NP1 {np1}')
print(f'Orifginal NP2 {np2}')