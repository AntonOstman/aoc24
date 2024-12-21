from collections import defaultdict, deque

DIST = 20
LIMIT = 100

f = open('input')

def inside_map(node, map):

    if node[0] < len(map[0]) and node[0] >= 0 and node[1] < len(map) and node[1] >= 0:
        return True

    return False


def get_adj4(node, lines, seen):

    adj = []
    x,y = node
    for dx, dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        nx,ny = x + dx, y + dy

        if inside_map((nx, ny), lines) and (nx,ny) not in seen:
            letter = lines[ny][nx]
            wall = letter == '#'

            if not wall: 
                adj.append((nx, ny))

    return adj

def backtrack(start,end,prev):
    node = end
    count = 0
    while(node != start):
        node = prev[node]
        if not node:
            return 0
        x,y = node
        count += 1
        map[y][x] = 'O'
    return count

def bfs(start, seen, prev, map):

    q = deque()
    q.appendleft(start)

    while(len(q) > 0):
        node = q.pop()

        if node not in seen:
            seen.add(node)
            for neighbour in get_adj4(node, map, seen):
                q.appendleft(neighbour)
                prev[neighbour] = node



lines = f.read().strip().split("\n")
map = []

prev = defaultdict(tuple)
start = None
end = None
road = []

cheat_pair = list()

for y, line in enumerate(lines):
    map.append([])
    for x, letter in enumerate(line):
        if letter in '.SE':
            road.append((x,y))
        if letter == 'S':
            start = (x,y)
        if letter == 'E':
            end = (x,y)
        map[y].append(letter)

visited = set()
for sx,sy in road: 
    for ex,ey in road:
        dist = abs(sx - ex) + abs(sy - ey)
        if dist <= DIST:
            cheat_pair.append((sx,sy, ex,ey, dist))


total = 0

prev = defaultdict(tuple)

bfs(start, set(), prev, lines)

first_run = backtrack(start,end,prev)

for sx,sy,ex,ey,dist in cheat_pair:
    if backtrack((sx,sy),(ex,ey),prev) - dist >= LIMIT:
        total += 1


print(total)
