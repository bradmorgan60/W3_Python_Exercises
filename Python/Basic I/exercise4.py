'''
4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504

area of a circle = pi * r ^2
'''
from math import pi

r = 1.1

radius = float(input("Enter the radius of the circle: "))
area = pi * radius ** 2


# print("Area with radius " + str(radius) + " is: " + str(area))
print("Radius:", str(radius))
print("Area: ", str(area))


# print(area(pi, radius))