# Name : Rehan Sameer Mahat
# Div: D
# roll no : D11
# Assignment no 6


#Write a python program that accepts a string from user and perform following string
#operations- i. Calculate length of string ii. String reversal iii. Equality check of two strings 
#iii. Check palindrome ii. Check substring

x=input("enter your string: ")

#print(len(x))

def callen(a):
    length=0
    for i in a:
        length+=1
    
    return length

def reversal(b):
    return b[::-1]

def equality(c):
    y=input("Enter ur second string: ")
    print("Second String: ",y)
    
    if (c==y):
        print("Both strings are EQUAL..!")
    else:
        print("Given two string are NOT EQUAL...!")
    
def palindrome(d):
    if (d==reversal(d)):
        print("Given string is a PALINDROME..!")
    else:
        print("Given string is NOT a palindrome.")
    
def checksub(e):
    sub=input("Enter the string you wish to search: ")
    print("Your are checking for: ",sub)

    if sub in e:
        print("Given string is a SUBSTRING ")
    else:
        print("Given string is NOT a substring")
    
#    if e.find(sub,0,len(e))==-1:
#        print("Given string is NOT a substring")
#    else:
#        print("Given string is a SUBSTRING")


choice=1

while(choice!=6):
    
    print("1: Calculate Length")
    print("2: Reverse the string")
    print("3: Check for equality")
    print("4: is Palindrome?")
    print("5: is SUBSTRING?")
    print("6: Exit")
    choice=int(input("Enter your choice: "))
    
    print("Your string is: ",x)
    if choice==1:
        print("Length of the string is = ",callen(x))
    
    elif choice==2:
        print("Reverse of the sring is = ",reversal(x))    
        
    elif choice==3:
        equality(x)
    
    elif choice==4:
        palindrome(x)  
    
    elif choice==5:
        checksub(x)



print("PROGRAM ENDS...!")
