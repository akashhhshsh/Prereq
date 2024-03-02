import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data.csv')
print(my_df)

#Multiple conditional AND
print(my_df[(my_df['Color'] == 'BROWN') & (my_df['Breed'] == 'MIXED')])

#Get length
print(len(my_df[(my_df['Color'] == 'BROWN') & (my_df['Breed'] == 'MIXED')]))

#Multiple Conditional OR
print(my_df[(my_df['Color'] == 'BROWN') | (my_df['Breed'] == 'MIXED')])

#Get length
print(len(my_df[(my_df['Color'] == 'BROWN') | (my_df['Breed'] == 'MIXED')]))

#Return Specific row
print(my_df[(my_df['Color'] == 'BROWN') & (my_df['Breed'] == 'MIXED')]['DogName'])
