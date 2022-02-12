# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

oddnum = 0
evennum = 0
for x in numbers:
        if not x % 2:
    	    oddnum+=1
        else:
    	    evennum+=1
print("Number of even numbers :",evennum)
print("Number of odd numbers :",oddnum)
    
