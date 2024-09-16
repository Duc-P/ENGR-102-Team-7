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

#Calculates the surface area for all four sides of the pyramid
#Uses (n * (n+1))/2 to get the total number of layers, multiplied by four to get it for all 4 sides, multiplied by square of side length to get total side surface area
side_area = (((layers * (layers+1))/2)*4 * side_length**2)
answer = top_area + side_area
print(f"You need {answer:.2f} m^2 of gold foil to cover the pyramid")