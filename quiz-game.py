questions = ['Q1: What does CPU stands for? ',
             'Q2: What does RAM stands for? ',
             'Q3: What does ROM stands for? ',
             'Q3: What does UML stands for? ']

answers = ['central processing unit',
           'random access memory',
           'read only memory',
           'unified modeling language']

counter = 0
correct = 0

print('Welcome to you Quiz Game')
play = input('Ready for a challenge? y/n\n')
if play != 'y':
    print('Bye Bye !')
    quit()
else:
    print('Let\'s start')
    for i in questions:
        answer = input(i)
        if answer == answers[counter]:
            print('correct')
            correct += 1
        else:
            print('incorrect')
        counter += 1
    print(f'You got {correct} answers right')
