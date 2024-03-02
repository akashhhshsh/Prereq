import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn


#create a new df
my_df = pd.DataFrame(randn(500,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#Density and kernel density plot
my_df.abs().plot(kind='kde')
plt.show()

#other way
my_df.plot.kde()
plt.show()

#density plot
my_df.abs().plot(kind='density')
plt.show()

#other way
my_df.plot.density()
plt.show()