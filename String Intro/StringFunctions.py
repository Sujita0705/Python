a = "hello world"
print(len(a)) # prints the length of the string.

print(a.endswith("lo")) # checks if the string ends with "lo". Returns True.
print(a.endswith("lm")) # checks if the string ends with "lm". Returns False.

print(a.startswith("he")) # checks if the string starts with "he". Returns True.
print(a.startswith("He")) # checks if the string starts with "He". Returns False.
print(a.startswith("ha")) # checks if the string starts with "ha". Returns False.

print(a.capitalize()) # capitalizes the first letter of the string.

print(a.upper()) # converts the string to uppercase.

print(a.lower()) # converts the string to lowercase.

print(a.title()) # converts the string to title case (first letter of each word is capitalized).

print(a.count("l")) # counts the number of occurrences of "l" in the string.

print(a.find("world")) # finds the index of the first occurrence of "world" in the string. Returns -1 if not found.

print(a.replace("world", "Python")) # replaces "world" with "Python" in the string.