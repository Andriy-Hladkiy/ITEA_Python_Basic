# Напишите функцию remove по индексу и по подстроке (для строк).


def do_remove_ind(str_to_remove, start_del_index, end_del_index):
    new_string = str_to_remove[:start_del_index] + str_to_remove[end_del_index + 1:]
    return new_string


def do_remove_substr(str_to_remove2, substring):
    first_simbol = substring[0]
    index = 0
    if substring in str_to_remove2:
        for i in str_to_remove2:
            if i != first_simbol:
                index += 1
            else:
                break
    new_string2 = str_to_remove2[:index] + str_to_remove2[index + len(substring):]
    return new_string2


string_to_remove = input('Введите строку: \n')
start_del_index = int(input('Введите индекс с которого начнтся удаление: \n'))
end_del_index = int(input('Введите индекс которым закончится удаление: \n'))
print(do_remove_ind(string_to_remove, start_del_index, end_del_index))

string_to_remove2 = input('Введите строку: \n')
substring = input('Введите подстроку удаления : \n')
print(do_remove_substr(string_to_remove2, substring))
