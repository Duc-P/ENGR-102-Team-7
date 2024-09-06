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
# Assignment: Lab Topic 4 Activity 1
# Date: 4-9-2024

from math import *

pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = pay - cost #finds the amount of change)
print(f"You received ${change:.2f} in change. That is...") #prints the amount of change
quarters = floor(change / 0.25) #divides change by 25 cents to get number of quarters
dimes = floor((change - (quarters * 0.25)) / 0.10) #subtracts change by the value of the quarters and divides change by 10 cents to get number of dimes
nickels = floor((change - (quarters * 0.25) - (dimes * 0.1)) / 0.05)#subtracts change by the value of the quarters and dimes and divides change by 5 cents to get number of nickels
pennies = round((change - (quarters * 0.25) - (dimes * 0.1) - (nickels * 0.05)) / 0.01, 0) #subtracts change by the value of the quarters, dimes, and nickels and divides change by 1 cent to get number of pennies

if quarters > 0: #Uses if statements so that the program doesn't print out 0 coins and only prints out the coins you'll get
  if quarters == 1:
    print(f"{quarters:.0f} quarter")
  else:
    print(f"{quarters:.0f} quarters")
if dimes > 0:
  if dimes == 1:
    print(f"{dimes:.0f} dime")
  else:
    print(f"{dimes:.0f} dimes")
if nickels > 0:
  if nickels == 1:
    print(f"{nickels:.0f} nickel")
  else:
    print(f"{nickels:.0f} nickels")
if pennies > 0:
  if pennies == 1:
    print(f"{pennies:.0f} penny")
  else:
    print(f"{pennies:.0f} pennies")