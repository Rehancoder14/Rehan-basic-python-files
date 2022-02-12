pi = 3.14
def area(radius):
    A = (pi * (radius ** 2))
    return A 

radius1  = float(input("radius:"))#here if the radius input would be in decimal then th
#the float function or else int function.
Area1 =  area(radius1)
print(Area1)

# or

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

