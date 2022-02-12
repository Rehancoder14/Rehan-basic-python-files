# Name : Rehan Sameer Mahat
# Div: D
# roll no : D11
# Assignment no 5
#To simulate simple calculator that performs basic tasks such as addition, subtraction,
#multiplication and division with special operations like computing x^y and x!

def addnum(num1,num2):     #addition function definiation
    r=num1+num2            #adding given two numbers
    return r               #returning the result

def subnum(a,b):
    return a-b

def multinum(c,d):
    return c*d

def divinum(e,f):
    return e/f
    
def power(g,h):
    return g**h

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    

x=int(input("Enter first  number: "))
y=int(input("Enter second number: "))



print("1. Addition")
print("2. Substraction")
print("3. Division")
print("4. Multiplication")
print("5. Power x^y")
print("6. Factorial")
choice=int(input("Enter your choice: "))

if choice==1:
    print("Addition= "+str(addnum(x,y)))     #function calling

elif choice==2:
    print("Substraction= "+str(subnum(x,y)))

elif choice==3:
    print("Division= ",str(divinum(x,y)))
    
elif choice==4:
    print("Multiplication= ",str(multinum(x,y)))

elif choice==5:
    print("x^y is = ",str(power(x,y)))

elif choice==6:
    print("Factorial of first no = ",str(fact(x)))
    print("Factorial of second no= ",str(fact(y)))
else:
    print("Invalid choice..!")
