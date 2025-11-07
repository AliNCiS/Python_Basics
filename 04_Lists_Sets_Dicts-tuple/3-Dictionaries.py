# This repository was created by Ali Hajian as part of university coursework.
# Create dictionary
cart = {"apple": 100, "banana": 50}

# Add / edit
cart["orange"] = 80
cart["banana"] = 60

# Remove
del cart["apple"]

# Loop
for i,(name, price) in enumerate(cart.items() , start= 1):
    print(f"{i} Product: {name}, Price: {price}")

# Check key
if "orange" in cart:
    print("Orange is in cart")


# Dictionary Comprehension
# algorithm == {key_expression: value_expression for item in iterable if condition}

squares = {x: x**2 for x in range(5)}
print(squares)


# use if 
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

# change data
names = ["Ali", "Amir", "Ablfz"]
ages = [22, 19, 24]
students = {name: age for name, age in zip(names, ages)}
print(students)

#Re
students = {"Ali": 22, "Sara": 19, "Reza": 24}
reversed_dict = {v: k for k, v in students.items()}
print(reversed_dict)
