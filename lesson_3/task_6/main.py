import function


def get_choice():
    print('''
    1.Добавить в справочник
    2.Вывод номера телефона по имени
    3.Вывод имени по номеру телефона
    4.Посчитать количество номеров телефонов в которых есть три или более одинаковых цифр подряд
    5.Удалить человека из справочника
    6.Редактировать имя
    7.Редактировать номер
    8.Выход
    
    ''')
    choice_number = int(input('Enter your choice:\n'))

    if choice_number == 1:
        function.add_to_dict()
    elif choice_number == 2:
        function.get_telephone_number()
    elif choice_number == 3:
        function.get_name()
    elif choice_number == 4:
        function.get_count_digits()
    elif choice_number == 5:
        function.delete_people()
    elif choice_number == 6:
        function.change_name()
    elif choice_number == 7:
        function.change_number
    elif choice_number == 8:
        exit()


if __name__ == '__main__':
    get_choice()
