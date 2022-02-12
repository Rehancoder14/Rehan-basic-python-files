sub1= int(input("Enter Your Marks:\n"))
sub2= int(input("Enter Your Marks:\n"))
sub3= int(input("Enter Your Marks:\n"))
passingmarks= 33
if (sub1<passingmarks or sub2<passingmarks or sub3< passingmarks):
    print("you are fail")
elif (sub1+sub2+ sub3)/3 < 40:
    print("You are fail due to less total percentage less ")
elif (sub1 +sub2+ sub3)/ 3 > 75:
    print("Your are pass with distinction")
elif (sub1 +sub2+ sub3)/ 3 > 60 and (sub1 +sub2+ sub3)/ 3 < 75:
    print("your pass with A grade")
else:
    print("You are pass ")

  
