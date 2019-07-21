def get_mid_array(array):
    count = 0
    sum = 0
    for i in array:
        count += 1
        sum += i
    mid = sum / count
    print(mid)


array = [1, 5, 3, 9, 1]

get_mid_array(array)
