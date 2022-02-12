def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
A = int(input("Enter Your Number:"))
f = factorial(A)
print(f)