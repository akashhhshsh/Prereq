import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data_short.csv')
print(my_df)

#Grab row method 1 location
print(my_df.loc[2])

#Grab row method 2 index location
print(my_df.iloc[3])

#Specific points (row and column)
#my_df.loc['Row','Column']
print(my_df.loc[1,'DogName'])

#subsets
#my_df.loc[['Row','row'],['column','column']]
print(my_df.loc[[1,3],['DogName','Breed','Color']])

