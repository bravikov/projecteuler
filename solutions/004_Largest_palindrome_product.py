'''
Задача 4

Числовые палиндромы читаюся в обоих направлениях одинаково. Наибольший
палиндром, получаемый из произведения двух дузнычных чисел,
равен 9009 (91 * 99 = 9009).

Найти наибольший полиндром, получаемый из произведения двух трехзначных
чисел.
'''

mn = 100
mx = 1000

# Возвращает True, если строка является палиндромом.
def is_palindrome(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

max_palindrome = 0
for i in range(mn, mx):
    for j in range(i, mx):
        n = i * j
        if is_palindrome(str(n)):
            if max_palindrome < n:
                max_palindrome = n
                print(i, '*', j, '=',  n)
