# Без использования методов строк, напишите реализацию
# таких методов строк: replace, split, find.


def do_replace(user_string, x, y):
    new_string = ""
    for char in user_string:
        if char == x:
            new_string += y
        else:
            new_string += char
    return new_string


def do_split(string, w):
    new_list = []
    stringe = string + '$'
    current_word = ''
    for char in stringe:
        if char == w or char == '$':
            if current_word:
                new_list.append(current_word)
            current_word = ''
        else:
            current_word += char
    return new_list


def do_find(str_to_find, f):
    index = 0
    while str_to_find[index:index + len(f)] != f:
        index += 1
        if f not in str_to_find:
            return -1
    return index


user_string = input('Ведите строку: \n')
x = input('Ведите то, что нужно заменить: \n')
y = input('Меняем на: \n')
print(do_replace(user_string, x, y))

string = input('Введите строку: \n')
w = input('Введите символ разделения: \n')
print(do_split(string, w))

string_to_find = input('Ведите строку: \n')
f = input('Найти: \n')
print(do_find(string_to_find, f))
