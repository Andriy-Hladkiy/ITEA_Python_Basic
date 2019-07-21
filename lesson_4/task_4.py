# Без использования методов списков,
# напишите реализацию таких методов
# списков: insert, remove.


def do_insert(user_list, insert_item, pos):
    new_user_list = user_list[0:pos] + [insert_item] + user_list[pos:]
    return new_user_list


def do_remove(user_list, remove_item):
    if remove_item in user_list:
        counter = 0
        for item in user_list:
            if item != remove_item:
                counter += 1
            else:
                break
        new_user_list2 = user_list[0:counter] + user_list[counter + 1:]
    else:
        print("Элемет не найден")
        quit()
    return new_user_list2


user_list = ['car', 'cap', 'camera', 2342, 'Andriy', 12312]
print('Список пользователя: ', user_list)
insert_item = input('Введите вставляемый элемент : \n')
position = int(input('Введите номер позиции вставляемого элемента : \n'))
print(do_insert(user_list, insert_item, position))

remove_item = input('Введите удаляемый элемент : \n')
print(do_remove(user_list, remove_item))
