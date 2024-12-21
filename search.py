from collections import defaultdict, deque
from copy import copy
import queue

f  = open("test")

lines = f.read().splitlines()

def inside_map(node, map):

    if node[0] < len(map[0]) and node[0] >= 0 and node[1] < len(map) and node[1] >= 0:
        return True

    return False


def get_adj8(node, lines):
    adj = []
    x,y = node
    cur_letter = lines[y][x]
    for dx, dy in [(1,0), (-1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1),(-1,-1)]:
        nx,ny = x + dx, y + dy
        if inside_map((nx, ny), lines): 
            letter = lines[ny][nx]
            if letter == cur_letter:
                adj.append((nx, ny))

    return adj

def get_adj4(node, lines):

    adj = []
    x,y = node
    cur_letter = lines[y][x]
    for dx, dy in [(1,0), (-1,0), (0,-1), (0,1)]:
        nx,ny = x + dx, y + dy
        if inside_map((nx, ny), lines): 
            letter = lines[ny][nx]
            if letter == cur_letter:
                adj.append((nx, ny))

    return adj



def dfs(node, seen, lines, graph):

    if node not in seen:
        seen.add(node)
        for n in get_adj8(node, lines):
            graph[node] = n
            dfs(n,seen,lines, graph)


def bfs(node, seen, lines, graph):

    q = deque()
    q.appendleft(node)

    while(len(q) > 0):
        curr = q.pop()
        if curr not in seen:
            seen.add(curr)
            neighbours = get_adj8(curr, lines)
            for neighbour in neighbours:
                graph[curr] = neighbour
                if neighbour not in seen:
                    q.append(neighbour)



g = defaultdict(set)
blobs = defaultdict(set)
for y in range(len(lines)):
    for x in range(len(lines)):
        if (x,y) not in g:
            seen = set()
            bfs((x,y), seen, lines, g)
            letter = lines[y][x]
            blobs[letter] = seen

cur_min = float('inf')
for key, values in blobs.items():

    map  = copy([['.' for _ in range(10)] for _ in range(10)])

    for blob in values:
        x,y = blob
        map[y][x] = key

    # print("".join(map))
    str_map = ""
    for y in range(len(map)):
        print(str_map.join(map[y]))
    print('='*10)

    # print("".join(y for x in map for y in x))


# print(g)


f.close()
