class person: 
    def __init__(self):
        print("Initialising  person.....")
    country = "India"
    def takebreath(self):
        print("I am breathing...")

class Employee(person):
    company  = "Google"
    def getsalary(self):
        print(f"The salary is {self.salary}")       
    @staticmethod
    def takebreath():
        print("I am an employ and I am luckily breathing.😊")

class programmer(Employee):
    company = "fiverr"

    def getsalary(self):
        print(" salary to the programmer is 10 million $ ")

    def takebreath(self):
        super().__init__()
        super().takebreath()
        print("I am an employ and I am luckily breathing.😌")


p = person()
e = Employee()
pr = programmer()


print(p.country) #prints country of the person mentioned in class person
p.takebreath() 


print(e.company)
e.takebreath()


print(pr.company)
pr.takebreath()


