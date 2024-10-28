# -*- coding: utf-8 -*-

"""
automatic_file_sorter.py- Automatically sorts file in Windows File Explorer 
"""

__author__ = "Austin Lopez"
__version__ = "2.2"
__email__ = "lopezaj88@gmail.com"
__status__ = "Production"

# Import Modules
import os
import shutil

# Define Variables
path =r''
folderNames = ['csv files', 'image files', 'text files']
fileName = os.listdir(path)

for loop in range(0,3):
    if not os.path.exists(path + folderNames[loop]):
        os.makedirs(path + folderNames[loop])

for file in fileName:
    if '.csv' in file and not os.path.exits(path + 'csv files/' + file):
        shutil.move(path +file, path + 'csv files/' + file)
    elif '.png' in file and not os.path.exits(path + 'image files/' + file):
        shutil.move(path +file, path + 'image files/' + file)
    if '.txt' in file and not os.path.exits(path + 'text files/' + file):
        shutil.move(path +file, path + 'text files/' + file)
    else:
        print('There are files in this path that were not moved!')
        
        



