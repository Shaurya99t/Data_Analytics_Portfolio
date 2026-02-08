import os

# Specify the directory you want to list
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)
a=68
b=97
c=a+b
print(c)
f=type(c)
d=float(c)
e=type(d)
print(d)
print(e)
print(f)