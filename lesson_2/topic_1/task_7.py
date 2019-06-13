count = 0
sum = 0
while True:
    number = int(input('Enter number: '))
    if number == 0:
        count += 1
        mid = sum/count
        break
    else:
        count += 1
        sum += number
        mid = sum/count
        continue

print(count)
print(sum)
print(mid)




