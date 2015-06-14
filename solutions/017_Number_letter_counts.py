'''
Задача 17

Если числа от 1 до 5 записать прописью: one, two, three,
four, five, тогда количество букв будет равно 3 + 3 + 5 + 4 + 4 = 19.

Найти сумму букв для чисел от 1 до 1000 (one hundred) включительно.

Примечание: не следуется считать пробелы и дефисы.
Например, 342 (three hundred and forty-two) содержит 23 буквы, а
115 (one hundred and fifteen) содержит 20 букв. Требуется использовать
слово "and" при записи чисел прописью в соответствии с Британским
упортеблением.
'''

limit = 1000

def in_words(i):
    w1 = (
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
    )

    w2 = (
        'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety'
    )
    
    if i > 1000:
        return 'unknown'

    if i == 1000:
        return 'one thousand'

    s = ''

    h = i // 100
    if h > 0:
        s = w1[h] + ' hundred'

    t = i % 100
    if t > 0:
        if h > 0:
            s += ' and '

        if t < 20:
            s += w1[t]
        else:
            s += w2[t // 10 - 2]

            o = t % 10
            if o > 0:
                s += '-' + w1[o]

    return s


sm = 0
for i in range(1, limit + 1):
    w = in_words(i)
    wc = w.replace(' ', '').replace('-', '')
    lwc = len(wc)
    sm += lwc
    print(i, w, len(wc))
print('Резульат:', sm)
