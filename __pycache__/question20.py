# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input("Enter any Integer:\n"))
compute1 = str(n)
compute2 = str(n)+str(n)
compute3 = str(n)+str(n)+str(n)
compute = (int(compute1) + int(compute2) +  int(compute3))
print(compute)