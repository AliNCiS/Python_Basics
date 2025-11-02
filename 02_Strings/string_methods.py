# This repository was created by Ali Hajian as part of university coursework.
# Strings, Slicing, and Formatting

text = "Hello Python World"

# Access characters
print(text[0])    # H
print(text[-1])   # d

# Slicing
print(text[0:5])  # Hello
print(text[6:12]) # Python
print(text[::2]) # HloPto ol

# String methods
print(text.upper())
print(text.lower())
print(text.replace("Python", "Programming"))
print(text.split())

# f-string formatting
name = "Ali"
age = 22
print(f"My name is {name} and I am {age} years old.")
