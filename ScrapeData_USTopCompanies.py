# Scrape data from wikipedia website and input into data frame

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup)

# Select the target table on website
table = soup.find_all('table')[0]

# Get headers from table
world_titles = table.find_all('th')
#print(world_titles)

# Loop through titles with 'th' tags to get titles as text
world_table_titles = [title.text.strip() for title in world_titles]
#print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)
#print(df)

# Find all row data
column_data = table.find_all('tr')

# Collect and print out data for each row, company
# [1:] skips first index which is empty, in this case
for row in column_data[1:]:
    row_data = row.find_all('td')
    single_row_data = [data.text.strip() for data in row_data]
    #print(single_row_data)
    
    # Assigns length of df, currently empty
    length = len(df)
    
    # Append each row of row_data into data frame, df
    df.loc[length] = single_row_data

# Print out updated data frame
#print(df)

# Read data frame into new csv file
df.to_csv(r"C:/Users/chike/OneDrive - University of Birmingham/Documents/C0de/DA Bootcamp Py/DA-Bootcamp-Py-/Companies.csv", index = False)