import pandas as pd
import numpy as np

#import csv file
my_df = pd.read_csv('akash.csv')
#print(my_df)

#Grab first 5 rows
print(my_df.head())

#Grab certain  number of rows
print(my_df.head(9))

#grab last 5 rows
print(my_df.tail())

#get info about data
print(my_df.info())

#Get shape of rows and columns
print(my_df.shape)

#Get dimension of data
print(my_df.ndim)

#get column datatypes
print(my_df.dtypes)

#Get some statistics about data
print(my_df.describe())

#Describe a specific column
print(my_df['Name'].describe())

#Select specific column using bracket
print(my_df['Age'])

#Select specific column using dot notation
print(my_df.Age)

#select specific column using location
print(my_df.iloc[:,0])