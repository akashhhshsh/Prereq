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

#Group by corporation - To get location in memory
company=my_df.drop('Employees',axis=1).groupby('Corporation')
print(company)

#sum
print(company.sum())

#mean
print(company.mean())

# max min
print(company.max())

#Standard deviation
print(company.std())

#variance
print(company.var())

#count
print(company.count())

#describe
print(company.describe())