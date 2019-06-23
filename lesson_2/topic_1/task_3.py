# Извлекать квадратный корень из введенного пользователем
# числа до тех пор, пока значение больше 10.

from math import *

i = int(input('Enter a number: '))

while i > 10:
    i = sqrt(i)
    print(i)
