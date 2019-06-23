# Сортировка массива


def get_array_of_sum_digits(l):
    size = len(l)
    res_array = []

    for i in range(size):
        s = 0
        for j in str(l[i]):
            s += int(j)
        res_array.append(s)

    return res_array


def get_sorted_array(l):
    def sum_digits(a):
        s = 0
        for i in a:
            s += int(i)
        return s

    size = len(l)

    for i in range(size):
        index_min = i

        for j in range(i+1, size):
            if sum_digits(str(l[j])) < sum_digits(str(l[index_min])):
                index_min = j
        temporary = l[index_min]
        l[index_min] = l[i]
        l[i] = temporary

    return l


array = [14, 30, 103]

print(array)
print(get_array_of_sum_digits(array))
print(get_sorted_array(array))
