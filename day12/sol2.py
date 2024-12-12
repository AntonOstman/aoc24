from collections import defaultdict
f = open("input")

lines = f.read().split("\n")[0:-1]

graph = defaultdict(set)
perimiters = 0

def get_adj(node, map):
    adj = []
    global perimiters

    if node[0] + 1 < len(lines[0]) and map[node[1]][node[0] + 1] == map[node[1]][node[0]]:
        adj.append((node[0] + 1, node[1]))
    else:
        perimiters += 1

    if node[1] + 1 < len(lines) and map[node[1] + 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] + 1))
    else:
        perimiters += 1

    if node[0] - 1 >= 0 and map[node[1]][node[0] - 1] == map[node[1]][node[0]]:
        adj.append((node[0] - 1, node[1]))
    else:
        perimiters += 1

    if node[1] - 1 >= 0 and map[node[1] - 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] - 1))
    else:
        perimiters += 1

    return adj

def dfs(node, map, visited, graph):
    global total, num_nodes, perimiters
    if node not in visited:
        visited.add(node)
        num_nodes += 1

        for neighour in get_adj(node, map):
            graph[node].add(neighour)
            dfs(neighour, map, visited, graph)

def calc_corners(nodes):
    corners = 0
    for node in nodes:
        for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:

            # outside
            if ((node[0] + dx, node[1]) not in nodes and (node[0], node[1] + dy) not in nodes):
                corners += 1

            # inside
            if ((node[0] + dx, node[1]) in nodes and (node[0], node[1] + dy) in nodes and (node[0] + dx, node[1] + dy) not in nodes):
                    corners += 1
    return corners

p1 = 0
p2 = 0

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if (x,y) in graph:
            continue
        num_nodes = 0
        seen = set()
        dfs((x,y), lines, seen, graph)
        sides = calc_corners(seen)
        p1 += len(seen) * perimiters
        p2 += num_nodes * sides
        perimiters = 0

print(p1)
print(p2)

f.close()
