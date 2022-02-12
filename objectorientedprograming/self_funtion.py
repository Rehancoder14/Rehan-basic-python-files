class employee:
    company = "Google"
    def getsalary(self): #self is a parameter which passes automatically once an object is called.
        print(f"salary is {self.salary}")
   #self function is used to access both attribute i.e, class and instance
        

rehan = employee()
rehan.salary= 1000000
rehan.getsalary() # employee.getsalary(rehan)
 #both are expectable