import pandas as pd
import numpy as np
# Create Data
stuff = {
    'Corporation':['Apple', 'Google', 'Meta', 'Apple', 'Google','Meta'],
    'Employees':['John', 'April', 'Wes', 'Beth', 'Justin', 'Steph'],
    'Salary':[200, 220, 190, 130, 120, 150]}
# Create Dataframe
my_df = pd.DataFrame(stuff)
print(my_df)

#Create function
def times1000(x):
    return format(x * 1000,',d')

#use apply function
print(my_df['Salary'].apply(times1000))

#Append to current df
my_df['Salary'] = my_df['Salary'].apply(times1000)
print(my_df)

#function apply on multiple column
def namer(x):
    return 'codemy: '+x

#apply to columns
print(my_df[['Corporation','Employees']].apply(namer))

#append to current df
my_df[['Corporation','Employees']] = my_df[['Corporation','Employees']].apply(namer)
print(my_df)
