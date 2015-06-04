'''
Задача 3

5, 7, 13, 29 - это простые множители числа 13195.

Найти наибольший простой множитель числа 600851475143.
'''

#n = 13195
n = 600851475143

factor_limit = int(n ** 0.5)
max_factor = 0
with open('простые_числа', 'r') as f:
    for line in f:
        factor = int(line)
        if factor > factor_limit:
            break
        if n % factor == 0:
            max_factor = factor
print(max_factor)
