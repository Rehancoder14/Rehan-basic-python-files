 #prob 1
f1 = input("Enter Fruit Name 1 :  ")
f2 = input("Enter Fruit Name 2 :  ")
f3 = input("Enter Fruit Name 3 :  ")
f4 = input("Enter Fruit Name 4 :  ")
f5 = input("Enter Fruit Name 5 :  ")
f6 = input("Enter Fruit Name 6 :  ")
f7 = input("Enter Fruit Name 7 :  ") 
myfruitlist = [f1, f2, f3, f4, f5, f6, f7]
print(myfruitlist)

#prob2 
stud1 = int(input("Enter Your marks : "))
stud2 = int(input("Enter Your marks : "))
stud3 = int(input("Enter Your marks : "))
stud4 = int(input("Enter Your marks : "))
stud5 = int(input("Enter Your marks : "))
stud6 = int(input("Enter Your marks : "))
studentranklist = [stud1, stud2, stud3, stud4, stud5, stud6]
studentranklist.sort()
print(studentranklist) 


# prob3 
# t= (2,3,4,5,5,65,68,54) 
# t[2] = 45 #this will show the type error as tuple cannot be altered or manipulated
# print(t) 

#prob 4 
a = [5, 10, 15, 20 ] 
print(sum(a)) 


#prob5 
a = (7, 0, 8, 0, 0, 9) 
print(a.count(0))