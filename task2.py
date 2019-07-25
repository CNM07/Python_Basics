#Implement a function that takes as input three variables, and returns the largest of the three.

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c

print(largest(10, 10, 20))

