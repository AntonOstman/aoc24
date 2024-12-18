from collections import defaultdict, deque

test = False

if test:
    f = open("test")
else:
    f = open("input")

lines = f.read().split("\n")[0:-1]

total = 0
graph = defaultdict(set)

def inside_map(node, map):

    if node[0] < len(map[0]) and node[0] >= 0 and node[1] < len(map) and node[1] >= 0:
        return True

    return False

def get_adj4(node, lines, visited):

    adj = []
    x,y = node
    for dx, dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        nx,ny = x + dx, y + dy
        if inside_map((nx, ny), lines): 
            letter = lines[ny][nx]
            if (nx,ny) in visited:
                continue
            if letter != '#':
                adj.append((nx, ny))

    return adj


def bfs(node, map, seen, prev):

    q = deque()
    q.append(node)

    while(len(q) > 0):
        curr = q.pop()
        if curr not in seen:
            seen.add(curr)
            neighbours = get_adj4(curr, map, seen)
            for neighbour in neighbours:
                print(curr,neighbours)
                q.appendleft(neighbour)
                prev[neighbour] = curr


def get_backtrack(prev):
    cur_node = (size - 1,size - 1)
    locs = set()
    while(cur_node != (0,0)):
        locs.add(cur_node)
        cur_node = prev[cur_node]

    return locs


map = []
if test:
    size = 6 + 1
    limit = 12
else:
    size = 70 + 1
    limit = 1024 

for y in range(size):
    map.append([])
    for x in range(size):
        map[y].append(".")


prev = defaultdict(tuple)

for y, line in enumerate(lines):
    x,y = line.split(",")
    x,y = int(x), int(y)
    
    map[y][x] = '#'
    first = False
    if prev and (x,y) in get_backtrack(prev):
        first = True

    prev = defaultdict(tuple)
    bfs((0,0),map,set(), prev)
    second = False
    if not prev[(70,70)]:
        second = True

    if first and second:
        print('blocking is',x,y)
        break

steps = 0

print(steps)

f.close()
