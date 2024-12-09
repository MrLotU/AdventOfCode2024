import re

test_input = '''2333133121414131402'''

with open('inputs/9.txt', 'r') as f:
    line = f.read()

# line = test_input

print('---- DAY 9 PART 1 ----')

output = 0
groups = [(int(a), int(b)) for a,b in re.findall(r'(\d)(\d)', line)]
groups.append(((int(line[-1])), 0))
idx = 0
gidx = 0
ge_idx = len(groups) - 1
ge_left = groups[ge_idx][0]

while True:
    size, empty = groups[gidx]
    for i in range(size):
        output += gidx * idx
        idx += 1
    gidx += 1
    for i in range(empty):
        if ge_left > 0:
            output += ge_idx * idx
            idx += 1
            ge_left -= 1
        if ge_left == 0:
            ge_idx -= 1
            ge_left = groups[ge_idx][0]

    if ge_idx == gidx:
        for i in range(ge_left):
            output += gidx * idx
            idx += 1
        break

print(output)

print('---- DAY 9 PART 2 ----')

output = 0
groups = [(i, a, b) for i, (a, b) in enumerate(groups)]
idx = 0
gidx = 0
used = set()
revgroups = groups[::-1]

while len(used) < len(groups):
    _, size, empty = groups[gidx]
    if gidx not in used:
        for i in range(size):
            output += gidx * idx
            idx += 1
    else:
        idx += size
    used.add(gidx)
    gidx += 1
    rem = empty
    while rem > 0:
        try:
            fill = next(g for g in revgroups if g[0] not in used and g[1] <= rem)
            f_gidx, f_size, _ = fill
            used.add(f_gidx)
            rem -= f_size
            for i in range(f_size):
                output += f_gidx * idx
                idx += 1
        except StopIteration:
            idx += rem
            rem = 0

print(output)