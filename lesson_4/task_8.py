# Без использования методов словарей(кроме items),
# напишите  функцию remove по ключу
# и remove по значению.


def do_remove_by_key(user_dict, key):
    new_dict = {i: user_dict[i] for i in user_dict if i != key}
    return new_dict


def do_remove_by_value(user_dict, value):
    new_dict = {}
    for k, v in user_dict.items():
        if v != value:
            new_dict[k] = v
    return new_dict


user_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(user_dict)

key = int(input("Удалить по ключу: \n"))
print(do_remove_by_key(user_dict, key))

value = input("Удалить по значению: \n")
print(do_remove_by_value(user_dict, value))
