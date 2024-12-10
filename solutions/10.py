import re

test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

with open("inputs/10.txt", "r") as f:
    lines = f.read()

# lines = test_input
lines = lines.split("\n")
cols = [[int(row[x]) for row in lines] for x in range(len(lines[0]))]
W = len(cols)
H = len(cols[0])
print("---- DAY 10 PART 1 ----")

DIRS = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}


def pathfind(x, y):
    reached = set()
    trails = 0
    val = cols[x][y]
    if val == 9:
        return set([(x, y)]), 1
    for dx, dy in DIRS.values():
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
        if cols[nx][ny] == val + 1:
            p1, p2 = pathfind(nx, ny)
            reached = reached.union(p1)
            trails += p2
    return reached, trails


scores = 0
p2_scores = 0

for y in range(H):
    for x in range(W):
        if cols[x][y] == 0:
            p1, p2 = pathfind(x, y)
            scores += len(p1)
            p2_scores += p2

print(scores)

print("---- DAY 10 PART 2 ----")
print(p2_scores)
