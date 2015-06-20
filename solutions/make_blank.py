'''
Создает файл-заготовку для решения задачи.

Вызов:
    python3 make_blank.py <номер задачи> <название задачи>

Например:
    python3 make_blank.py 1 Multiples of 3 and 5
'''

import sys

if len(sys.argv) < 3:
    print('Пример вызова:')
    print('    python3 make_blank.py <номер задачи> <название задачи>')
    exit()

problem_number = int(sys.argv[1])
problem_title = '_'.join(sys.argv[2:])

filename = '%03i_%s.py' % (problem_number, problem_title)

content = """'''
Задача %i



Найти 
'''



answer = 0

print('Ответ:', answer)

""" % (problem_number)

with open(filename, 'x') as f:
    f.write(content)
    print(filename)
