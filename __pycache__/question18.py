# Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Enter file name :\n")
file_1 = filename.split(".")
print(repr(file_1[-1]))
