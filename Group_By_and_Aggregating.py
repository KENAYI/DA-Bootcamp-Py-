# Group by function and Aggregating within pandas

import pandas as pd

df = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/Flavors.csv")
#print(df)

# Group By Function

# group_by_frame = df.groupby('Base Flavor')
# pd.set_option('display.max.rows', 2)
# print(group_by_frame.mean())

#OR

# group_by_frame_mean = df.groupby('Base Flavor').mean()
# print(group_by_frame_mean)

# group_by_frame_count = df.groupby('Base Flavor').count()
# print(group_by_frame_count)

# group_by_frame_min = df.groupby('Base Flavor').min()
# print(group_by_frame_min)

# group_by_frame_max = df.groupby('Base Flavor').max()
# print(group_by_frame_max)

# group_by_frame_sum = df.groupby('Base Flavor').sum()
# print(group_by_frame_sum)

# Using aggregate function
group_by_frame_agg = df.groupby('Base Flavor').agg({'Flavor Rating': ['mean', 'max', 'count', 'sum'], 'Texture Rating': ['mean', 'max', 'count', 'sum']})
pd.set_option('display.max.columns', 8)
print(group_by_frame_agg)

# Group by multiple columns
df.groupby(['Base Flavor','Liked']).mean()

df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating': ['mean', 'max', 'count', 'sum']})

# describe() function gives an overview of different aggregations
df.groupby('Base Flavor').describe()