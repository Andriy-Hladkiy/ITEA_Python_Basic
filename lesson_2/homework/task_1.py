# Выводить буквы строки, до первой заглавной

string = str(input('Enter your string: '))

for i in string:
    if i.isupper():
        break
    else:
        print(i, end='')
