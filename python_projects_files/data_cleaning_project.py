# -*- coding: utf-8 -*-

"""
BMI_Calculator.py- Calculates BMI using height and weight 
"""

__author__ = "Austin Lopez"
__version__ = "2.0"
__email__ = "lopezaj88@gmail.com"
__status__ = "Production"

# Import modules
import pandas as pd 

# Define variables
fP = r"C:\Users\LopezA-5651\Documents\Python_Data_Practice\pandas_practice_data\Customer Call List.xlsx"
dF = pd.read_excel(fP)

# Drop Duplicates
dF = dF.drop_duplicates()

# Drop 'Not_Useful_Column'
dF = dF.drop(columns = 'Not_Useful_Column')

# Clean up last names so they are all standardized
dF['Last_Name'] = dF['Last_Name'].str.lstrip('...')
dF['Last_Name'] = dF['Last_Name'].str.lstrip('/')
dF['Last_Name'] = dF['Last_Name'].str.rstrip('_')
#dF['Last_Name'] = dF['Last_Name'].str.strip('123._/') -- This also works, all the characters have to be in as a single value because strip works via RegEx

# Clean up phone numbers so they are all standardized
dF["Phone_Number"] = dF["Phone_Number"].str.replace('[^a-zA-Z0-9]', '', regex = True)
dF["Phone_Number"] = dF["Phone_Number"].apply(lambda x: str(x))
dF["Phone_Number"] =  dF["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

# Make cells with no phone number blank
dF["Phone_Number"] = dF["Phone_Number"].str.replace('nan--', '')
dF["Phone_Number"] = dF["Phone_Number"].str.replace('Na--', '')

# Expand the address column into separate columns
dF[["Street_Address", "State", "Zip_Code"]] = dF["Address"].str.split(',', n = 2, expand = True)

# Standardize 'Paying Customer' column
dF["Paying Customer"] = dF["Paying Customer"].str.replace('Yes', 'Y')
dF["Paying Customer"] = dF["Paying Customer"].str.replace('No', 'N')

# Standardize 'Do_Not_Contact' column
dF["Do_Not_Contact"] = dF["Do_Not_Contact"].str.replace('Yes', 'Y')
dF["Do_Not_Contact"] = dF["Do_Not_Contact"].str.replace('No', 'N')

# Replace N/a with empty space
dF = dF.replace('N/a', '')
dF = dF.fillna('')

# Drop any rows where Do not Contact is Yes
for x in dF.index:
    if dF.loc[x, "Do_Not_Contact"] == 'Y':
        dF.drop(x, inplace = True)

# Drop rows without phone numbers
for x in dF.index:
    if dF.loc[x, "Phone_Number"] == '':
        dF.drop(x, inplace = True)

# Another way to drop null values
# dF = dF.dropna(subset = "Phone_Number", inplace = True)

# Resetting the index for readability
dF = dF.reset_index(drop = True)
dF


