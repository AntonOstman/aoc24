from collections import defaultdict, deque
from queue import PriorityQueue


def inside_map(node, map):

    if node[0] < len(map[0]) and node[0] >= 0 and node[1] < len(map) and node[1] >= 0:
        return True

    return False

def get_adj4(node, lines, prev_dir):

    adj = []
    x,y = node
    cur_letter = lines[y][x]
    for dx, dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        nx,ny = x + dx, y + dy
        if inside_map((nx, ny), lines): 
            letter = lines[ny][nx]
            if letter == '.' or letter == 'E':
                if (dx, dy) != prev_dir:
                    cost = 1000
                else:
                    cost = 0

                adj.append((cost, (nx, ny), (dx, dy)))

    return adj

def bfs(node, seen, lines, prev, dist):

    q = PriorityQueue()
    dir = (1,0)
    dist[node] = 0

    q.put((0, node, dir))

    while(not q.empty()):
        curr = q.get()
        # seen.add(curr)
        print(curr)
        cost, node, prev_dir = curr

        neighbours = get_adj4(node, lines, prev_dir)
        for cost, neighbour, dir in neighbours:
            alt = 1 + cost
            if neighbour not in dist or alt < dist[neighbour]:
                dist[neighbour] = alt
                prev[neighbour] = node
                q.put((cost, neighbour, dir))

f = open('test')

lines = f.read().splitlines()

graph = defaultdict(tuple)
dist = defaultdict(int)

end = None
start = None

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter == 'E':
            end = (x,y)
        if letter == 'S':
            seen = set()
            start = (x,y)
            bfs((x,y), seen, lines, graph, dist)

node = end
cost = 0
while(node != start):

    cost += dist[node]
    node = graph[node]


print(cost)

# print(graph)

f.close()
