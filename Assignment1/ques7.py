# 7. Explore the `os` module in Python and write a Python program to:
# 	- List all files in a folder entered by user.
# 	- Rename any given file in the specified folder

import os

dir = input("Enter directory path to list all its files:")
l = os.listdir(dir)
ch=input("See all files(y/n)?:")
if ch=='y' or ch == 'Y':
	print(l)
	print()
else:
	print()

os.chdir(dir)

curName = input("Enter file name to rename: ")
newName = input("Enter new name for file: ")

os.rename(curName,newName)

print("Rename successful!")