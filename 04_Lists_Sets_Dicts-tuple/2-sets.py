# This repository was created by Ali Hajian as part of university coursework.
# Create sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Add/remove
A.add(10)
A.remove(2)

# Operations
print(A | B)  # Union
print(A & B)  # Intersection
print(A - B)  # Difference
print(A ^ B)  # Symmetric Difference

# Check membership
print(3 in A)  # True
