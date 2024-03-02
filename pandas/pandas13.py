import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data.csv')
print(my_df)

#Grab a specific column
print(my_df['DogName'])

#Count values
print(my_df['DogName'].value_counts())
#pass as dataframe
print(pd.DataFrame(my_df['DogName'].value_counts().head(50)))

#Grab Uniques
print(my_df['DogName'].unique())

#show as Dataframe
print(pd.DataFrame(my_df['DogName'].unique()))