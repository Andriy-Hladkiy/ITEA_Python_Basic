import random


def generate_numbers():
    return_list = []
    for i in range(5):
        number = random.randint(0, 10)
        return_list.append(number)
        i += 1
    joint_list = ' '.join([str(n) for n in return_list])
    return joint_list


with open("test3_result.bin", 'wb') as result_file:
    for i in range(100):
        result_file.write(bytes(generate_numbers() + '\n', 'utf8'))
        i += 1
