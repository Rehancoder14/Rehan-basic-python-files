codinglanguage = {}
a = input("Enter your favourite language:\n")
b = input("Enter your favourite language:\n")
c = input("Enter your favourite language:\n")
d = input("Enter your favourite language:\n") 
codinglanguage["Dipuu"]= a
codinglanguage["Rehan"]= b
codinglanguage["Sid"]  =c 
codinglanguage["virat"]= d

codinglanguage["Dipuu"]= a
codinglanguage["Rehan"]= b
codinglanguage["Sid"]  =c 
codinglanguage["Sid"]= d  #here "sid" is repeatitive so it will prints just once its 1st fav lang
# In dictionary keys should be unique 
#if the values are same no change will be observed in output 
print(codinglanguage)

S= {8, 7, 12,"Rehan", 14,26}
 #list cannot be stored in set
S.remove(8)
print(S)
S.add(15)
print(S)
