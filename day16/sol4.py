
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
            if letter == '.' or letter == 'S' or letter == 'E':
                if (dx, dy) != prev_dir:
                    cost = 1001
                else:
                    cost = 1

                adj.append((cost, (nx, ny), (dx, dy)))

    return adj

def djikstra(node,s_dir, seen, lines, prev, dist):

    q = PriorityQueue()
    dist[node] = 0

    q.put((0, node, s_dir))

    while(not q.empty()):
        curr = q.get()
        # seen.add(curr)
        print(curr)
        cost, node, prev_dir = curr

        neighbours = get_adj4(node, lines, prev_dir)
        for cost, neighbour, dir in neighbours:
            alt = cost + dist[node]
            if neighbour not in dist or alt < dist[neighbour]:
                dist[neighbour,] = alt
                prev[neighbour] = (node, dir)
                q.put((cost, neighbour, dir))

f = open('input')

lines = f.read().splitlines()

start_graph = defaultdict(tuple)
end_graph = defaultdict(tuple)

start_dist = defaultdict(int)
end_dist = defaultdict(int)

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
            djikstra((x,y),(0,-1), seen, lines, end_graph, end_dist)
        if letter == 'S':
            seen = set()
            start = (x,y)
            djikstra((x,y),(1,0), seen, lines, start_graph, start_dist)

node = end
cost = 0

dirmap = {(1,0) : '>', (-1,0) : '<', (0,-1):'^', (0,1):'v'}
num = 0

# while(node != start):
#
#     num+=1
#     # print(dist[node])
#     cost += dist[node]
#     node, dir = graph[node]
#     print(node)
#     map[node[1]][node[0]] = dirmap[dir]

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if end_dist[(x,y)] + start_dist[(x,y)] == start_dist[end]:
            num+=1

for i in map:
    print(i)

# print(dist[end])
# print(cost)
print(start_dist[end])
print(num)

# print(graph)

f.close()

