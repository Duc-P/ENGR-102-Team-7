# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:
# Townsend Wheeler
# Duc Pham
# Julian Curry
# Archelaus Paxon
# Section: 518
# Assignment: Lab Topic 6 Activity 2
# Date: 16-9-2024

#import math for the exact ln value
from math import *

x = 0
ask = True

#Ask user for inputs of x value and tolerance
#Use while loop to ensure user puts in an x value between 0 exclusive and 2 inclusive

x = float(input("Enter a value for x: "))
if x > 2 or x <= 0: #if x is outside of 0 < x <= 2, keep asking
    ask = True
else:
    ask = False #else, keep x as is

while ask == True: #if x is outside of 0 < x <= 2, keep asking
    x = float(input("Out of range! Try again: "))
    if x > 0 and x <= 2:
        ask = False

tol = float(input("Enter the tolerance: "))
#Approximate ln(x) using taylor series expanison and a loop
check = 1
approximate = x - 1 #do the first step of the expansion before looping
n = 1
total_sum = 0.0
while abs(approximate) >= tol:
    total_sum += approximate
    n += 1
    approximate = ((-1) ** (n-1)) * (((x-1) ** n) / n)

#Get the exact ln of x
exact = log(x)

#print out the approximate, exact, and difference values
print(f"ln({x}) is approximately {total_sum}")
print(f"ln({x}) is exactly {exact}")
print(f"The difference is {abs(total_sum - exact)}")
