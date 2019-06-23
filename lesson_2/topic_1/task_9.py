# Вывести n чисел фибоначчи: 1 1 2 3 5 8 13...

fib1 = fib2 = 1

n = int(input())

if n < 2:
    quit()

print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
