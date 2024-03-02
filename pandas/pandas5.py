import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data_short.csv')
#print(my_df)

#Add column from list
gender = ['Male','Female','Male','Male','Female']
my_df['Gender'] = gender
print(my_df)

#Add default values
my_df['Alive/Dead'] = [True]*len(my_df)
print(my_df)

#Add NaN values
my_df['Show dog'] = [np.nan]*len(my_df)
print(my_df)

#add column with .insert() - allows position
my_df.insert(1,'Adopted',[True]*len(my_df),True)
print(my_df)

#add column with .assign() - creates new df
my_df2 = my_df.assign(Horse=[False]*len(my_df))
print(my_df2)
