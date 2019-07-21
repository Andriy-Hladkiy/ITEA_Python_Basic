'''Нарисовать равнобедренный треугольник из символов ^.
Высоту выбирает пользователь. Например: высота = 5, на экране
'''

while 1:
    try:
        height = int(input('Enter height: '))
        break
    except ValueError:
        print("Ви помилились. Спробуйте знову.")
n = height - 1
k = 1
c = 0

for i in range(1, height + 1):
    print(' ' * n, '^' * k)
    n -= 1
    k += 2
    c += 1
