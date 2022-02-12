mylist= ["Rehan", "range","creategem", "possible"]
myl1 = mylist[0]
myl2 = mylist[1]
myl3 = mylist[2]
myl4 = mylist[3]
A1 = len(mylist[0])
A2 = len(mylist[1])
A3 = len(mylist[2])
A4 = len(mylist[3])

if A1> A2:
    lengthyword1= A1
else:
    lengthyword1= A2

if A3> A4:
    lengthyword2= A3
   
else:
    lengthyword2= A4
  
if lengthyword1 > lengthyword2:
    print(myl4)
    print("The lenth of the word is ", lengthyword1)
else:
    print(myl3)
    print("The lenght of the word is ", lengthyword2)


print("Hello World")