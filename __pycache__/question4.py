# Write a Python program to guess a number between 1 to 9. 
# write a number until it is guessed correctly

import random
target_num, guess_num = random.randint(1, 10)
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
