def addition(num1, num2):
    result = num1 + num2
    return result


def subtraction(num1, num2):
    result = num1 - num2
    return result


def multiplication(num1, num2):
    result = num1 * num2
    return result


def division(num1, num2):
    result = num1 / num2
    return result


print("Welcome to our magical calculator! wooooooooo")
choice = float(input(
    'Choose and operation to perform: \n 1- Addition\n 2- Subtraction\n 3- Multiplication\n 4- Division\n'))
value1 = float(input('Enter first value: \n'))
value2 = float(input('Enter second value: \n'))

if choice == 1:
    print('The result is:', addition(value1, value2))

if choice == 2:
    print('The result is:', subtraction(value1, value2))

if choice == 3:
    print('The result is:', multiplication(value1, value2))

if choice == 4:
    print('The result is:', division(value1, value2))
