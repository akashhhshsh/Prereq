import pandas as pd
import numpy as np
#Create Dumny Data
stuff = {'A':[1,2,3],'B':[4,np.nan,6],'C':[7,8,9],'D':[10,11,12]}
my_df = pd.DataFrame(stuff)
print(my_df)

#Drop rows with null data
print(my_df.dropna())

#Drop column with null data
print(my_df.dropna(axis=1))

#drop more than 1 null value - set threshold
print(my_df.dropna(thresh=2,axis=1))  #thresh is minimum non null count for a row/column to be retained

#replace this with fillna
print(my_df.fillna(value=99))

#Use math function
print(my_df.fillna(value=my_df['B'].mean()))

#use min or max
print(my_df.fillna(value=my_df['B'].min()))
print(my_df.fillna(value=my_df['B'].max()))
 

