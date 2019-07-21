# Разбить строку data на группы по 3 числа и посчитать
# суммы каждого первого, второго и третьего.


data = """
0.00002640
23174.4902
0.61180654
0.00002599
8434.0130
0.21919999
0.00002000
52622.1944
1.05244388
0.00001599
13708.5678
0.21919999
0.00001500
100232.3673
1.50348550
"""

sdata = data.strip()
ssdata = sdata.split('\n')
print(ssdata)

summ_of_first_numbers = 0
for c in ssdata[::3]:
    summ_of_first_numbers = summ_of_first_numbers + float(c)
print('сумма 1 группы: ', summ_of_first_numbers)

summ_of_second_numbers = 0
for d in ssdata[1::3]:
    summ_of_second_numbers = summ_of_second_numbers + float(d)
print('сумма 2 группы: ', summ_of_second_numbers)

summ_of_third_numbers = 0
for e in ssdata[2::3]:
    summ_of_third_numbers = summ_of_third_numbers + float(e)
print('сумма 3 группы: ', summ_of_third_numbers)
