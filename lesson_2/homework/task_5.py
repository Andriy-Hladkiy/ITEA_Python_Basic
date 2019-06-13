'''Вывести сумму всех делителей заданного числа'''

while 1:
    try:
        number = int(input('Enter number: '))
        break
    except ValueError:
        print("Ви помилились. Спробуйте знову.")

s = 0

for i in range(1, number + 1):
    if number % i == 0:
        s += i
        continue
    else:
        continue

print(s)
