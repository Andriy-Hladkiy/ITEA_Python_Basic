# Вывести сумму всех делителей заданного числа

number = input('Enter number: ')

while not number.isdigit():
    number = input('Ви помилились\n')
    number = str(number)

number = int(number)

s = 0

for i in range(1, number + 1):
    if number % i == 0:
        s += i
        continue
    else:
        continue

print(s)
