# Организовать непрерывный ввод цифр с клавиатуры, пока
# пользователь НЕ введёт 0 После ввода нуля, показать
# на экран количество чисел, которые были Введены, их
# общую сумму и среднее арифметическое.

count = 0
sum = 0
while True:
    number = int(input('Enter number: '))
    if number == 0:
        count += 1
        mid = sum/count
        break
    else:
        count += 1
        sum += number
        mid = sum/count
        continue

print(count)
print(sum)
print(mid)
