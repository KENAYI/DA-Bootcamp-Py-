# Find and fetch matching items in given case

from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
#print(soup)

#soup.find_all('p')
# paragraph = soup.find('p', class_ = 'lead').text.strip()
# print(paragraph)

#print(soup.find_all('td'))
print(soup.find('th').text.strip())