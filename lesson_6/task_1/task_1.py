from collections import Counter

with open("test1") as input_file:
    count = Counter(word for line in input_file for word in line.split())
    result = count.most_common(5)

with open("test1_result.txt", "w") as result_file:
    print(result, file=result_file)
