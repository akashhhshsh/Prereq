import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(500,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#box plot
my_df.plot(kind='box')
plt.show()

#other way
my_df.plot.box()
plt.show()  #to keep the window