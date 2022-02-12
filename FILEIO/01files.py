
from os import linesep, read, write


f = open('Another.txt', 'r') #open is a built in function 
data= f.read() # Read is the built in function which is use to read the file 
print(data)
f.close() # close is the built in function to wrap the file 



# readline() function reads only the first line of the file 
# if the same function is overwritten will print next consecutive lines


# r = read
# w = write
# a = open for appending
# t = updating

# rb = will read in binary Mode 
# rt = will read in txt mode

