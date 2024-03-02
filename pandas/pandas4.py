import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data.csv')
#print(my_df)

#count distinct values -Descending
print(my_df['Color'].value_counts())

#count distinct values -Ascending
print(my_df['Color'].value_counts(ascending=True))

#Dog names - Without NaN
print(my_df['DogName'].value_counts())

#Dog names - Without NaN
print(my_df['DogName'].value_counts(dropna=False))

#Get relative frequency -Percentage
print(my_df['Color'].value_counts(normalize=True)*100)

#Get specific item count
print(my_df['Color'].value_counts()['WHITE'])  #Count of white Dogs

#Count unique values - Size
print(my_df.groupby('Color').size())

#Count unique values - count
print(my_df.groupby('Color').count())

#get a count of all columns across all columns
print(my_df.apply(pd.value_counts()))