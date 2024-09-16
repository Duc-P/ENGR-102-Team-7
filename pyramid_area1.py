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
# Assignment: Lab Topic 6 Activity 1
# Date: 16-9-2024

#Asks the user for the side length and number of layers
side_length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

#calculates the surface area of the pyramid as viewed from its top
top_area = ((layers*side_length)**2)

#Calculates the surface area for one side of the pyramid
side_area = 0
for i in range(1, layers + 1):
    side_area += side_length * side_length * i
    i += 1

#Multiply side area by four to get surface area for all 4 sides of the pyramid
side_area *= 4

#Add together the top and side areas to get total surface area
answer = top_area + side_area
print(f"You need {answer:.2f} m^2 of gold foil to cover the pyramid")