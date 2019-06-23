# Выведите случайные числа в заданном пользователем диапазоне

import random

firstNumber = int(input('Enter first number of diapason: '))
secondNumber = int(input('Enter second number of diapason: '))

if firstNumber < secondNumber:
    print(random.randint(firstNumber, secondNumber))
else:
    print(random.randint(secondNumber, firstNumber))
