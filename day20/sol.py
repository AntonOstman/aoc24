from collections import defaultdict, deque

def inside_map(node, map):

    if node[0] < len(map[0]) and node[0] >= 0 and node[1] < len(map) and node[1] >= 0:
        return True

    return False


def get_adj4(node, lines, seen, ghost_wall):

    adj = []
    x,y = node
    for dx, dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        nx,ny = x + dx, y + dy

        if inside_map((nx, ny), lines) and (nx,ny) not in seen:
            letter = lines[ny][nx]
            wall = letter == '#' and (nx,ny) != ghost_wall

            if not wall: 
                adj.append((nx, ny))

    return adj


def bfs(start, seen, prev, map, ghost_wall):

    q = deque()
    q.appendleft(start)

    while(len(q) > 0):
        node = q.pop()

        if node not in seen:
            seen.add(node)
            for neighbour in get_adj4(node, map, seen, ghost_wall):
                q.appendleft(neighbour)
                prev[neighbour] = node


f = open('input')

lines = f.read().strip().split("\n")
map = []

prev = defaultdict(tuple)
start = None
end = None
walls = []

for y, line in enumerate(lines):
    map.append([])
    for x, letter in enumerate(line):
        if letter == '#':
            walls.append((x,y))
        if letter == 'S':
            start = (x,y)
        if letter == 'E':
            end = (x,y)
        map[y].append(letter)

total = 0

prev = defaultdict(tuple)
node = end
bfs(start, set(), prev, lines, (-10,-10))

count = 0
while(node != start):
    node = prev[node]
    x,y = node
    count += 1
    map[y][x] = 'O'
first = count

count = 0
for wall in walls:
    prev = defaultdict(tuple)
    bfs(start, set(), prev, lines, wall)
    node = end
    while(node != start):
        node = prev[node]
        x,y = node
        count += 1

    if first - count >= 100:
        total += 1
    count = 0

print(total)
