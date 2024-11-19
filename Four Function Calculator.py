'''
Four Function Calculator Python Code
Kaushal Raju
'''


'''
functions
'''

def add(number1, number2):
    return number1 + number2



def subtract(number1, number2):
    return number1 - number2



def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2
    
'''
code
'''

number1 = (float(input('pick a number: ')))
number2 = (float(input('pick another number: ')))

print('add, multiply, subtract, or divide? ')
operation = input()
x = 0
if (operation == 'add'):
    x = add(number1, number2)
    print(x)
elif (operation == 'multiply'):
    x = multiply(number1, number2)
    print(x)
elif (operation == 'subtract'):
    x = subtract(number1, number2)
    print(x)
elif (operation == 'divide'):
    x = divide(number1, number2)
    print(x)

    







    


    
    
