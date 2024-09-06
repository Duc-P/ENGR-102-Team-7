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
# Assignment: Lab Topic 4 Activity 3
# Date: 6-9-2024

   
############ Part A ############

# create a, b, c (strings); ask for user input
# check and convert a, b, c to their boolean variants
# if a = "True" or "T" or "t" and NOT ("False" or "F" or "f")

# example:
a = input("Enter True or False for a: ")
a = (a == "True" or a == "T" or a == "t") and not(a == "False" or a == "F" or a == "f")
b = input("Enter True or False for b: ")
b = (b == "True" or b == "T" or b == "t") and not(b == "False" or b == "F" or b == "f")
c = input("Enter True or False for c: ")
c = (c == "True" or c == "T" or c == "t") and not(c == "False" or c == "F" or c == "f")


############ Part B ############

print(f"a and b and c: {(a and b and c)}")
print(f"a or b or c: {(a or b or c)}")

############ Part C ############

print(f"XOR: {((not a and b) or (not b and a))}")
print(f"Odd number: {((a and b and c) or (a and (not b) and (not c)) or (b and (not a) and (not c)) or (c and (not a) and (not b)))}")

# all three are true: (a and b and c)
# only a is true: (a and (not b) and (not c))
# only b is true: (b and (not a) and (not c))
# only c is true: (c and (not a) and (not b))
#Combined: ((a and b and c) or (a and (not b) and (not c)) or (b and (not a) and (not c)) or (c and (not a) and (not b)))

# evaluate all 4 cases above using <and> on ONE LINE OF CODE (probably inside the print statement; if one case fail, it should return False)

############ Part D ############

# notice how the parenthesis light up when you click on one of its pair

# (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
# (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

# ¯\_(ツ)_/¯ idk how to simplify these yet
