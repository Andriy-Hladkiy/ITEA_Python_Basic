# Написать рекурсивную функцию, которая возвращает сумму цифр числа


def sum_digit(n):
    if n > 0:
        return sum_digit(n // 10) + n % 10
    else:
        return 0


print(sum_digit(45))
