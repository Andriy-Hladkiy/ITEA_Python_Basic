matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

k = 0
matrix_sum = 0

for i in matrix[k]:
    for j in i:
        matrix_sum += j
    k += 1
