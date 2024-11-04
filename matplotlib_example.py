# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names:
# Townsend Wheeler
# Duc Pham
# Archelaus Paxon
# Julian Curry

# Section: 518
# Assignment: Lab 12 Activity 1
# Date: 4-11-2024

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

# Load matplotlib.pyplot, pandas, and numpy
import matplotlib.pyplot as plt
import numpy as np


# Create an equally spaced array with 100 elements from -2 to 2
x = np.linspace(-2, 2, num=100)

# Plot the graph for y = 1/4f * x^2, with f = 2
plt.plot(x, (x ** 2)/8, "b", label = "f=2", linewidth='2.0')

# Plot the graph for y = 1/4f * x^2, with f = 6
plt.plot(x, (x ** 2)/24, "r", label = "f=6", linewidth='6.0')


#PARABOLAS
#Add title and axes
plt.title("Parabola plots with varying length")
plt.legend()
plt.ylabel("Y Axis")
plt.xlabel("X Axis")
#Save the figure
plt.savefig('plot1.png')
plt.show()

#CUBIC FUNCTION
x = np.linspace(-4, 4, num=25)
#Plot cubic with stars and black outline around stars
plt.plot(x, 2*x**3 + 3*x**2 - 11*x - 6, "y*", markeredgecolor='black')
#Add title and axes
plt.title("Plot of cubic polynomial")
plt.ylabel("Y values")
plt.xlabel("X values")
#Save the figure
plt.savefig('plot2.png')
plt.show()

#SIN AND COS
# Create an equally spaced array with 100 elements from -2pi to 2pi
x = np.linspace(-2*np.pi, 2*np.pi, num=100)
#Create subplot for cos
plt.subplot(2, 1, 1)
plt.suptitle("Plot of cos(x) and sin(x)", fontsize=20, c='black')
plt.plot(x, np.cos(x), "r", label = "cos(x)")
#Add grid
plt.grid(axis='x')
plt.grid(linestyle='--')
plt.legend(loc = "lower right")
plt.ylabel("y = cos(x)")
#Create subplot for sin
plt.subplot(2, 1, 2)
plt.plot(x, np.sin(x), "b", label = "sin(x)")
#Add grid
plt.grid(axis='x')
plt.grid(linestyle='--')
plt.ylabel("y = sin(x)")
plt.legend()
plt.savefig('plot3.png')
plt.show()

#ADD GRID