from os import environ
import re
f = open("input")

lines = f.read().split("\n")[0:-1]

x = 0
current_position = 0
direction = 0


def get_position(lines):
    pos = (0,0)
    dir = 0
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "v":
                pos = (j,i)
                dir = 'S'
            elif letter == ">":
                pos = (j,i)
                dir = 'W'
            elif letter == "<":
                pos = (j,i)
                dir = 'E'
            elif letter == "^":
                pos = (j,i)
                dir = 'N'

    return pos, dir

def get_action(lines, pos, dir):
    new_dir = ''
    x,y = pos
    dx,dy = 0,0
    gone = False

    if dir == "N":
        if (y-1 < 0):
            gone = True
        elif lines[y-1][x] == '#':
            new_dir = 'E'
        else:
            dx,dy = 0,-1
    elif dir == "W":
        if (x-1 < 0):
            gone = True
        elif lines[y][x-1] == '#':
            new_dir = 'N'
        else:
            dx,dy = -1,0
    elif dir == "S":
        if (y+1 >= len(lines)):
            gone = True
        elif lines[y+1][x] == '#':
            new_dir = 'W'
        else:
            dx,dy = 0,1
    elif dir == "E":
        if (x+1 >= len(lines[y])):
            gone = True
        elif lines[y][x+1] == '#':
            new_dir = 'S'
        else:
            dx,dy = 1,0

    new_pos = (x + dx, y + dy)
    if new_dir == '':
        new_dir = dir

    return new_pos, new_dir, gone

def print_map(map):
    print(8*'-')
    for m in map:
        print(m)
    print(8*'-')

for line in lines:
    for letter in line:
        if letter == "X":
            x += 1

map = []

for i, line in enumerate(lines):
    map.append([])
    for j, letter in enumerate(line):
        map[i].append([letter])

pos, dir = get_position(lines)
gone = False

while(not gone):
    map[pos[1]][pos[0]] = ['X']
    pos, dir, gone = get_action(lines, pos, dir)

total = 0
for letters in map:
    for letter in letters:
        if letter[0] == 'X':
            total += 1

print(total)

f.close()
