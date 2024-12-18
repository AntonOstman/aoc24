import sys
from collections import defaultdict, deque
sys.setrecursionlimit(100000000)

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


for y, line in enumerate(lines):
    if y == limit:
        break
    x,y = line.split(",")
    x,y = int(x), int(y)

    map[y][x] = '#'

graph = defaultdict(set)
prev = defaultdict(tuple)

bfs((0,0),map,set(), prev)

cur_node = (size - 1,size - 1)
steps = 0
while(cur_node != (0,0)):
    print(cur_node)
    map[cur_node[1]][cur_node[0]] = 'O'
    cur_node = prev[cur_node]
    steps += 1


for i in map:
    print(i)

print(steps)

f.close()
