# -*- coding: utf-8 -*-

"""
web_scraping_project.py- Scrapes data from a website 
"""

__author__ = "Austin Lopez"
__version__ = "1.5"
__email__ = "lopezaj88@gmail.com"
__status__ = "Production"

# Import modules
from bs4 import BeautifulSoup
import requests
import pandas as pd  

# Define Variables
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

# Search the html to extract world titles
table = soup.find_all('table')[0]
worldTitles = table.find_all('th')

# Strip out the excess
worldTabletitles = [title.text.strip() for title in worldTitles]

# Create a data frame using the stripped values as column titles 
dataFrame = pd.DataFrame(columns = worldTabletitles)

# Grab row data from html
columnData = table.find_all('tr')
for row in columnData[1:]:
    rowData = row.find_all('td')
    individualRowdata = [data.text.strip() for data in rowData]
    length = len(dataFrame)
    dataFrame.loc[length] = individualRowdata

# Export data frame to csv
dataFrame.to_csv(r'C:\Users\LopezA-5651\Documents\Python_Data_Practice\Companies.csv', index = False)


