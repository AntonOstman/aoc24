from collections import defaultdict
from copy import copy
f = open("input")

lines = f.read().split("\n")[0:-1]

total = 0
graph = defaultdict(set)

def get_adj(pos, map):
    adj = []

    if pos[0] + 1 < len(lines[0]) and int(map[pos[1]][pos[0] + 1]) == int(map[pos[1]][pos[0]]) + 1:
        adj.append((pos[0] + 1, pos[1]))

    if pos[1] + 1 < len(lines) and int(map[pos[1] + 1][pos[0]]) == int(map[pos[1]][pos[0]]) + 1:
        adj.append((pos[0], pos[1] + 1))

    if pos[0] - 1 >= 0 and int(map[pos[1]][pos[0] - 1]) == int(map[pos[1]][pos[0]]) + 1:
        adj.append((pos[0] - 1, pos[1]))

    if pos[1] - 1 >= 0 and int(map[pos[1] - 1][pos[0]]) == int(map[pos[1]][pos[0]]) + 1:
        adj.append((pos[0], pos[1] - 1))

    return adj

def dfs(node, map, visited, graph):
    global total
    if node not in visited:
        visited.add(node)
        if map[node[1]][node[0]] == '9':
            total += 1

        for neighour in get_adj(node, map):
            graph[node].add(neighour)
            dfs(neighour, map, copy(visited), graph)

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter == '0':
            dfs((x,y), lines, set(), graph)


print(total)

f.close()
