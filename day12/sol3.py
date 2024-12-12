from collections import defaultdict
f = open("test")

lines = f.read().split("\n")[0:-1]

total = 0
graph = defaultdict(set)
perimiter = defaultdict(set)
num_nodes = 0

def get_adj(node, map):
    adj = []

    if node[0] + 1 < len(lines[0]) and map[node[1]][node[0] + 1] == map[node[1]][node[0]]:
        adj.append((node[0] + 1, node[1]))

    if node[1] + 1 < len(lines) and map[node[1] + 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] + 1))

    if node[0] - 1 >= 0 and map[node[1]][node[0] - 1] == map[node[1]][node[0]]:
        adj.append((node[0] - 1, node[1]))

    if node[1] - 1 >= 0 and map[node[1] - 1][node[0]] == map[node[1]][node[0]]:
        adj.append((node[0], node[1] - 1))

    return adj

def check_segments(nodes):

    up_seg = set()
    down_seg = set()
    left_seg = set()
    right_seg = set()
    for node in nodes:
        # If this node is fully sournded by other, continue
        if (node[0] + 1, node[1]) in nodes and (node[0] - 1, node[1]) in nodes and (node[0], node[1] + 1) in nodes and (node[0], node[1] - 1) in nodes:
            continue
        up_left = None
        up_right = None

        for i in range(len(nodes)):
            # UP WALL
            # print((node[0] + i, node[1]) in nodes, (node[0] + i, node[1] - 1) not in nodes)
            # print((node[0] + i, node[1]), (node[0] + i, node[1] - 1))
            if (node[0] - 1, node[1]) in nodes:
                continue
            
            if (node[0] + i, node[1]) in nodes and (node[0] + i, node[1] - 1) not in nodes:
                up_right = (node[0] + i, node[1])
            if (node[0] - i, node[1]) in nodes and (node[0] - i, node[1] - 1) not in nodes:
                up_left = (node[0] - i, node[1])

        if up_left is None and up_right is None:
            pass
        elif up_right is None:
            up_seg.add((up_left,node))
        elif up_left is None:
            up_seg.add((node,up_right))
        else:
            up_seg.add((up_left,up_right))

        down_left = None
        down_right = None
        for i in range(len(nodes)):
            if (node[0] + 1, node[1]) in nodes:
                continue
            # DOWN WALL
            if (node[0] + i, node[1]) in nodes and (node[0] + i, node[1] + 1) not in nodes:
                down_right = (node[0] + i, node[1])
            if (node[0] - i, node[1]) in nodes and (node[0] - i, node[1] + 1) not in nodes:
                down_left = (node[0] - i, node[1])

        if down_left is None and down_right is None:
            pass
        elif down_right is None:
            down_seg.add((down_left,node))
        elif down_left is None:
            down_seg.add((node,down_right))
        else:
            down_seg.add((down_left,down_right))

        left_up  = None
        left_down = None
        for i in range(len(nodes)):
            if (node[0], node[1] - 1) in nodes:
                continue
            # LEFT WALL
            if (node[0], node[1] + i) in nodes and (node[0] - 1, node[1] + i) not in nodes:
                left_up = (node[0], node[1] + i)
            if (node[0], node[1] - i) in nodes and (node[0] - 1, node[1] - i) not in nodes:
                left_down = (node[0], node[1] - i)

        if left_up is None and left_down is None:
            pass
        elif left_down is None:
            left_seg.add((left_up,node))
        elif left_up is None:
            left_seg.add((node,left_down))
        else:
            left_seg.add((left_up, left_down))

        right_up = None
        right_down = None
        for i in range(len(nodes)):
            if (node[0], node[1] + 1) in nodes:
                continue
            # RIGHT WALL
            if (node[0], node[1] + i) in nodes and (node[0] + 1, node[1] + i) not in nodes:
                right_up = (node[0], node[1] + i)
            if (node[0], node[1] - i) in nodes and (node[0] + 1, node[1] - i) not in nodes:
                right_down = (node[0], node[1] - i)

        if right_up is None and right_down is None:
            pass
        elif right_down is None:
            right_seg.add((right_up,node))
        elif right_up is None:
            right_seg.add((node,right_down))
        else:
            right_seg.add((right_up,right_down))

        # up_seg.add((up_left, up_right))
        # down_seg.add((down_left, down_right))
        # left_seg.add((left_up, left_down))
        # right_seg.add((right_up, right_down))

    all_segments = up_seg.union(down_seg.union(left_seg.union(right_seg)))

    perimiters = 0
    checked = set()

    print('up_seg',up_seg)
    print('down_seg',down_seg)
    print('left_seg',left_seg)
    print('right_seg',right_seg)
    #
    for _ in all_segments:
        perimiters += 1
    # for segment in up_seg:
    #     checked.add(segment)
    #     perimiters += 1
    # for segment in down_seg:
    #     checked.add(segment)
    #     perimiters += 1
    # for segment in left_seg:
    #     checked.add(segment)
    #     perimiters += 1
    # for segment in right_seg:
    #     checked.add(segment)
    #     perimiters += 1

    return perimiters



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
        bunch = set()
        dfs((x,y), lines, bunch, graph)
        perimiters += check_segments(bunch)
        total += num_nodes * perimiters
        num_nodes = 0
        perimiters = 0

print(total)

f.close()
