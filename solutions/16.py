import heapq
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

test_input = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''

with open('inputs/16.txt', 'r') as f:
    lines = f.read()

# lines = test_input
lines = lines.split('\n')
cols = [[row[x] for row in lines] for x in range(len(lines[0]))]
W = len(cols)
H = len(cols[0])

start = end = (0,0)
for x in range(W):
    for y in range(H):
        if cols[x][y] == 'S':
            start = (x, y)
        if cols[x][y] == 'E':
            end = (x, y)

DIR_IDX = 1
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def spinning_dijkstra(graph, starts):
    distances = defaultdict(lambda: float('inf'))
    queue = []
    for start in starts:
        distances[start] = 0
        x,y,f = start
        queue.append((0, (x,y), f))

    while queue:
        distance, node, facing = heapq.heappop(queue)

        for i, (dx, dy) in enumerate(DIRS):
            cost = 1001
            if i == facing:
                cost = 1

            # Fucking p2
            if cost == 1001 and distances[(x, y, i)] > distance + 1000:
                distances[(x, y, i)] = distance + 1000

            x, y = node
            nx, ny = x + dx, y + dy
            if graph[nx][ny] == '#':
                continue
            nd = distance + cost
            if nd < distances[(nx, ny, i)]:
                distances[(nx, ny, i)] = nd
                heapq.heappush(queue, (nd, (nx, ny), i))

    return dict(distances)            

print('---- DAY 16 PART 1 ----')

costs_from_start = spinning_dijkstra(cols, [start + (1,)])

shortest = 100_000_000
for i in range(4):
    shortest = min(costs_from_start.get(end + (i,), 100_000_000), shortest)
print(shortest)

print('---- DAY 16 PART 2 ----')

costs_from_end = spinning_dijkstra(cols, [end + (i,) for i in range(4)])
good_seats = set()
for x in range(W):
    for y in range(H):
        for d in range(4):
            flip_d = (d + 2) % 4
            fs = (x, y, d)
            fe = (x, y, flip_d)
            if fs in costs_from_start and fe in costs_from_end:
                if costs_from_start[fs] + costs_from_end[fe] == shortest:
                    good_seats.add((x, y))

print(len(good_seats))

