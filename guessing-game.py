import random

def guess():
    random_num = random.randint(1, 10)
    guessed = 0
    while guessed != random_num:
        guessed = int(input('Guess a number between 1 and 10: '))
        if guessed == random_num:
            print(f'Yaaaaaaaaaay, you got {random_num} right')
        else:
            print('Nah, Try again!')
            
guess()
