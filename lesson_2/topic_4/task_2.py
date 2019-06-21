# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.


def get_power(number):
    if number <= 0:
        return False
    if number == 1:
        return True
    return number & 1 == 0 and get_power(number // 2)


n = int(input('Enter N: '))
print(get_power(n))
