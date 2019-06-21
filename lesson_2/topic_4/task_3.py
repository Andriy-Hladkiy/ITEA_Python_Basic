# Дано натуральное число N. Выведите все его цифры
# по одной, в обратном порядке, разделяя их пробелами
# или новыми строками.1/5


def rev(x):
    if x > 0:
        print(x % 10, end=' ')
        rev(x//10)


number = int(input('Enter number: '))
print(rev(number))
