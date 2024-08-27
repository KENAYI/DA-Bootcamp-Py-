# Reading files different file types into Pandas data frame

import pandas as pd

# Read csv file into pandas data frame
df = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/countries of the world.csv")

#print(df)

# Read txt file into pandas data frame
df1 = pd.read_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/countries of the world.txt", sep="\t")
df1 = pd.read_table(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/countries of the world.txt")
print(df1)

# Read in json file to pandas data frame
df2 = pd.read_json(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/json_sample.json")
pd.set_option("display.max.columns", 40)
print(df2)

# Read in excel file to pandas data frame
df3 = pd.read_excel(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/Pandas Tutorial/world_population_excel_workbook.xlsx", sheet_name= 'Sheet1')
pd.set_option("display.max.rows", 235)
print(df3)

# Returns important details on data frame
#df3.info()

# Returns number of rows and columns
#print(df3.shape)

#  Returns first 5 rows within data frame
# print(df3.head())
#print(df3.head(10))

# Returns last 5 rows within data frame
# print(df3.tail())
#print(df3.tail(10))

# Returns data from given column, and it's index
#print(df3['CCA3'])

# Returns data for given index
# print(df3.loc[224])
# print(df3.iloc[224])