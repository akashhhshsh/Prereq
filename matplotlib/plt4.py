import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(25,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#line plot
my_df.plot(kind = 'line')
plt.show()

#line plot abs
my_df.abs().plot(kind = 'line')
plt.show()

#line width
my_df.abs().plot(kind = 'line',lw=5)
plt.show()

#line single
my_df['Mon'].abs().plot(kind = 'line')
plt.show()

#more than one
my_df[['Mon','Thur']].abs().plot(kind = 'line')
plt.show()

#size
my_df[['Mon','Thur']].abs().plot(kind = 'line',figsize=(10,5)) #figsize works for all graphs; defaults is (6,8)
plt.show()

#second way
my_df.plot.line()
plt.show()