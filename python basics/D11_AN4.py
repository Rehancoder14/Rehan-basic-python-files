# Name : Rehan Sameer Mahat
# Div: D
# roll no : D11
# Assignment no 4



# To accept students five courses marks and compute his/her result.
# Student is passing if he/she scores marks equal to and above 40 in each course.
# If student scores aggregate greater than 75%, then the grade is distinction.
# If aggregate is 60>= and <75 then the grade if first division.
# If aggregate is 50>= and <60, then the grade is second division.
# If aggregate is 40>= and <50, then the grade is third division.

course1= int(input("Enter Your Marks:\n"))
course2= int(input("Enter Your Marks:\n"))
course3= int(input("Enter Your Marks:\n"))
course4= int(input("Enter Your Marks:\n"))
course5= int(input("Enter Your Marks:\n"))
passingmarks = 40
if (course1<40 or course2<40 or course3<40 or course4<40 or course5<40):
    print(" You are fail.")
elif (course1 + course2 + course3 + course4 + course5)/5 >= 75:
    print("You are pass with distinction.")
elif (course1 + course2 + course3 + course4 + course5)/5 >= 60:
    print("You are pass with first class. ")
elif (course1 + course2 + course3 + course4 + course5)/5 >= 50:
    print("Your are pass  with second class")
elif (course1 + course2 + course3 + course4 + course5)/5 >= 40:
    print("You are pass with third class")
else:
    print(" You are fail due to low aggregate.")
