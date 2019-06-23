# Найти факториал числа

number = input('Enter number: ')

while not number.isdigit():
    number = input('Ви помилились\n')
    number = str(number)

number = int(number)

factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(factorial)
