class employee:
    company = "Camel"
    salary = 100000
    location = "Delhi"

    # def changeSalary(self,sal):
    #     self.__class__.self.salary = sal #changes the class attribute

    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal  #alternate method for changing the class attribute



e = employee()
print(e.salary)
e.changeSalary(500000)
print(e.salary)
print(employee.salary)
