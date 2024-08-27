# Filtering and Ordering files in pandas

import pandas as pd

df = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/world_population.csv")

# Return rows for countries ranked top 10
top_10 = df[df['Rank'] >= 10]
print(top_10)

# Filters and return rows for given countries
specific_countries = ['Bangladesh', 'Brazil']
print(df[df['Country'].isin(specific_countries)])

# Filters and returns rows containing given keyword in a column
print(df[df['Country'].str.contains('United')])

# Set countries as index 
df2 = df.set_index('Country')
print(df2)

# Search for given items in Columns, 1
df2.filter(items= ['Continent', 'CCA3'], axis = 1)

# Search for country in index, 0
df2.filter(items= ['Zimbabwe'], axis= 0)
df2.filter(like= 'United', axis= 0)

# Location or Integer Location to filter out  search
print(df2.loc['United'])
print(df2.iloc[200])

# Order table by one column, ascending
df[df['Rank'] <= 10].sort_values(by = 'Rank', ascending= True)

# Order table by multiple columns, both ascending and descending
df[df['Rank'] <= 10].sort_values(by= ['Continent', 'Country'], ascending= [False, True])