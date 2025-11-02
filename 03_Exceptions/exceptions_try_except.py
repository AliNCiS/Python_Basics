# This repository was created by Ali Hajian as part of university coursework.
# Exception Handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Your number is {num} and result is {result}")
finally:
    print("This runs no matter what.")

# Raising your own exception
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
