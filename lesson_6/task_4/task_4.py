from test2 import count_squares


def count_average(ready_line):
    total = 0
    for number in ready_line:
        total += number
        average = total / len(ready_line)
    return average


user_list = []
with open("test3_result.txt") as file:
    for line in file:
        strip_line = line.rstrip()
        ready_line = [int(x) for x in strip_line.split(' ')]
        av = count_average(ready_line)
        user_list.append(av)

print(count_squares(user_list))
