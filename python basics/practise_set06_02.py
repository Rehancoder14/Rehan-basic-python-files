# Write a program to find the greatest number of the numbers enter by the user 
a1 = int(input("Enter Your Name:\n"))
a2 = int(input("Enter Your Name:\n"))
a3 = int(input("Enter Your Name:\n"))
a4 = int(input("Enter Your Name:\n"))

if(a1> a2):
    num1 = a1
else: 
    num1 = a2

if (a3> a4):
    num2 = a3
else:
    num2 = a4

if (num1>num2):
    print(num1, "is greatest")
else :
    print(num2, "is greatest")