'''
There are several ways to calculate the area of a regular polygon. 
Given the number of sides, n, and the length of each side, s, the polygon's area is

(n * s^2) / 4 * tan(pi/n)

For example, a regular polygon with 5 sides, each of length 7 inches, has area 84.30339262885938 square inches.

Write a function that calculates the area of a regular polygon, given the number of sides and 
length of each side. Submit the area of a regular polygon with 7 sides each of length 3 inches. 
Enter a number (and not the units) with at least four digits of precision after the decimal point.
'''

import math
def area(n, s):
    area = n*s*s / (4 * math.tan(math.pi/n))
    print area
    return area

area(5, 7)
area(7, 3)