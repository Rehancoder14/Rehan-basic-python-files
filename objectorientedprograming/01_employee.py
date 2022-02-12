class employee:
    company = "Google"
    salary = 50000
harry = employee()
rehan = employee()
harry.salary= 40000


# harry.salary = 30000 #these are the instance attribute
# rehan.salary = 1000000
print(harry.company)
print(rehan.company)
# above 2 line will print the company of employee which is google


employee.company = "youtube"
print(harry.company)
print(rehan.company)
# Now this line will print the  company of employee which is youtube(updated)


print(harry.salary)
print(rehan.salary)