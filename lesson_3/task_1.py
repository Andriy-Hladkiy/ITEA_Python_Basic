''' Вывести прямоугольник со сторонами a,b
Например a = topic_3, b=topic_2
***
*** '''

a = int(input('Enter a: '))
b = int(input('Enter b: '))

for i in range(1, b + 1):
    print('*' * a)
