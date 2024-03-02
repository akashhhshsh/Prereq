import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data.csv')
print(my_df)

#Conditional selection
# > < = >= <= etc
#Return Boolean
print(my_df=='BROWN')

#return dataframe with data
print(my_df[my_df== 'BROWN'])

#Run them on a column
print(my_df[my_df== 'BROWN']['Color'])

#Return multiple columns
print(my_df[my_df== 'BROWN'][['Color','Breed']])

