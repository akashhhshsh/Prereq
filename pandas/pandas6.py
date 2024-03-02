import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data_short.csv')
#print(my_df)

#Add column from list
gender = ['Male','Female','Male','Male','Female']
my_df['Gender'] = gender
print(my_df)

#Remove columns
print(my_df.drop('Gender',axis=1))
print(my_df)
#to delete it permanently
print(my_df.drop('Gender',axis=1,inplace=True))
print(my_df)

#Remove row
print(my_df.drop(3))
print(my_df)