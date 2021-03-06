'''
Задача 14

Сиракузкая последовательность чисел получается следующим образом: берём
любое натуральное число n. Если оно чётное, то делим его на 2, а если
нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1). Над
полученным числом выполняем те же самые действия, и так далее.

Существует гипотеза Коллатца, которая утверждает, что какое бы начальное
число не было бы взято, рано или поздно получиться еденица.

Для начального числа 13 получается последовательность из 10 чисел:
    13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

Найти начальное число, которое меньше миллиона и из которого получается
наиболее длиинная последовательность.
'''

limit = 1000000

best_starting_number = 0
max_c = 0

for sn in range(2, limit):
    n = sn
    c = 0
    while n != 1:
        c += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

    print(sn, c)

    if max_c < c:
        max_c = c
        best_starting_number = sn

print(best_starting_number, 'длина последовательности:', max_c)
