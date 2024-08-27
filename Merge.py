# Merge, Join, Concatenate

import pandas as pd

df1 = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/LOTR.csv")
print(df1)

df2 = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/LOTR 2.csv")
print(df2)

# Inner Join
df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName'])

# Outer Join
df1.merge(df2, how = 'outer')

# Left Join
df1.merge(df2, how = 'left')

# Right Join
df1.merge(df2, how = 'right')

# Cross Join
df1.merge(df2, how = 'cross')

# Join function
df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix = '_Right')

# Join with index set as FellowshipID
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix= '_Left', rsuffix= '_Right', how = 'outer')
print(df4)

# Concatenation
pd.concat([df1, df2])
pd.concat([df1, df2], join= 'inner')
pd.concat([df1, df2], join= 'outer', axis= 1)