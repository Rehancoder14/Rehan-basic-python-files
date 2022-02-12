import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')

randomnumber = random.randint(1,10)

userguess = None
guesses = 0

while (userguess!= randomnumber) :
    userguess = int(input("Enter Your number: "))
    if userguess == randomnumber:
        print(f"Your number is {userguess}, and is perfectly guessed")
    else:
        print("try again")
# with open("hiscore.txt", "r") as f:
#     hiscore = int(f.read())

# if (guesses < hiscore):
#     with open("hiscore.txt", "w") as f:
#         f.write(guesses)
