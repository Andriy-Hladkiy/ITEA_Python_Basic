import random

number = random.randint(1, 100)

while True:
    while 1:
        try:
            yourNumber = int(input('Enter your number: '))
            break
        except ValueError:
            print("Ви помилились. Спробуйте знову.")
    if yourNumber > number:
        print('Ваше число завелике')
        continue
    elif yourNumber == number:
        print('Ви вгадали:)')
        break
    else:
        print('Ваше число замале')
        continue
