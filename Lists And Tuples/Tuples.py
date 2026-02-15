# Tuples are similar to lists but are immutable, meaning their values cannot be changed after creation. They are defined using parentheses ().

a = () # this is an empty tuple.
print(a)

a = (1) # this is not a tuple, it is just an integer.
print(type(a))

a = (1,) # this is a tuple with one item. the comma is necessary to indicate that it is a tuple.
print(type(a))

friends = ("aman","sahil",45, 34.20,True,"aman") # It allows duplicate members. It contains items of different data types.
print(type(friends)) # to check the type of the variable.
print(friends)

print(friends[0]) # to access the first item in the tuple

# friends[1] = "apple" # This will raise an error because tuples are immutable

print(friends[1:4]) # to access a range of items in the tuple.
print(friends)

# Tuples do not support methods like append, insert, remove, pop, sort, reverse because they are immutable.

# Counting occurrences of an item in a tuple
count = friends.count("aman")
print(count)

# Finding the index of an item in a tuple
index = friends.index("sahil")
print(index)

print(friends*2) # to repeat the items in the tuple.

print(len(friends)) # to find the length of the tuple.

print("sahil" in friends) # to check if an item is in the tuple.

print("apple" not in friends) # to check if an item is not in the tuple.

print(friends + a) # to concatenate two tuples.

print(friends+("banana",)) # to concatenate a tuple with a single item.

friends1= (45, 34,12,7)
print(min(friends1)) # to find the minimum item in the tuple.

print(max(friends1)) # to find the maximum item in the tuple.

a,b,c,d = friends1 # to unpack the items in the tuple into separate variables.
print(a , b, c, d)
