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


#Set Comprehension

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers}
print(unique_squares)

# if
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)

#Text Checke
text = "programming"
unique_chars = {ch for ch in text if ch not in 'aeiou'}
print(unique_chars)
