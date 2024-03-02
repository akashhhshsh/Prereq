import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(100,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#Histogram
(my_df['Wed'].hist())
plt.show()

#histogram with smaller bin
(my_df['Wed'].hist(bins=50))
plt.show()

#histogram without grid bars
(my_df['Wed'].plot(kind='hist'))
plt.show()

(my_df['Wed'].hist(bins=20,grid=False))
plt.show()