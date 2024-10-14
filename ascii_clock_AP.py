# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Archelaus Paxon
# Section:      518
# Assignment:   Module 8 team lab (individual component)
# Date:         13-10-2024
#

### input ###
#time
time = input("Enter the time: ")
while ":" not in time: #Check if time has a colon
    time = input("Please enter a colon with the time! Enter the time: ")
time_list = time.split(":")
#Check if the hour is between 0 to 24
while int(time_list[0]) < 0 or int(time_list[0]) > 24:
    time = input("Please enter a valid time1! Enter the time: ")
    time_list = time.split(":")
#check if the minutes is between 0 - 60
while int(time_list[1]) < 0 or int(time_list[1]) > 60:
    time = input("Please enter a valid time2! Enter the time: ")
    time_list = time.split(":")
#Check if first half of time has 1 or 2 digits
while len(time_list[0]) not in [1,2]:
    time = input("Please enter a valid time3! Enter the time: ")
    time_list = time.split(":")
#Check if second half of time has 2 digits
while len(time_list[1]) != 2:
    time = input("Please enter a valid time4! Enter the time: ")
    time_list = time.split(":")
#Store the hour and minutes separately
hour = time_list[0]
minutes = time_list[1]
