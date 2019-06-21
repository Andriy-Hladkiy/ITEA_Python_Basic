# Возвести число в степень с помощью цикла

number = input('Enter number: ')

while not number.isdigit():
    number = input('Ви помилились\n')
    number = str(number)

number = int(number)

degree = input('Enter degree: ')

while not degree.isdigit():
    degree = input('Ви помилились\n')
    degree = str(degree)

degree = int(degree)

while degree > 1:
    number *= number
    degree -= 1

print(number)
