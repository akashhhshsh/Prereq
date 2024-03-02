import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(500,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#Hexplot
my_df.plot(kind='hexbin',x='Mon',y='Tue',gridsize=20,cmap='Greens')
plt.show()

#other method
my_df.plot.hexbin(x='Mon',y='Tue',C='Wed',gridsize=10)
plt.show()