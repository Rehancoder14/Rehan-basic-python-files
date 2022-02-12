# complex number formula = (a+bi) (c+ di) = (ac - bd) + (ad + bc) i 

class complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,comp):
        return complex(self.real + comp.real, self.imaginary + comp.imaginary)
    
    def __mul__(self, comp):
        return complex(self.real * comp.real, self.imaginary * comp.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = complex(5,6)
c2 = complex(3,4)
print(c1 + c2)
print(c1 * c2)
