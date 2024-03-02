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

#sort salaries from lowest to highest
print(my_df.sort_values('Salary'))

#sort salaries from highest to lowest
print(my_df.sort_values('Salary',ascending=False))

#not permanent without inplace
print(my_df.sort_values('Salary',inplace=True))
print(my_df)

#sort df alphabetically
print(my_df.sort_values('Corporation'))
#sort df alphabetically descending
print(my_df.sort_values('Corporation',ascending=False))