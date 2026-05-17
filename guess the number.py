import random
num=random.randint(1,1000)
attempt=0
while True:
    attempt+=1
    print("Enter your guess in between 1-1000")
    number=int(input("Enter your guess"))
    if number>num:
        print("Oh no, the number guessed is too high, try again!")
    elif number<num:
        print("Oh no, the number guessed is too low, try again!")
    else:
        print("Yay, you got that right!")
        print("You took",attempt,"tries to guess the number")
        break

