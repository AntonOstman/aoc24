from collections import defaultdict
f = open("input")

def get_next_pos(pos,dir, map):
    px,py = pos
    dx, dy = dir
    moved_locations = []
    
    running = True
    while(running):

        next = map[py+dy][px+dx]

        if next == '#':
            moved_locations = []
            running = False
        elif next == '.':
            running = False
            moved_locations.append((px, py))
        else:
            moved_locations.append((px, py))

        px,py = px+dx,py+dy

    return moved_locations

total = 0
map, moves = f.read().split("\n\n")
map = map.split("\n")
map = [list(i) for i in map]
moves = moves.split("\n")[0:-1]
directions = {'<': (-1,0), 'v':(0,1), '>':(1,0), '^':(0,-1)}

dude_pos = (0,0)

for y, line in enumerate(map):
    for x,letter in enumerate(line):
        if letter == '@':
            dude_pos = (x,y)


for i, line in enumerate(moves):
    for j, move in enumerate(line):
        dir = directions[move]
        moved_locations = get_next_pos(dude_pos, directions[move], map)
        dx,dy = dir

        for moved_location in moved_locations[::-1]:
            x,y = moved_location
            map[y+dy][x+dx] = map[y][x]

        if len(moved_locations) > 0:
            map[dude_pos[1]][dude_pos[0]] = '.'
            dude_pos = (dude_pos[0] + dx, dude_pos[1] + dy)

for y, row in enumerate(map):
    for x in range(len(row)):
        if map[y][x] == 'O':
            total += y * 100 + x

print(total)

f.close()
