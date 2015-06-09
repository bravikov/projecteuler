'''
Задача 12

Последовательность треугольных чисел получается сложением натуральных
чисел. Так седьмое треугольное число равно 1+2+3+4+5+6+7 = 28.
Первые десять треугольных чисел:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55.

Список множителей для первых семи треугольных чисел:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

Число 28 - это первое треугольное число, которое имеет более пяти
делителей.

Найти первое треугольное число, которое имеет более 500 делителей.
'''

limit = 500

#debug = True
debug = False

# Получить список простых чисел
primes = []
with open('простые_числа', 'r') as f:
    for line in f:
        primes.append(int(line))

n = 1
t_n = 1
while True:
    if debug:
        print(t_n, '=', end = ' ')
    have_divisor = False
    k = t_n
    p = 0
    c = 0
    divisors_count = 1
    have_divisor = False # Используется при отладке
    # Перебрать делители
    while k >= primes[p]:
        prime = primes[p]
        if k % prime == 0:
            k //= prime
            c += 1
            if have_divisor:
                if debug:
                    print('*', end = ' ')
            have_divisor = True
            if debug:
                print(prime, end = ' ')
        else:
            divisors_count *= c + 1
            c = 0
            p += 1

    if c > 0:
        divisors_count *= c + 1

    if debug:
        print('делителей:', divisors_count)

    if divisors_count > limit:
        print('Число', t_n, 'имеет', divisors_count, 'делителей')
        break
    
    n += 1
    t_n += n
