from math import trunc
import random
r = random.randint(1,10)
while True:
    num = int(input())
    if num< r:
        print("Wrong guessed, Try greater num: ")
    elif (num>r):
        print("Wrong guessed, try smaller num: ")
    else :
        print("well guessed")
        break