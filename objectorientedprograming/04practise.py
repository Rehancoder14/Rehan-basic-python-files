
class calculator:

    def __init__(self,num):
        self.number = num
    
    def square(self):
        print(f"The value of {self.number} is {self.number **2}")

    def squareroot(self):
        print(f"The value of {self.number} is {self.number**0.5}")
    
    def cube(self):
        print(f"The value of {self.number} is {self.number**3}")
    @staticmethod
    def greet():
        print("Hello,\nwelcome to the calculator")
       
a = calculator(4)    
a.square()   
a.cube()
a.squareroot()
a.greet()

        
        