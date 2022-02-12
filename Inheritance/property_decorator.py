class employee:
    company = "Bharat gas"
    salary = 4000
    salaryBonus = 1000
    # totalSalary = salary + salaryBonus
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    @totalSalary.setter
    def totalSalary(self, val):
        self.salary = val - self.salary


e = employee()
print(e.totalSalary)
e.totalSalary = 5000
print(e.salary)
print(e.salaryBonus)
