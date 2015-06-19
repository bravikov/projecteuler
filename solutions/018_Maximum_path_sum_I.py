'''
Задача 18

Если пройти треугольник

   3
  7 4
 2 4 6
8 5 9 3

сверху вниз по соседним числам, то можно найти такой ряд чисел, который
дает максимальную сумму: 3 + 7 + 4 + 9 = 23.

Найти максимальную сумму в следующем треугольнике:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

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
triangle = '''
              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''


triangle = shortcuts.grid(triangle)

sums = []
row_index = 0
for row in triangle:
    row_sums = []
    value_index = 0
    for value in row:
        value_sums = []
        previous_row_index = row_index - 1
        previous_left_value_index = value_index - 1
        previous_right_value_index = value_index

        if previous_row_index < 0:
            value_sums.append(value)
        else:
            previous_sums = []
            if previous_left_value_index >= 0:
                s = sums[previous_row_index][previous_left_value_index]
                previous_sums += s
            if previous_right_value_index < len(sums[previous_row_index]):
                s = sums[previous_row_index][previous_right_value_index]
                previous_sums += s
            for s in previous_sums:
                value_sums.append(s + value)
        if len(value_sums) > 0:
            row_sums.append(value_sums)
        value_index += 1
    sums.append(row_sums)
    row_index += 1

max_sum = 0
for row in sums:
    for value in row:
        for s in value:
            max_sum = max(max_sum, s)

print(max_sum)
