# -*- coding: utf-8 -*-

"""
exploratory_data_analysis.py- EDA project on practice data 
"""

__author__ = "Austin Lopez"
__version__ = "2.7"
__email__ = "lopezaj88@gmail.com"
__status__ = "Production"

# Import Modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

# Define variables
fP = r"C:\Users\LopezA-5651\Documents\Python_Data_Practice\pandas_practice_data\world_population.csv"
dF = pd.read_csv(fP)
dF

# Set display format out to two decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)
dF

# Show basic info of the data
dF.info()

# Get basic statistics of the data
dF.describe()

# Get a sum of the null values in each column
dF.isnull().sum()

# Number of unique values in each column
dF.nunique()

# Sort the data by the World Population Percentage, in descending order, and only show the top 10
dF.sort_values(by = "World Population Percentage", ascending = False).head(10)

# Find correlations between numeric data
dF.corr(numeric_only= True)

# Plot a heatmap showing the correlations
sns.heatmap(dF.corr(numeric_only = True), annot = True)
plt.rcParams['figure.figsize'] = (30,7)
plt.show()

# Create a new data frame that only focuses on the population by continent, and has the columns sorted from oldest to newest data
dF2 = dF.groupby('Continent')[dF.columns[12:4:-1]].mean(numeric_only= True).sort_values(by = "2022 Population", ascending= False)

# Pull the columns of the dF data frame
dF.columns

# Make a new data frame where the columns from dF2 become the rows for dF3 and the rows from dF2 become the columns for dF3
dF3 = dF2.transpose()

# Plot the data to see how the population of the continents has changed over time
dF3.plot()

# Create a box plot of the populations of each year to see the distribution and outliers
dF.boxplot(figsize=(20,10))

# Only showing data types within the data that are numbers
dF.select_dtypes(include='number')


