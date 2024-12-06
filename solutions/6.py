import re
from itertools import product

test_input = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

with open('inputs/6.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')
cols = [[row[x] for row in lines] for x in range(len(lines[0]))]

directions = ['U', 'R', 'D', 'L']
dir_idx = 0
offset = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0)
}
seen = set()
startrow = next(i for i, x in enumerate(cols) if '^' in x)
startcol = next(i for i, x in enumerate(cols[startrow]) if x == '^')
x, y = startrow, startcol
print('---- DAY 6 PART 1 ----')

while True:
    dx, dy = offset[directions[dir_idx]]
    nx, ny = x + dx, y + dy
    if nx < 0 or ny < 0 or nx >= len(lines[0]) or ny >= len(cols):
        break
    v = cols[nx][ny]
    if v == '#':
        dir_idx = (dir_idx + 1) % len(directions)
    else:
        seen.add((nx, ny))
        x, y = nx, ny
        
print(len(seen))

print('---- DAY 6 PART 2 ----')

infinity = 0
for blocked in seen:
    if blocked == (startrow, startcol):
        continue
    
    turned = set()
    x, y = startrow, startcol
    dir_idx = 0
    while True:
        dx, dy = offset[directions[dir_idx]]
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= len(lines[0]) or ny >= len(cols):
            break
        v = cols[nx][ny]
        if v == '#' or (nx, ny) == blocked:
            dir_idx = (dir_idx + 1) % len(directions)
            if (nx, ny, dir_idx) in turned:
                infinity += 1
                break
            turned.add((nx, ny, dir_idx))
        else:
            x, y = nx, ny

print(infinity)