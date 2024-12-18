from collections import defaultdict
import heapq

test_input = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''

with open('inputs/18.txt', 'r') as f:
    lines = f.read()

H = W = 70
drops = 1024
# lines, H, W, drops = test_input, 6, 6, 12
lines = lines.split('\n')

coords = [(int(x), int(y)) for x, y in [l.split(',') for l in lines]]
coords_lookup = set()
for i in range(drops):
    coords_lookup.add(coords[i])
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

print('---- DAY 18 PART 1 ----')

def dijkstra(graph, start, lu):
    distances = defaultdict(lambda: float('inf'))
    queue = []
    distances[start] = 0
    queue.append((0, start))

    while queue:
        distance, node = heapq.heappop(queue)
        
        for dx, dy in DIRS:
            x, y = node
            nx, ny = x + dx, y + dy

            if (nx, ny) in lu or (nx, ny) not in graph:
                continue
            nd = distance + 1
            if nd < distances[(nx, ny)]:
                distances[(nx, ny)] = nd
                heapq.heappush(queue, (nd, (nx, ny)))
    
    return dict(distances)

g = set()
for x in range(W + 1):
    for y in range(H + 1):
        g.add((x, y))

result = dijkstra(g, (0,0), coords_lookup)
goal = (H, W)

print(result[goal])

print('---- DAY 18 PART 2 ----')

for i in range(len(coords) - drops - 1):
    idx = i + drops + 1
    coords_lookup.add(coords[idx])

    res = dijkstra(g, (0,0), coords_lookup)
    # print(res[goal])
    if goal not in res:
        x, y = coords[idx]
        print(f'{x},{y}')
        break
