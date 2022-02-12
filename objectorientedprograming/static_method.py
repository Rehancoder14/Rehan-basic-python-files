class employee:
    company = "Google"

    def getsalary(self): #self is a parameter which passes automatically once an object is called.
        print(f"salary for this employee working in {self.company} is {self.salary}")
   #self function is used to access both attribute i.e, class and instance


    @staticmethod #static method is the decorator which can run the function without self
    def greet():
        print("Good morning, sir") #we can use multiple static method
        

rehan = employee()
rehan.salary = 10000000
rehan.greet()
rehan.getsalary()
