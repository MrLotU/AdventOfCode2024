import re
from collections import defaultdict
from itertools import combinations

test_input = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

with open('inputs/8.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')
cols = [[row[x] for row in lines] for x in range(len(lines[0]))]

print('---- DAY 8 PART 1 ----')

coords_by_freqency = defaultdict(list)
coords = set()
for x in range(len(cols)):
    for y in range(len(cols[0])):
        if cols[x][y] != '.':
            coords_by_freqency[cols[x][y]].append((x,y))

antinodes = set()

for freq, coords in coords_by_freqency.items():
    combos = combinations(coords, 2)
    for (xa, ya), (xb, yb) in combos:
        dx, dy = xa - xb, ya - yb

        weirds = [(xa + dx, ya + dy), (xb - dx, yb - dy)]
        for nx, ny in weirds:
            if nx < 0 or ny < 0 or nx >= len(cols) or ny >= len(cols[0]):
                continue
            antinodes.add((nx, ny))

print(len(antinodes))

print('---- DAY 8 PART 2 ----')

antinodes = set()

for freq, coords in coords_by_freqency.items():
    combos = combinations(coords, 2)
    for (xa, ya), (xb, yb) in combos:
        dx, dy = xa - xb, ya - yb
        weirds = [(xa + dx, ya + dy), (xb - dx, yb - dy)]
        for nx, ny in [(xa, ya), (xb, yb)]:
            if nx < 0 or ny < 0 or nx >= len(cols) or ny >= len(cols[0]):
                continue
            antinodes.add((nx, ny))
        (nx, ny), (nnx, nny) = weirds
        W = len(cols)
        H = len(cols[0])
        while (nx >= 0 and ny >= 0 and nx < W and ny < H) or (nnx >= 0 and nny >= 0 and nnx < W and nny < H):
            if nx >= 0 and ny >= 0 and nx < W and ny < H:
                antinodes.add((nx, ny))
            if nnx >= 0 and nny >= 0 and nnx < W and nny < H:
                antinodes.add((nnx, nny))
            
            nx, ny = nx + (dx), ny + (dy)
            nnx, nny = nnx - (dx), nny - (dy)

print(len(antinodes))

