import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('dog_data_short.csv')
#print(my_df)

#Create new column
my_df['Frame Header'] = ['Dog1','Dog2','Dog3','Dog4','Dog5']
print(my_df)

#set index
print(my_df.set_index("Frame Header",inplace = True)) #do inplace = True for permanent
print(my_df)

#reset index
print(my_df.reset_index(inplace=True))
print(my_df)

#drop the column
my_df.drop('Frame Header',axis=1,inplace=True)
print(my_df)