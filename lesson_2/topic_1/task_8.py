# Найти сумму цифр числа 2 способами: циклом интерпретируя
# число как str и с помощью операций ‘%’, ‘/’, интерпретируя
# число как Integer

number = str(input('Enter number: '))
number_sum = 0

for i in number:
    number_sum += int(i)

print(number_sum)

number = int(input('Enter number: '))
number_sum = 0

while number > 0:
    if number % 10 != 0:
        number_sum = number_sum + number % 10
        number = number // 10

print(number_sum)
