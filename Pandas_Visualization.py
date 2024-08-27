# Create visualizations using Pandas lib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/Ice Cream Ratings.csv")
pd.set_option('display.max.columns', 3)
df = df.set_index('Date')
#print(df)

# Plots multiple different line graphs
df.plot(kind= 'line', subplots= True)

# Plots a line graph
df.plot(kind= 'line', title= 'Ice Cream Ratings', xlabel= 'Daily Ratings', ylabel= 'Scores')

# Plots a stacked vertical bar chart
df.plot(kind= 'bar', stacked= True) 

# Plots a vertical bar chart, for one given column
df['Flavor Rating'].plot(kind= 'bar', stacked= True)

# PLots a stacked horizontal bar chart
df.plot.barh(stacked= True)

# Plots a scattered chart
df.plot.scatter(x= 'Texture Rating', y= 'Overall Rating', s = 200, c= 'Green')

# Plots a histogram chart
df.plot.hist(bins= 10)

# PLots a box plot graph
df.boxplot()

# Plots an area chart
df.plot.area(figsize= (10,5))

# Plot a pie chart
df.plot.pie(y= 'Flavor Rating', figsize=(10,6))

# To find various styling options for visualizations
# print(plt.style.available)
# plt.style.use(' ')