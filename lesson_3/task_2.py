a = [[1, 2, 3, 4], [5, 6, 7, 3], [7, 8, 9, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print(s)
