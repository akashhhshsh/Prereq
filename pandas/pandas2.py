import pandas as pd
import numpy as np
from numpy.random import randn

my_data = randn(4,3)  #rows,columns
my_rows= ['A', 'B','C','D']
my_cols= ['Monday', 'Tuesday','Friday']

#create dataframe
my_df = pd.DataFrame(my_data,my_rows,my_cols)
print(my_df)

my_df2 = pd.read_csv('akash.csv')
print(my_df2)

#pull out rows
print(my_df2.loc[0])   #row number 0

#pull out multiple rows
print(my_df2.loc[[1,5,9]])    #list of row numbers