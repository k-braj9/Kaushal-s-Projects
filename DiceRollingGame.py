import random
decision = input('Would you like to roll the dice? (y/n)')
list1 = [1, 2, 3, 4, 5, 6]
if (decision == 'y'):
    x = random.choice(list1)
    y = random.choice(list1)
    print(x, y)
elif(decision == 'n'):
    print('No worries. Come again Next Time!')
else:
    print('Invalid Choice')