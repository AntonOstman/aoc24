from collections import deque
f = open("input")

def get_next_pos(pos,dir, map):
    dx, dy = dir
    q = deque()
    q.append(pos)
    seen = set()
    while(len(q) > 0):
        seedx,seedy = q.pop()
        next = map[seedy+dy][seedx+dx]
        seen.add((seedx,seedy))

        if next == '[' and (seedx+dx, seedy+dy) not in seen:
            q.append((seedx+dx, seedy+dy))
            q.append((seedx+dx + 1, seedy+dy))
            assert map[seedy+dy][seedx +dx + 1] == ']'

        if next == ']' and (seedx+dx, seedy+dy) not in seen:
            q.append((seedx+dx, seedy+dy))
            q.append((seedx+dx - 1, seedy+dy))
            assert map[seedy+dy][seedx +dx - 1] == '['
        if next == '#':
            seen = set()
            break

    return seen

def get_robot(map):
    for y, line in enumerate(map):
        for x,letter in enumerate(line):
            if letter == '@':
                return (x,y)

total = 0
map, moves = f.read().split("\n\n")
map = map.split("\n")
map = [list(i) for i in map]
moves = moves.split("\n")[0:-1]
new_map = []
directions = {'<': (-1,0), 'v':(0,1), '>':(1,0), '^':(0,-1)}

for y, line in enumerate(map):
    new_map.append([])
    for x,letter in enumerate(line):
        if letter == '#':
            new_map[y].append('#')
            new_map[y].append('#')
        elif letter == '.':
            new_map[y].append('.')
            new_map[y].append('.')
        elif letter == 'O':
            new_map[y].append('[')
            new_map[y].append(']')
        elif letter == '@':
            new_map[y].append('@')
            new_map[y].append('.')

map = new_map

for i, line in enumerate(moves):
    for j, move in enumerate(line):
        dir = directions[move]
        dx,dy = dir
        seen = get_next_pos(get_robot(map), directions[move], map)

        while(seen):
            remove_pos = []
            for pos in seen:
                x,y = pos
                if map[y+dy][x+dx] == '.':
                    map[y+dy][x+dx] = map[y][x]
                    map[y][x] = '.'
                    remove_pos.append(pos)
                    break
            for i in remove_pos:
                seen.remove(i)

for y, row in enumerate(map):
    for x in range(len(row)):
        if map[y][x] == '[':
            total += y * 100 + x

print(total)

f.close()
