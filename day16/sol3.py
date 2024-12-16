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
                    cost = 1001
                else:
                    cost = 1

                adj.append((cost, (nx, ny), (dx, dy)))

    return adj

def djikstra(node, seen, lines, prev, dist):

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
            alt = cost + dist[node]
            if neighbour not in dist or alt < dist[neighbour]:
                dist[neighbour] = alt
                prev[neighbour] = (node, dir)
                q.put((cost, neighbour, dir))

f = open('test')

lines = f.read().splitlines()

end_graph = defaultdict(tuple)
start_graph = defaultdict(tuple)

end_dist = defaultdict(int)
start_dist = defaultdict(int)
dist = defaultdict(int)

end = None
start = None
map = []


for y, line in enumerate(lines):
    map.append([])
    for x, letter in enumerate(line):
        map[y].append(letter)
        if letter == 'E':
            end = (x,y)
            seen = set()
            djikstra((x,y), seen, lines, end_graph, end_dist)
        if letter == 'S':
            seen = set()
            start = (x,y)
            djikstra((x,y), seen, lines, start_graph, start_dist)

node = end
cost = 0

dirmap = {(1,0) : '>', (-1,0) : '<', (0,-1):'^', (0,1):'v'}
num = 0

seen = set()

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if end_dist[(x,y)] + start_dist[(x,y)] == end_dist[start]:
            seen.add((x,y))
            # num += 1
        

# while(node != start):
#
#     num+=1
#     # print(dist[node])
#     cost += dist[node]
#     node, dir = graph[node]
#     print(node)
#     map[node[1]][node[0]] = dirmap[dir]

for i in map:
    print(i)

# print(dist[end])
# print(cost)
print(dist[end])
print(len(seen))

# print(graph)

f.close()
