'''
Задача 21

Пусть d(n) - это сумма собственных делителей числа n.

Собственный делитель - это любой положительный делитель натурального
числа, не совпадающий с самим этим числом.

Если d(a) = b и d(b) = a, где a ≠ b, тогда a и b - это дружественные
числа.

Найти сумму всех дружественных чисел до 10000.
'''

limit = 10000

# Возвращает список собственных делителей числа n.
def divisors(n):
    d = []
    for i in range(1, int(n) // 2 + 1):
        if n % i == 0:
            d.append(i)
    return(d)

sums = []
for n in range(1, limit):
    s = sum(divisors(n))
    sums.append(s)

amicable_numbers = set()
print('Пары дружественных чисел:')
for i in range(limit - 1):
    a = i + 1
    d_a = sums[i]
    if d_a < limit:
        b = d_a
        d_b = sums[b - 1]
        if a != b and d_a == b and d_b == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
            print(a, b)

answer = sum(amicable_numbers)
print('Ответ:', answer)
