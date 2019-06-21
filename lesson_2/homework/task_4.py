# Проверить является ли введенное число простым.
# Число считается простым если оно не делится нацело
# на все числа до квадратного корня этого числа'''

number = input('Enter number: ')

while not number.isdigit():
    number = input('Ви помилились\n')
    number = str(number)

number = int(number)

x = True
for i in range(2, number):
    if number % i == 0:
        x = False
        break

if x:
    print("prime")
else:
    print("not prime")
