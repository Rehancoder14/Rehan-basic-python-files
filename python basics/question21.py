humanage = int(input("Input a dog's age in human years: "))

if humanage < 0:
	print("Age must be positive number.")
	exit()
elif humanage <= 2:
	dogage = humanage * 10.5
else:
	dogage = 21 + (humanage - 2)*4

print("The dog's age in dog's years is", dogage)