import pandas as pd
import numpy as np

print(pd. __version__)
my_series = [5,9,12,27]
my_var1 = pd.Series(my_series)
print(my_var1)

#print specific value
print(my_var1[2])

#Labels using the index argument
my_index = ['A','B','C','D']
my_var2 = pd.Series(my_series , my_index)
print(my_var2)

print(my_var2["B"])

#Key value dictionary
cars = {'Tesla':12,'Mercedes':59,'BMW':45}
my_var3 = pd.Series(cars)
print(my_var3)