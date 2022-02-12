num1  =  int(input("Enter Your number:\n"))
num2  =  int(input("Enter Your number:\n"))
num3  =  int(input("Enter Your number:\n"))

if num1<num2 :
    a = num2
else:
    a =  num1

if num1< num3:
    b = num3
else:
    b = num1

if a<b:
    print("The greater number among three number is ",b)
else:
    print("The greater number among three number is ", a)
