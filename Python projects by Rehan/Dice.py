#importing the random module
import random 
def dice_rolling(startfrom, endwit):
# creating while loop in order to run according to will of the user
    while True:  
        print("DICE Rolling.....")
        # generating random number using randint function between 1 to 6
        dice = random.randint(startfrom,endwit)   
        print("Your number after rolling the dice is : ", dice)
        a = input("do want to roll the dice again: yes(y) or No(n): ") # getting the input from the user either to run or break the loop.
        if (a=="n"):
            break
        else:
            continue
A = dice_rolling(1, 6)
print(A) 



