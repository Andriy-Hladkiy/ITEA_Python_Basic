# Напишите программу “угадай число”.  Компьютер генерирует рандомное
# число (функция random), пользователь вводит числа, пока не угадает,
# а компьютер отвечает больше или меньше

import random

number = random.randint(1, 100)

while True:
    while 1:
        try:
            your_number = int(input('Enter your number: '))
            break
        except ValueError:
            print("Ви помилились. Спробуйте знову.")
    if your_number > number:
        print('Ваше число завелике')
    elif your_number < number:
        print('Ваше число замале')
    else:
        print('Ви вгадали:)')
        break
