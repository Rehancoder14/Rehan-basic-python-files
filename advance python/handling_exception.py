try: 
    a = int(input("Enter your number: "))
    b = 1/a
    print(b)
except ValueError as e:
    print("Exception 1 Occured: ")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you have not divided by zero : ")
    print(e)

print("Thanks for using this code")
