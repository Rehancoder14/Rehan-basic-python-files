comment= input("Enter your text:\n")
if ("makes a lot of money" in comment):
    spam = True
elif("buy now"in comment):
    spam = True
elif ("click this"in comment):
    spam= True
elif ("subscribe now" in comment):
    spam = True
else:
    spam = False
if (spam): 
    print("This text is spam")
else :
    print("This text is not spam")