# Написать функцию, которая вычисляет среднее
# арифметическое элементов массива(списка),
# переданного ей в качестве аргумента.


def get_mid_array(array):
    count = 0
    sum_of_number = 0
    for i in array:
        count += 1
        sum_of_number += i
    mid = sum_of_number / count
    print(mid)


user_array = [1, 5, 3, 9, 1]

get_mid_array(user_array)
