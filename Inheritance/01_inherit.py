class employee: #class employee is base class
    company = "Google"
    def showdetails(self):
        print("This is an employee.")

class name(employee):
    name = "Rehan"
    def getname(self):
        print("The Name of the employee is Rehan.")


class programmer(employee): #class programmer is child class derived from parent class employee
    language = "Python"
    def getlang(self):
        print("The language of the programmer is python", )
    def showdetails(self):
        print("he is a coder.")


e = employee()
p = programmer()
e.showdetails()
p.getlang()
print(p.company)
p.showdetails()

