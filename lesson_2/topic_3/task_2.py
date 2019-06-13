def sum(massive):
    sum = 0
    for i in massive:
        sum += i
    print(sum)


def sort(massive):
    massive.sort(key=lambda x: sum(map(str, x)), reverse=True)
    print(massive)


massive = [14, 30, 103]

sum(massive)
sort(massive)
