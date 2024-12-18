import re
from collections import deque

test_input = '''EEEEE
EXXXX
EEEEE
EXXXX
EEEEE'''

with open('inputs/12.txt', 'r') as f:
    lines = f.read()

lines = test_input
lines = lines.split('\n')
cols = [[row[x] for row in lines] for x in range(len(lines[0]))]
W = len(cols)
H = len(cols[0])

DIRS = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
seen = set()

total_price = 0
p2_price = 0

def find_and_calc(x, y):
    letter = cols[x][y]
    seen.add((x, y))
    total_area = 1
    total_perimeter = 0
    side_segments = []
    to_scan = deque()
    for s, (dx, dy) in DIRS.items():
        to_scan.append((x + dx, y + dy, s))
    
    while len(to_scan) > 0:
        nx, ny, s = to_scan.popleft()
        if (nx < 0 or nx >= W or ny < 0 or ny >= H) or (cols[nx][ny] != letter):
            total_perimeter += 1
            side_segments.append((nx, ny, s))
            continue
        if (nx, ny) in seen:
            continue
        seen.add((nx, ny))
        total_area += 1
        for s, (dx, dy) in DIRS.items():
            to_scan.append((nx + dx, ny + dy, s))
    
    discounted_perimiter = 0
    # print(letter, side_segments)
    while len(side_segments) > 0:
        x, y, s = side_segments.pop()
        relevant = y if s in ['U', 'D'] else x
        sortval = x if s in ['U', 'D'] else y
        sort_idx = 0 if s in ['U', 'D'] else 1
        rel_idx = 1 if s in ['U', 'D'] else 0
        segments_same_side = [(a, b, c, i) for i, (a,b,c) in enumerate(side_segments) if c == s]
        # sorted_segs = sorted(segments_same_side, key=lambda t: abs(t[sort_idx] - sortval))
        # print(letter, (x, y, s), sorted_segs)
        removables = []
        dis = 1
        while True:
            # if dis
            # seg = 
            if seg[rel_idx] != relevant:
                break
            removables.append(seg[-1])
        for i in sorted(removables, reverse=True):
            side_segments.pop(i)
        discounted_perimiter += 1

    print(letter, total_area, discounted_perimiter)
    if total_area == 1:
        print(nx, ny)
    # print(letter, total_area, total_perimeter)
    return total_area * total_perimeter, total_area * discounted_perimiter


for x in range(W):
    for y in range(H):
        if (x,y) in seen:
            continue
        p1, p2 = find_and_calc(x, y)
        total_price += p1
        p2_price += p2
        # p2_price += find_and_calc(x, y)

print('---- DAY 12 PART 1 ----')
print(total_price)

print('---- DAY 12 PART 2 ----')
print(p2_price)