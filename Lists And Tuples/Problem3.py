# Check that a tuple type cannot be changed in python.

# Tuples are immutable, so their type cannot be changed after creation.
t = (1, 2, 3)
print(type(t))
# t[0] = 4 # This would raise an error because tuples are immutable.
print(t)