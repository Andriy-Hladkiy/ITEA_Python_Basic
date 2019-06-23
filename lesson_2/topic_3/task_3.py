# Написать функцию, которая заполняет массив случайными
# числами в диапазоне, указанном пользователем.

import random


def set_array(start_of_range, end_of_range, m=8):
    result = []
    if start_of_range == end_of_range:
        return None
    else:
        start = min(start_of_range, end_of_range)
        end = max(start_of_range, end_of_range)
        for j in range(m):
            result.append(random.randint(start, end))
    return result


start_of_range = int(input('Enter start: '))
end_of_range = int(input('Enter end: '))
print(set_array(start_of_range, end_of_range))
