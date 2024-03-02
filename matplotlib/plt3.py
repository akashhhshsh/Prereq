import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(25,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#bar plot
my_df.abs().plot(kind = 'bar',figsize= (10,6))
plt.show()

#bar plot stacked
my_df.abs().plot(kind = 'bar',stacked = True)
plt.show()

#shading
my_df.abs().plot(kind = 'bar',stacked = True,alpha=0.4)
plt.show()

#Title
my_df.abs().plot(kind = 'bar',stacked = True,alpha=0.4,title= "Absolute Values",legend=False)
plt.show()

#second way
my_df.abs().plot.bar()
plt.show()

#second way stacked,shading,title,legend
my_df.abs().plot.bar(stacked=True,alpha=0.4,title='awesome plot',legend=False)
plt.show()


