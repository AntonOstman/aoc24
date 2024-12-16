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
            if letter == '.' or letter == 'E' or letter == 'S':
                if (dx, dy) != prev_dir:
                    cost = 1001
                else:
                    cost = 1

                adj.append((cost, (nx, ny), (dx, dy)))

    return adj

def djikstra(node,s_dir, seen, lines, prev, dist):

    q = PriorityQueue()
    dist[(node,s_dir)]= 0

    q.put((0, node, s_dir))
    seen = set()

    while(not q.empty()):
        curr = q.get()
        # print(curr)
        dist_cost, node, prev_dir = curr
        seen.add((node, prev_dir))

        neighbours = get_adj4(node, lines, prev_dir)
        for n_cost, neighbour, dir in neighbours:
            
            alt = n_cost + dist[(node, prev_dir)]

            # if (neighbour, dir) not in dist or alt < dist[(neighbour, dir)]:
            #     dist[(neighbour, dir)] = alt
            #     # prev[(neighbour,dir)].add((node, prev_dir))
            #     prev[neighbour] = {(node, prev_dir)}
            #     q.put((alt, neighbour, dir))
            # elif alt <= dist[neighbour]:
            #     dist[(neighbour, dir)] = alt
            #     prev[neighbour].add((node, prev_dir))
            #     q.put((alt, neighbour, dir))

            if (neighbour, dir) not in seen:
                dist[(neighbour, dir)] = alt
                prev[neighbour].add((node, prev_dir))
                q.put((alt, neighbour, dir))


                # print('replacing',neighbour, alt)

            # if (neighbour,dir) not in seen:
            #     # print('adding', neighbour, alt)
            #     dist[(neighbour, dir)] = alt
            #     prev[(neighbour)].add((node, prev_dir))
            #     q.put((alt, neighbour, dir))
            #
            #     seen.add((neighbour,dir))


f = open('test2')

lines = f.read().splitlines()

start_graph = defaultdict(set)
end_graph = defaultdict(set)

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

num =0

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        for adj in [(1,0), (-1,0), (0,1), (0,-1)]:
            if ((x,y), adj) in end_dist:
                if end_dist[((x,y),adj)] + start_dist[((x,y),(-adj[0],-adj[1]))] == start_dist[(end,(0,-1))]:
                    num+=1


print(num)

# print(graph)

f.close()
