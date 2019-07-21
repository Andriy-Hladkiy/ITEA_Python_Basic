# Напишите функцию, которая сортирует
# массив рекурсивно.


def do_rec_sort(user_array):
    if user_array:
        point_left = [x for x in user_array if x < user_array[0]]
        point_x = [x for x in user_array if x == user_array[0]]
        point_right = [x for x in user_array if x > user_array[0]]
        return do_rec_sort(point_left) + point_x + do_rec_sort(point_right)
    return []


user_array = [43, 456, 123, 76, 45, 87, 23, 97, 76]
print('Массив:', user_array)
print('Отсортированный массив', do_rec_sort(user_array))
