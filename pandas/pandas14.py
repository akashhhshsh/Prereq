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

#Make into Data frame
print(pd.DataFrame(my_df['Salary'].apply(times1000)))

#Add elder last name
def namer(x):
    if x == 'John':
        return 'John Elder'
    else:
        return x
#Show elder last names
print(my_df['Employees'].apply(namer))

#use lambda
print(pd.DataFrame(my_df['Salary'].apply(lambda x: format (x*1000,',d'))))\
    
