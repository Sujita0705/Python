import os
# specify the directory you want to list
directory_path = '/'

# list all files and directories in the specified path
comtents = os.listdir(directory_path)

# print each file and directory name
for item in comtents:
    print(item)