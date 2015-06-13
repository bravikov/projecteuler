'''
Задача 15

По сетке 2 на 2 можно проложить 6 путей при условии, что начало пути в
верхнем левом углу, конец в нижнем правом, а двигаться можно только вниз
и вправо.

Найти количество путей в сетке 20 на 20.
'''
size = 20

grid = []

for y in range(size + 1):
    grid.append([])
    for x in range(size + 1):
        grid[y].append(1)

x = size
y = size
while x > 0 and y > 0:
    x -= 1
    y -= 1

    for x2 in range(size, x, -1):
        grid[y][x2] = grid[y + 1][x2]
        if x2 < size:
            grid[y][x2] += grid[y][x2 + 1]

    for y2 in range(size, y, -1):
        grid[y2][x] = grid[y2][x + 1]
        if y2 < size:
            grid[y2][x] += grid[y2 + 1][x]

    grid[y][x] = grid[y+1][x] + grid[y][x+1]

grid[size][size] = 0

for y in range(size + 1):
    for x in range(size + 1):
        w = len(str(grid[0][x]))
        print('%*i' % (w, grid[x][y]), end = '|')
    print()

print('Путей:', grid[0][0])
