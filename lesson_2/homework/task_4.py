'''Проверить является ли введенное число простым.
Число считается простым если оно не делится нацело
на все числа до квадратного корня этого числа'''

while 1:
    try:
        number = int(input('Enter number: '))
        break
    except ValueError:
        print("Ви помилились. Спробуйте знову.")

x = True
for i in range(2, number):
    if number % i == 0:
        x = False
        break

if x:
    print("prime")
else:
    print("not prime")
