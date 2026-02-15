a = "Hello"
#  """This is a multi-line string with "quotes" and 'apostrophes' inside."""
#  '''A nother multi-line string that can contain both "double quotes" and 'single quotes' inside.'''
# String is immutable, so we cannot change it after it's created. However, we can create a new string by concatenating or slicing.
length = len(a)
print(length)
nameshort = a[0:4] # start from index 0 and go up to but not including index 3. We can start indexcing from the end of the string using negative indices. For example, a[-1] gives us the last character of the string.
print(nameshort)
print(a[0])
print(a[-1])
print(a[1:5])
print(a[1:]) # start from index 1 and go to the end of the string. Same as a[1:len(a)]
print(a[:4]) # start from the beginning of the string and go up to but not including index 4. Same as a[0:4].