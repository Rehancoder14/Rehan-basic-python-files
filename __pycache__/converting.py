def converter(sgpa):
    percentage = (sgpa*10)-7.5
    return percentage

your_sgpa = float(input("Enter Your sgpa:\n"))
A = converter(your_sgpa)
print("Your percentage is ",A)