import random


def play():
    user = input('"r" for rock, "p" for paper, "s" for scissors:\n')
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie'
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return 'You Won!!!!!'
    else:
        return 'You Lost ): '


print(play())