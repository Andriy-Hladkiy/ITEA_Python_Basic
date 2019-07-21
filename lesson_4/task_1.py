# Пользователь задает случайное число n. Сгенерировать
# список этой длины и заполнить его 0 и 1 случайным образом.
# Найти самую длинную цепочку из подряд идущих 0 или 1.
# Вывести эту длину. Для какого максимального значения n, ваш
# алгоритм будет работать меньше чем 1 секунда?

import random

your_number = int(input('Введите число: \n'))
my_list = []
for i in range(your_number):
    my_list.append(random.randint(0, 1))
print(my_list)

my_string_list = [str(i) for i in my_list]
value = ''.join(my_string_list)
string_value = str(value)

print(string_value)

max_zero = len(max(string_value.split('1'), key=len))
max_one = len(max(string_value.split('0'), key=len))

print('самая длинная цепочка 0:', max_zero)
print('самая длинная цепочка 1:', max_one)
