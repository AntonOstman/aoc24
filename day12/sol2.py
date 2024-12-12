
from collections import defaultdict
f = open("test2")

lines = f.read().split("\n")[0:-1]

total = 0
graph = defaultdict(set)
# perimiter = defaultdict(set)
perimiter = set()
num_nodes = 0
perimiters = 0

def get_adj2(node, map):
    adj = []
    dirs = []

    # print(map)
    for n in map:
        if (n[0] + 1,n[1]) == node:
            adj.append(n)
            dirs.append("side")

        if(n[0],n[1] + 1) == node:
            adj.append(n)
            dirs.append("up")

        if (n[0] - 1,n[1]) == node:
            adj.append(n)
            dirs.append("side")

        if (n[0], n[1] - 1) == node:
            adj.append(n)
            dirs.append("up")

    # print('working on', node)
    # print('adjecent', adj)
    # print('dirs', dirs)
    return (adj, dirs)

def get_adj(node, map):
    adj = []
    global perimiters

    if node[0] + 1 < len(lines[0]) and map[node[1]][node[0] + 1] == map[node[1]][node[0]]:
        adj.append((node[0] + 1, node[1]))
    else:
        # perimiters += 1
        perimiter.add((node[0] + 1,node[1]))

    if node[1] + 1 < len(lines) and map[node[1] + 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] + 1))
    else:
        # perimiters += 1
        perimiter.add((node[0],node[1] + 1))

    if node[0] - 1 >= 0 and map[node[1]][node[0] - 1] == map[node[1]][node[0]]:
        adj.append((node[0] - 1, node[1]))
    else:
        # perimiters += 1
        perimiter.add((node[0] - 1,node[1]))

    if node[1] - 1 >= 0 and map[node[1] - 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] - 1))
    else:
        # perimiters += 1
        perimiter.add((node[0],node[1] - 1))

    # Add diagonals to perimiters

    if node[0] + 1 < len(lines[0]) and node[1] + 1 < len(lines) and map[node[1] + 1][node[0] + 1] == map[node[1]][node[0]]:
        pass
        # adj.append((node[0] + 1, node[1]))
    else:
        # perimiters += 1
        perimiter.add((node[0] + 1,node[1] + 1))

    if node[1] + 1 < len(lines) and node[0] - 1 >= 0 and map[node[1] + 1][node[0] - 1] == map[node[1]][node[0]]:
        pass
        # adj.append((node[0], node[1] + 1))
    else:
        # perimiters += 1
        perimiter.add((node[0] - 1,node[1] + 1))

    if node[1] - 1 >= 0 and node[0] + 1 < len(lines[0]) and map[node[1] - 1][node[0] + 1] == map[node[1]][node[0]]:
        # adj.append((node[0] + 1, node[1] - 1))
        pass
    else:
        # perimiters += 1
        perimiter.add((node[0] + 1,node[1] - 1))

    if node[1] - 1 >= 0 and node[0] - 1 >= 0 and map[node[1] - 1][node[0] - 1] == map[node[1]][node[0]]:
        # adj.append((node[0], node[1] - 1))
        pass
    else:
        # perimiters += 1
        perimiter.add((node[0] - 1,node[1] - 1))

    # print('working on', node)
    # print('adjecent', adj)
    # print('perimiters', perimiter)
    return adj

def dfs(node, map, visited, graph):
    global total, num_nodes, perimiters
    if node not in visited:
        visited.add(node)
        num_nodes += 1

        for neighour in get_adj(node, map):
            graph[node].add(neighour)
            dfs(neighour, map, visited, graph)

def dfs2(node, map, visited, graph, prev_dir):
    global perimiters
    # if prev_dir is None:
    #     perimiters += 1
    if node not in visited:
        # print('doing node', node)
        # if prev_dir is not None:
        #     visited.add(node)
        visited.add(node)
        # num_nodes += 1
        
        # neighours = get_adj2(node, graph);
        # print(map)
        neighours = get_adj2(node, map);
        # print(neighours)

        # print(neighours) 
        # print(neighours[0]) 
        # print(neighours[1]) 
        # print('node', node, 'has', len(neighours))
        # new_dirs = set()
        # new_dirs.add(prev_dir)
        for i in range(len(neighours[0])):
            neighour = neighours[0][i]
            # print('node', node, 'has adj', neighour)
            dir = neighours[1][i]
            # print('node and nourghjksd',node, neighour, dir)

            # graph[node].add(neighour)
            # print(dir, prev_dir)
            # if dir not in new_dirs:
                # new_dirs.add(dir)
                # perimiters += 1
                # print(node, neighour, prev_dir, dir)
            if prev_dir is None:
                perimiters += 1
                dfs2(neighour, map, visited, graph, dir)
                break
            if prev_dir != dir and neighour not in visited:
                perimiters += 1
                print(node, neighour, prev_dir, dir)
            dfs2(neighour, map, visited, graph, dir)

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if (x,y) in graph:
            continue
        num_nodes = 0
        perimiters = 0
        print('letter', letter)
        dfs((x,y), lines, set(), graph)
        start = next(iter(perimiter))
        print('start', start)
        print('perimiters', perimiter)
        dfs2(start, perimiter, set(), defaultdict(set), None)
        print('number of perimiters', len(perimiter), perimiters)
        # calculate_line_segments(perimiter) 
        # print(perimiters)
        perimiter = set()
        total += num_nodes * perimiters
        num_nodes = 0
        perimiters = 0


print(total)

f.close()
