'''
Задача 67

Если пройти треугольник

   3
  7 4
 2 4 6
8 5 9 3

сверху вниз по соседним числам, то можно найти такой ряд чисел, который
дает максимальную сумму: 3 + 7 + 4 + 9 = 23.

Найти максимальную сумму в треугольнике, который находиться в файле
p067_triangle.txt.

Примечание: эта задача - усложненный вариант задачи 18. Здесь невозможно
перебрать все пути для решения задачи, так как их 2^99. Если проверять
10^12 путей в секунду, то полный перебор займет 20 миллиардов лет.

'''

import shortcuts

"""
triangle = '''
       3
      7 4
     2 4 6
    8 5 9 3
'''
"""

triangle = ''
with open('p067_triangle.txt', 'r') as f:
    for line in f:
        triangle += line

triangle = shortcuts.grid(triangle)
print(triangle)

previous_sums = []
current_sums = []
row_count = 0
for row in triangle:
    current_sums.clear()
    value_index = 0
    for value in row:
        value_sums = []
        previous_left_value_index = value_index - 1
        previous_right_value_index = value_index

        if len(previous_sums) == 0:
            value_sums.append(value)
        else:
            t = []
            if previous_left_value_index >= 0:
                s = previous_sums[previous_left_value_index]
                t.append(s)
            if previous_right_value_index < len(previous_sums):
                s = previous_sums[previous_right_value_index]
                t.append(s)
            for s in t:
                value_sums.append(s + value)
        if len(value_sums) > 0:
            current_sums.append(max(value_sums))
        value_index += 1
    previous_sums = list(current_sums)

    print(row_count, previous_sums)
    row_count += 1
    
max_sum = 0
for value in current_sums:
    max_sum = max(max_sum, value)

print('Результат:', max_sum)
