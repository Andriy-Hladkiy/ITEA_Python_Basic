# Найти факториал числа

while 1:
    try:
        number = int(input('Enter number: '))
        break
    except ValueError:
        print("Ви помилились. Спробуйте знову.")

factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(factorial)
