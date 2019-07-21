def sum(array):
    sum = 0
    for i in array:
        sum += i
    print(sum)


def sort(array):
    array.sort(key=lambda x: sum(map(str, x)), reverse=True)
    print(array)


array = [14, 30, 103]

sum(array)
sort(array)
