# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Julian Curry
# Section:      518
# Assignment:   Module 8 team lab (individual component)
# Date:         13-10-2024
#

#format
clock_type = input("Choose the clock type (12 or 24): ")
while clock_type not in ["12", "24"]:
    clock_type = input("Time type not permitted! Try again: ")

#character # Duc modified #
allowed_chars = "abcdeghkmnopqrsuvwxyz@$&*="
fav_char = input("Enter your preferred character: ")
if fav_char == "": # turn into numerical ascii value
    print()
else:
    while fav_char not in allowed_chars or len(fav_char) != 1:
        fav_char = input("Character not permitted! Try again: ")
    print()
    
# make all the number into the char value
if fav_char != "":
    for i in range(10): #0 to 9 inclusive
        mat_clock[i] = char_convert(mat_clock[i], fav_char, str(i))
