import copy


def get_copy_function(l):
    result_copy = copy.copy(l)
    return len(result_copy)


array = [w * 2 for w in 'python']
dictionary = {a: a ** 2 for a in range(1, 6)}

dictionary[7] = 7 ** 2
array.append('java')

print(get_copy_function(array))
print(get_copy_function(dictionary))
