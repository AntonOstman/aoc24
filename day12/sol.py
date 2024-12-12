from collections import defaultdict
f = open("input")

lines = f.read().split("\n")[0:-1]

total = 0
graph = defaultdict(set)
perimiter = defaultdict(set)
num_nodes = 0
perimiters = 0

def get_adj(node, map):
    adj = []
    global perimiters

    if node[0] + 1 < len(lines[0]) and map[node[1]][node[0] + 1] == map[node[1]][node[0]]:
        adj.append((node[0] + 1, node[1]))
    else:
        perimiters += 1
        # perimiter[map[node[1]][node[0]]].add((node[0] + 1,node[1]))

    if node[1] + 1 < len(lines) and map[node[1] + 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] + 1))
    else:
        perimiters += 1
        # perimiter[map[node[1]][node[0]]].add((node[0],node[1] + 1))

    if node[0] - 1 >= 0 and map[node[1]][node[0] - 1] == map[node[1]][node[0]]:
        adj.append((node[0] - 1, node[1]))
    else:
        perimiters += 1
        # perimiter[map[node[1]][node[0]]].add((node[0] - 1,node[1]))

    if node[1] - 1 >= 0 and map[node[1] - 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] - 1))
    else:
        perimiters += 1
        # perimiter[map[node[1]][node[0]]].add((node[0],node[1] - 1))

    return adj

def dfs(node, map, visited, graph):
    global total, num_nodes, perimiters
    if node not in visited:
        visited.add(node)
        num_nodes += 1

        for neighour in get_adj(node, map):
            graph[node].add(neighour)
            dfs(neighour, map, visited, graph)


for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if (x,y) in graph:
            continue
        num_nodes = 0
        perimiters = 0
        dfs((x,y), lines, set(), graph)
        print(num_nodes)
        total += num_nodes * perimiters
        num_nodes = 0
        perimiters = 0



print(total)

f.close()
