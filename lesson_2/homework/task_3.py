# Возвести число в степень с помощью цикла

while 1:
    try:
        number = int(input('Enter number: '))
        break
    except ValueError:
        print("Ви помилились. Спробуйте знову.")

while 1:
    try:
        degree = int(input('Enter degree: '))
        break
    except ValueError:
        print("Ви помилились. Спробуйте знову.")

while degree > 1:
    number *= number
    degree -= 1

print(number)
