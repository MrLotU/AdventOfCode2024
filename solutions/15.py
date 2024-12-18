test_input = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

with open('inputs/15.txt', 'r') as f:
    lines = f.read()

# lines = test_input
maze, instructions = lines.split('\n\n')
p2maze = maze.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.').split('\n')
instructions = instructions.replace('\n', '')
maze = maze.split('\n')
cols = [[row[x] for row in maze] for x in range(len(maze[0]))]
W = len(cols)
H = len(cols[0])

start = (0,0)
for x in range(W):
    for y in range(H):
        if cols[x][y] == '@':
            start = (x, y)

cols[start[0]][start[1]] = '.'
DIRS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

print('---- DAY 15 PART 1 ----')
current = start
for i in instructions:
    dx, dy = DIRS[i]
    cx, cy = current
    nx, ny = cx + dx, cy + dy

    n = cols[nx][ny]
    if n == '#':
        continue
    elif n == '.':
        current = (nx, ny)
        continue
    elif n == 'O':
        _n = n
        _nx, _ny = nx, ny
        movers = []
        while _n not in ('#', '.'):
            if _n == 'O':
                movers.append((_nx, _ny))
            _nx, _ny = _nx + dx, _ny + dy
            _n = cols[_nx][_ny]
        if _n == '#':
            continue
        else:
            for mover in movers:
                mx, my = mover
                nmx, nmy = mx + dx, my + dy
                cols[nmx][nmy] = 'O'
            cols[nx][ny] = '.'
            current = (nx, ny)

score = 0

for n in range(H):
    s = ''
    for i in range(W):
        s += cols[i][n]
        if cols[i][n] == 'O':
            score += n * 100 + i
    print(s)

print(score)
print('---- DAY 15 PART 2 ----')

cols = [[row[x] for row in p2maze] for x in range(len(p2maze[0]))]
W = len(cols)
H = len(cols[0])

start = (0,0)
for x in range(W):
    for y in range(H):
        if cols[x][y] == '@':
            start = (x, y)

cols[start[0]][start[1]] = '.'

current = start
for i in instructions:
    dx, dy = DIRS[i]
    cx, cy = current
    nx, ny = cx + dx, cy + dy

    n = cols[nx][ny]
    if n == '#':
        pass
    elif n == '.':
        current = (nx, ny)
        pass
    elif n in '[]':
        if i in '<>':
            _n = n
            _nx, _ny = nx, ny
            movers = []
            while _n not in '#.':
                if _n in '[]':
                    movers.append((_nx, _ny))
                _nx, _ny = _nx + dx, _ny + dy
                _n = cols[_nx][_ny]
            if _n == '#':
                pass
            else:
                for mover in movers[::-1]:
                    mx, my = mover
                    nmx, nmy = mx + dx, my + dy
                    cols[nmx][nmy] = cols[mx][my]
                cols[nx][ny] = '.'
                current = (nx, ny)
        else:
            def find_other_half(a,b):
                if cols[a][b] == '[':
                    return (a + 1, b)
                return (a - 1, b)
            checks = [(nx, ny), find_other_half(nx, ny)]
            movers = checks[:]
            can_move = True
            while len(checks) > 0 and can_move:
                next_checks = set()
                for cx, cy in checks:
                    _nx, _ny = cx + dx, cy + dy
                    _n = cols[_nx][_ny]
                    if _n == '#':
                        can_move = False
                    elif _n == '.':
                        continue
                    else:
                        a, b = (_nx, _ny), find_other_half(_nx, _ny)
                        next_checks.add(a)
                        next_checks.add(b)
                        if a not in movers:
                            movers.append(a)
                        if b not in movers:
                            movers.append(b)
                checks = list(next_checks)
            
            if not can_move:
                pass
            else:
                for mover in movers[::-1]:
                    mx, my = mover
                    nmx, nmy = mx + dx, my + dy
                    cols[nmx][nmy] = cols[mx][my]
                    cols[mx][my] = '.'

                cols[nx][ny] = '.'
                current = (nx, ny)

score = 0

for n in range(H):
    s = ''
    for i in range(W):
        s += cols[i][n]
        if cols[i][n] == '[':
            score += n * 100 + i
    print(s)

print(score)
