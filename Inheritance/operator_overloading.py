#Dunder method

class number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,num2): #for addition
        print("Lets add")
        return self.num + num2.num

    def __mul__(self,num2): #for multiplication
        print("Lets Multiply")
        return self.num * num2.num

    def __sub__(self,num2): #for substraction
        print("Lets substract")
        return self.num - num2.num
    
    def __truediv__(self,num2): #for division
        print("Lets divide")
        return self.num / num2.num
    
    def __floordiv__(self,num2): #for float division
        print("Lets divide")
        return self.num // num2.num
    
    def __str__(self):
        return f"Decimal number : {self.num}"
    
    def __len__(self):
        return 5



n1 = number(4)
n2 = number(6)
sum = n1 + n2 
print(sum)

multiply = n1 * n2
print(multiply)

substract = n2 - n1
print(substract)

div = n2 / n1
print(div)


floor_div = n2 // n1
print(floor_div)


n = number(9) #def str
print(n)
print(len(n))