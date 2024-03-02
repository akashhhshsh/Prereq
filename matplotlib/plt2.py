import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

#create a new df
my_df = pd.DataFrame(randn(25,4), columns = ['Mon','Tue','Wed','Thur'])
print(my_df)

#area plot
my_df.plot(kind = 'area',stacked = False) #stack allowes negative and positive values to not get stacked
my_df.abs().plot(kind = 'area') #makes all negative value positive
plt.show()

#shading
my_df.abs().plot(kind = 'area',alpha = 0.3) #alpha is used ro set transparency of the graph 
#lower the alpha  number, more transparent it will be
plt.show()

#title 
my_df.abs().plot(kind = 'area',alpha = 0.3,title = "my awesome plot")
plt.show()

#legend
my_df.abs().plot(kind = 'area',alpha = 0.3,title = "my awesome plot",legend=False)  #turns off the legend
plt.show()

#sjow only one column
my_df['Mon'].abs().plot(kind = 'area',alpha = 0.3,title = "my awesome plot")
plt.show()

my_df[['Mon','Thur']].abs().plot(kind = 'area',alpha = 0.3,title = "my awesome plot")
plt.show()

#add table
my_df.abs().plot(kind = 'area',alpha = 0.3,title = "my awesome plot",table=True)
plt.show()
