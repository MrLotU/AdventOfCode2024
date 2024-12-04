import re

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open("inputs/4.txt", "r") as f:
    lines_raw = f.read()

# lines_raw = test_input
lines = lines_raw.split("\n")
mod = len(lines[0])
cols = [[row[x] for row in lines] for x in range(mod)]

print("---- DAY 4 PART 1 ----")

CHECKS = [
    [(1, 0), (2, 0), (3, 0)],
    [(-1, 0), (-2, 0), (-3, 0)],
    [(0, 1), (0, 2), (0, 3)],
    [(0, -1), (0, -2), (0, -3)],
    [(1, 1), (2, 2), (3, 3)],
    [(1, -1), (2, -2), (3, -3)],
    [(-1, 1), (-2, 2), (-3, 3)],
    [(-1, -1), (-2, -2), (-3, -3)],
]

final = 0
for x in range(mod):
    for y in range(len(cols)):
        if cols[y][x] != 'X':
            continue
        for check in CHECKS:
            l = 'X'
            for dx,dy in check:
                nx, ny = x + dx, y + dy
                if nx >= mod or nx < 0 or ny >= len(cols) or ny < 0:
                    break
                l += cols[ny][nx]
            if l == 'XMAS':
                final += 1

print(final)

print("---- DAY 4 PART 2 ----")

CHECKS = [
    [(-1,-1), (1,1)],
    [(1, -1), (-1, 1)]
]

final = 0
for x in range(mod):
    for y in range(len(cols)):
        if cols[y][x] != 'A':
            continue
        masses = 0
        for check in CHECKS:
            l = ''
            for dx, dy in check:
                nx, ny = x + dx, y + dy
                if nx >= mod or nx < 0 or ny >= len(cols) or ny < 0:
                    break
                l += cols[ny][nx]
            if l == 'MS' or l == 'SM':
                masses += 1
        if masses == 2:
            final += 1

print(final)
