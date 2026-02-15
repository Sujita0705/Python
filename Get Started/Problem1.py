# Write a python program to print the contents of a directory using the OS module. Search online for the function which does that.
import os
# specify the directory you want to list
directory_path = '/'

# list all files and directories in the specified path
comtents = os.listdir(directory_path)

# print each file and directory name
for item in comtents:

    print(item)
