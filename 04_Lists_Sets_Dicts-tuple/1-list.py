# This repository was created by Ali Hajian as part of university coursework.
# Create a list
fruits = ["apple", "banana", "orange"]

# Access elements
print(fruits[0])   # apple
print(fruits[-1])  # orange

# Slicing
print(fruits[0:2]) # ['apple', 'banana']

# Add elements
fruits.append("grape")       # Add at end
fruits.insert(1, "kiwi")     # Add at index
fruits.extend(["melon", "pear"])  # Add multiple elements

# Remove elements
fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove last element, returns it
fruits.clear()               # Remove all elements

# Sort & reverse
numbers = [5, 2, 9, 1]
numbers.sort()               # Sort ascending
numbers.sort(reverse=True)   # Sort descending
numbers.reverse()            # Reverse the list

# Loop
for fruit in fruits:
    print(fruit)

# Enumerate
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# List comprehension
squared = [x**2 for x in range(1, 6)]
print(squared)  # [1,4,9,16,25]
