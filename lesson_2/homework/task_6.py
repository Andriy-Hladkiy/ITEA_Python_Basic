# Нарисовать равнобедренный треугольник из символов ^.
# Высоту выбирает пользователь. Например: высота = 5, на экране


height = input('Enter height: ')

while not height.isdigit():
    height = input('Ви помилились\n')
    height = str(height)

height = int(height)


n = height - 1
k = 1
c = 0

for i in range(1, height + 1):
    print(' ' * n, '^' * k)
    n -= 1
    k += 2
    c += 1
