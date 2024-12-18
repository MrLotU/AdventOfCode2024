import re
from collections import defaultdict

test_input = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''

with open('inputs/14.txt', 'r') as f:
    lines = f.read()

W, H = 101, 103
# lines, W, H = test_input, 11, 7
lines = lines.split('\n')

print('---- DAY 14 PART 1 ----')
grid = defaultdict(lambda: 0)
qs = defaultdict(lambda: 0)
def quadrant(x, y):
    if x < W // 2:
        if y < H // 2:
            return 0
        elif y >= H // 2 + 1:
            return 2
        return -1
    elif x >= W // 2 + 1:
        if y < H // 2:
            return 1
        elif y >= H // 2 + 1:
            return 3
        return -1
    return -1


for line in lines:
    sx, sy, dx, dy = [int(t) for t in re.findall(r'-?\d+', line)]
    nx, ny = sx + dx * 100, sy + dy * 100
    nx, ny = nx % W, ny % H
    qs[quadrant(nx, ny)] += 1
    grid[(nx, ny)] += 1

val = 1
for i in range(4):
    val *= qs[i]

print(val)

print('---- DAY 14 PART 2 ----')
i = 0 # 13580000
while True:
    if i % 10_000 == 0:
        print(i)
    grid = defaultdict(lambda: 0)
    for line in lines:
        sx, sy, dx, dy = [int(t) for t in re.findall(r'-?\d+', line)]
        nx, ny = sx + dx * i, sy + dy * i
        nx, ny = nx % W, ny % H
        qs[quadrant(nx, ny)] += 1
        grid[(nx, ny)] += 1
    should_skip = True
    for x in range(W):
        for y in range(H):
            found_all = True
            if (x, y) not in grid:
                continue
            for n in range(4):
                if (x + n, y + n) in grid and (x -n, y + n) in grid:
                    pass
                else:
                    found_all = False
            if found_all:
                should_skip = False
    if should_skip:
        i += 1
        continue
    for y in range(H):
        l = ''
        for x in range(W):
            if (x,y) in grid and grid[(x, y)] != 0:
                l += f'{grid[(x,y)]}'
            else:
                l += '.'
        print(l)
    print(i,'\n\n')
    i += 1
    _ = input()

