class C2Dvector:
    def __init__(self,i,j):
        self.icap = i 
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j "

class C3Dvector(C2Dvector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k "



a = int(input("Enter Your number: "))
b = int(input("Enter Your number: "))

vector2d = C2Dvector(a,b)
print(vector2d)

x = int(input("Enter Your number: "))
y = int(input("Enter Your number: "))
z = int(input("Enter Your number: "))
vector3d = C3Dvector(x,y,z)
print(vector2d)
print(vector3d)