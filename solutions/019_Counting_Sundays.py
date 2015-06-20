'''
Задача 19

Найти количество воскрестных дней, приходящихся на первый день месяца в
20 веке (с 1 января 1901 по 31 декабря 2000).
'''

import datetime

first_date = datetime.date(1901, 1, 1)
last_date = datetime.date(2000, 12, 31)

current_date = first_date
one_day = datetime.timedelta(days = 1)
sundays_count = 0
sunday = 6
while current_date <= last_date:
    if current_date.day == 1 and current_date.weekday() == sunday:
        sundays_count += 1
    current_date += one_day

print('Результат:', sundays_count)
