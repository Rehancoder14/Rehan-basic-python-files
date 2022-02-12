marks = int(input("Enter your marks:\n"))
if (marks >= 90 and marks<=100):
    print("Excellant grade")
elif(marks >= 80 and marks<=89):
    print("A grade")
elif(marks >=70  and marks<=79):
    print("B grade")
elif (marks >= 60 and marks<=69):
    print("C grade")
elif(marks >= 50 and marks<=59):
    print("D grade")
else:
    print("F grade")

A = input("Enter Your Post:\n")
B= "Rehan"
if B in A:
    print("This post is talking about Rehan")
else :
    print("This post is not talking about Rehan ")