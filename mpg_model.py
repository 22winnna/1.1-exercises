#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = float(input("Please enter the length:\t\t"))
width = float(input("Please enter the width:\t"))

# calculate miles per gallon
area = length * width
area = round(area, 2)
perimeter = length + length + width + width
perimeter = round(perimeter, 2)           
# format and display the result
print()
print("Area:\t\t" + str(area))
print("Perimiter:\t\t" + str(perimeter))

print()
print("Thanks for using this program!")


