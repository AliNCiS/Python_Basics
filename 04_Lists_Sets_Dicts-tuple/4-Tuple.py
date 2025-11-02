# This repository was created by Ali Hajian as part of university coursework.
# Tuple creation
t1 = (1, 2, 3)
t2 = ("apple", 5, True)
t3 = 1, 2, 3
t4 = (5,)  # Single element tuple

# Access
print(t1[0])      # 1
print(t1[-1])     # 3
print(t1[0:2])    # (1,2)

# Operations
print(t1 + t3)    # Concatenation
print(t1 * 2)     # Repetition
print(len(t1))    # Length
print(2 in t1)    # Membership check

# Tuple is immutable
# t1[0] = 10  # Error!
