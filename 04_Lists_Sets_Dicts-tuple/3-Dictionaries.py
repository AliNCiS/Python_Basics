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
