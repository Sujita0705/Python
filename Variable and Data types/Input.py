a = input("Enter a value: ")
# a = int(input("Enter a value: ")) we can also convert the input to an integer directly if we want to work with numbers.
b = input("Enter another value: ")

print("you entered: ",a,"and",b)
print("the sum of the two values is: ",int(a)+int(b))
print("the sum of the two values is: ",a+b) # this will concatenate the two strings instead of adding  them as numbers because input() returns a string by default.
