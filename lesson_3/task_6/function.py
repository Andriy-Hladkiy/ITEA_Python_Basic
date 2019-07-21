from main import get_choice


dictionary = {
    'John': '+380953336667',
    'Alan': '+36674490',
    'Andriy': '+380968226831',
    'Michael': '+380934531234',
}


def add_to_dict():
    print(dictionary)
    dict_key = str(input('Введите ключ:\n'))
    dict_value = str(input('Введите значение: \n'))
    dictionary.update({dict_key: dict_value})
    print(dictionary)
    get_choice


def get_telephone_number():
    dict_key = str(input('Введите ключ: \n'))
    print(dictionary.setdefault(dict_key))
    get_choice


def get_name():
    new_dict = dict(zip(dictionary.values(), dictionary.keys()))
    dict_key = str(input('Введите значение\n'))
    print(new_dict.setdefault(dict_key))
    get_choice


def get_count_digits():
    numbers = list(dictionary.values())
    print(numbers)
    count_numbers = []
    r = 0
    while r < len(numbers):
        numm = numbers[r]
        for p in range(2, len(numm) - 1):
            if numm[p] == numm[p - 1] and numm[p - 1] == numm[p - 2]:
                count_numbers.append(numm)
        r = r + 1
    print(count_numbers)
    get_choice


def delete_people():
    dict_key = str(input('Введите имя человека которого хотите удалить: '))
    dictionary.pop(dict_key, None)
    print(dictionary)
    get_choice


def change_name():
    print(dictionary)
    old_key = str(input('Введите ключ который хотите изменить: '))
    new_key = str(input('Введите новый ключ: '))
    dictionary[new_key] = dictionary.pop(old_key)
    print(dictionary)
    get_choice


def change_number():
    print(dictionary)
    new_dict = dict(zip(dictionary.values(), dictionary.keys()))
    old_key = str(input('Введите значение которое хотите изменить: '))
    new_key = str(input('Введите новое значение: '))
    new_dict[new_key] = new_dict.pop(old_key)
    old_dict = dict(zip(new_dict.values(), new_dict.keys()))
    print(old_dict)
    get_choice
