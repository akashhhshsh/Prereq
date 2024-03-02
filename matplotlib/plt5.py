import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(500,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#scatter plot
my_df.plot(kind='scatter',x='Mon',y='Tue')
plt.show()

#3 variable
my_df.plot(kind='scatter',x='Mon',y='Tue',c='Wed')
plt.show()

#colours
my_df.plot(kind='scatter',x='Mon',y='Tue',c='Wed',cmap='magma') #new colours on matplotlib cmap website
plt.show()

#by size
my_df.plot(kind='scatter',x='Mon',y='Tue',s='Wed') 
plt.show()

#edit size my multiplying
my_df.plot(kind='scatter',x='Mon',y='Tue',s=my_df['Wed']*50) 
plt.show()

#By size easier to read with alpha 
my_df.plot(kind='scatter',x='Mon',y='Tue',s=my_df['Wed']*50,alpha=0.3) 
plt.show()