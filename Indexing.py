# Manipulating files in pandas using their indexes

import pandas as pd

# Read in csv file, setting Country as its index
df = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/world_population.csv", index_col="Country")

# Reset index to integers, as before
#df.reset_index(inplace=True)
#print(df)

# Set index to Country, using set_index
df.set_index('Country', inplace = True)
print(df)

# Search for Albania in data frame
#df.loc['Albania']
#df.iloc[1]

#df.reset_index(inplace= True)

# Set multiple indexes
df.set_index(['Continent', 'Country'], inplace= True)
df.sort_index(ascending=True)
pd.set_option('display.max.rows', 235)

# Search for Angola
df.loc['Africa', 'Angola']
