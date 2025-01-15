import random
import string

list1 = []

print('Generating Password......')

user_input1 = (int(input('What is your preferred amount of characters for your password?: ')))
user_input2 = (input('Would you like the password to consist of special characters?: '))
for i in range(user_input1):
    if user_input2 == ('yes' or 'YES' or 'Yes'):
        character = random.choice(string.printable)
    else:
        character = random.choice(string.ascii_letters + string.digits)
    list1.append(character)
s = ''.join(list1)

print(s)




