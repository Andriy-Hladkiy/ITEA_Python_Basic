# Напишите программу, которая считает сумму последних цифр двух введенных пользователем чисел

number_one = input('Enter a: ')
number_two = input('Enter b: ')

print(int(number_one[-1]) + int(number_two[-1]))
