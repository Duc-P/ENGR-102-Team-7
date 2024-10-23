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
# Assignment: lab Topic 10
# Date: 23-10-2024

def no_three_in_line(n):
    points = []
    
    # Generate points while ensuring no three are collinear
    for x in range(n):
        for y in range(n):
            # Check if we can add the point (x, y)
            if can_add_point(points, (x, y)):
                points.append((x, y))
    
    return points

def can_add_point(points, new_point):
    """Check if adding new_point would result in three collinear points."""
    x1, y1 = new_point
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x2, y2 = points[i]
            x3, y3 = points[j]
            if are_collinear((x1, y1), (x2, y2), (x3, y3)):
                return False
    return True

def are_collinear(p1, p2, p3):
    """Check if points p1, p2, p3 are collinear using area of triangle formula."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)

# Example usage
print(no_three_in_line(3))
