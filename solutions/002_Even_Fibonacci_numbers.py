'''
Задача 2

Каждый следующий элемент в последовательности Фибоначчи получается из
суммы двух предыдущих элементов. Первые 10 элементов последовательности:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

Для элементов последовательности Фибоначчи, которые не превышает четырех
миллионов найти сумму четных эелементов.
'''

limit = 4000000

n1 = 1
n2 = 2
s = 0
while n2 <= limit:
    if n2 % 2 == 0:
        s += n2
    temp = n1 + n2
    n1 = n2
    n2 = temp
print(s)
