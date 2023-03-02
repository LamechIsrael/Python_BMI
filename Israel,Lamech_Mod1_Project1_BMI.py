######################################
# CS 1110A - Programming in Python   #
# Module 1 - Project 1 - BMI         #
# Author: Lamech Israel              #
# Date:   01/11/2022                 #
######################################


print('Calculate Body Mass Index (BMI)')

# Input

weight = int(input('\nWhat is your weight in pounds? '))
height = int(input('What is your height in inches? '))

# Processing

weight_in_kg = weight / 2.2
height_in_meters = height * 0.0254

bmi = weight_in_kg / height_in_meters**2

# Output

print('\nAt a weight of', weight ,'pounds and a height of', height ,'inches, your BMI is', round(bmi,1))

print('\nDone')