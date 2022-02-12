class employee:
    company = "Google"

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created")

    def getdetails(self):
        print(f"The name of the employee is \n{self.name}")
        print(f"The salary of the employee is \n{self.salary}")
        print(f"The subunit of the employee is \n{self.subunit}")
        

    def getsalary(self,signature): #self is a parameter which passes automatically once an object is called.
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")
   #self function is used to access both attribute i.e, class and instance


    @staticmethod #static method is the decorator which can run the function without self
    def greet():
        print("Good morning, sir") #we can use multiple static method
        
rehan = employee("rehan", 100000,"google")
rehan.getdetails()

