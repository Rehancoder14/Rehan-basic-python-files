# snake water gun game project

import random
def gameWin(comp, you):
    if comp == you :
        return None

    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
            


print ("computer turn: snake(s) water(w) or gun(g)?")
randno =  random.randint(1,3)
print(randno)
if randno==1:
    comp = "s"
elif randno == 2:
    comp = "w"
else :
    comp = "g"


you =  input("your turn: snake(s) water(w) or gun(g)?")

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {comp}")

if a == None:
    print("The game is tie!😅😅 ")
elif a :
    print(" You win🥳👏")
else  : 
    print("You loose.\n Better luck next time.🙂")