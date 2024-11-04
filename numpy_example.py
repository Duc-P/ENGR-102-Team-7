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

#import numpy for matrix manipulation
import numpy as np

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]) #3x4 matrix
b = np.array([[0, 1], [2, 3], [4, 5], [6, 7]]) #4x2 matrix
c = np.array([[0, 1, 2], [3, 4, 5]]) #2x3 matrix

#print matrices a,b,c, and format similar to pdf
print(f"A = {a}\n")
print(f"B = {b}\n")
print(f"C = {c}\n")

#Do matrix multiplication for abc, assign to d and print
d = a @ b @ c
print(f"D = {d}\n")

#Transpose matrix d and print
d_t = d.transpose()	
print(f"D^T = {d_t}\n")

#Calculate sqrt(d), divide by 2, assign to e and print matrix e
e_matrix = np.sqrt(d) / 2
print(f"E = {e_matrix}")