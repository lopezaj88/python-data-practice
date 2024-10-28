# -*- coding: utf-8 -*-

"""
BMI_Calculator.py- Calculates BMI using height and weight 
"""

__author__ = "Austin Lopez"
__version__ = "1.0"
__email__ = "lopezaj88@gmail.com"
__status__ = "Production"

# Basic formula
# BMI = (weight in pounds * 703) / (height in inches * height in inches)

# Import Modules

# Define Variables
name = input('Please enter your name: ')
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

# BMI Calculation
BMI = (weight * 703)/(height ** 2) 

if BMI > 0:
    if(BMI < 18.5):
        print(f'{name}, your BMI is {BMI}. You are underweight.')
    elif(BMI <= 24.9):
        print(f'{name}, your BMI is {BMI}. Your weight is normal.')
    elif(BMI < 34.9):
        print(f'{name}, your BMI is {BMI}. You are overweight.')
    elif(BMI < 39.9):
        print(f'{name}, your BMI is {BMI}. You are severely obese.')
    else:
        print(f'{name}, your BMI is {BMI}. You are morbidly obese.')


