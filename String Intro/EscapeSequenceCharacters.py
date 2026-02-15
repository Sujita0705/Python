# Sequence of characters that are used to represent text. They are encloced in either single quotes (' '), double quotes( " "), or triple quotes (''' ''' or """ """).

# a = "hello
# world" # This will give us an error because the string is not properly closed.

a = "Hello \nWorld"
print(a) # this (\n) represents a new line in the string.

b = "This is a tab \t character"
print(b) # this (\t) represents a tab in the string.

c = "Hello \"World\""
print(c) # this (\") allows us to include double quotes inside the string.

print("This \\\\ is a backslash.") # To print a literal backslash, you must escape it with another backslash.

print(r"This \ is a backslash.")
# If you want Python to treat backslashes as literal characters, you can create a raw string by prefixing the string with the letter r or R. This is especially useful for regular expressions or file paths. 

print("Hello\rWorld") # Moves cursor to line start and overwrites "Hello" with "World".

print("Hello \bWorld") # Removes the previous character before "World", resulting in "HelloWorld".

