class employee:
    salary = 50000
    increment = 1.5
    
    @property
    def salaryaftIncrement(self):
        return self.salary * self.increment

    @salaryaftIncrement.setter
    def salaryaftIncrement(self,sai):
        self.increment = sai/self.salary

e = employee()
print(e.salary)
print(e.salaryaftIncrement)


print(e.increment)
e.salaryaftIncrement = 100000
print(e.increment)
