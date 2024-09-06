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
# Assignment: Lab Topic 4 Activity 2
# Date: 4-9-2024

a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: ")) #comment

if a < 0 and a != -1:
  pretty_a = f"- {abs(a)}x^2"
elif a < 0 and a == -1:
  pretty_a = "- x^2"
elif a == 1:
  pretty_a = "x^2"
elif a == 0:
    pretty_a = ""
else:
  pretty_a = f"{a}x^2"

if b < 0 and b != -1:
  pretty_b = f" - {abs(b)}x"
elif b < 0 and b == -1:
  pretty_b = " - x"
elif b == 1:
  if a == 0:
    pretty_b = "x"
  else:
    pretty_b = " + x"
elif b == 0:
    pretty_b = ""
else:
  if a == 0:
    pretty_b = f"{b}x"
  else:
    pretty_b = f" + {b}x"

if c < 0 and c != -1:
  pretty_c = f" - {abs(c)}"
elif c < 0 and c == -1:
  pretty_c = " - 1"
elif c == 1:
  pretty_c = " + 1"
elif c == 0:
    pretty_c = ""
else:
  pretty_c = f" + {c}"

print(f"The quadratic equation is {pretty_a}{pretty_b}{pretty_c} = 0")