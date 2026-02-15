 # list is a collection of items which are ordered and changeable. It allows duplicate members. It contains items of different data types. It is defined by using square brackets []. Lists are mutable, which means that we can change the values of the items in the list after it has been created.

friends = ["aman","sahil",45, 34.20,True,"priya"]
print(friends)

print(friends[0]) # to access the first item in the list

friends[1] = "apple" # to change the value of the second item in the list
print(friends[1])

print(friends[1:4]) # to access a range of items in the list.
print(friends)

friends.append("banana") # to add an item to the end of the list
print(friends)

friends.insert(3, "Blue") # to add an item at a specific position in the list.
print(friends)

friends.remove(45) # to remove an item from the list.
print(friends)

friends.pop() # to remove the last item from the list.
print(friends)

friends.pop(2) # to remove an item at a specific position in the list.
print(friends.pop(2))
print(friends)

li = [45, 34.20, 12, 98, 76]
li.sort() # to sort the items in the list in ascending order.
print(li)

li.sort(reverse=True) # to sort the items in the list in descending order.
print(li)

li.reverse() # to reverse the order of the items in the list.
print(li)