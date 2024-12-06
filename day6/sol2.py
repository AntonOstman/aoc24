from threading import Lock
from multiprocessing import Process, Pipe
import time
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

def get_action(lines, pos, dir, obs_pos):
    new_dir = ''
    x,y = pos
    dx,dy = 0,0
    gone = False

    if dir == "N":
        if (y-1 < 0):
            gone = True
        elif lines[y-1][x] == '#':
            new_dir = 'E'
        elif (x, y-1) == obs_pos:
            new_dir = 'E'
        else:
            dx,dy = 0,-1
    elif dir == "W":
        if (x-1 < 0):
            gone = True
        elif lines[y][x-1] == '#':
            new_dir = 'N'
        elif (x-1, y) == obs_pos:
            new_dir = 'N'
        else:
            dx,dy = -1,0
    elif dir == "S":
        if (y+1 >= len(lines)):
            gone = True
        elif lines[y+1][x] == '#':
            new_dir = 'W'
        elif (x, y+1) == obs_pos:
            new_dir = 'W'
        else:
            dx,dy = 0,1
    elif dir == "E":
        if (x+1 >= len(lines[y])):
            gone = True
        elif lines[y][x+1] == '#':
            new_dir = 'S'
        elif (x+1, y) == obs_pos:
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
new_lines = []

for i, line in enumerate(lines):
    map.append([])
    new_lines.append([])
    for j, letter in enumerate(line):
        # print(letter)
        map[i].append([letter])
        new_lines[i].append([letter])

total = 0

def search(p, obs_x, obs_y): 
    global total
    prev_states = set()
    pos, dir = get_position(lines)
    gone = False
    print('current', obs_x, obs_y)
    while(not gone):
        if (pos, dir) in prev_states:
            p.send(1)
            p.close()
            return
        prev_states.add((pos, dir))
        pos, dir, gone = get_action(lines, pos, dir, (obs_x, obs_y))

    p.send(0)
    p.close()
    return

pool = 20
start_time = time.time()
for obs_y in range(len(lines)):
    cur_pool = 0
    threads = []
    for obs_x in range(0,len(lines[0])):
        parent, child = Pipe()
        th = Process(target=search, args=(child, obs_x, obs_y))
        th.start()
        threads.append((parent,th))

    for pipe,process in threads:
        total += pipe.recv()
        process.join()

print('time', time.time() - start_time)
print(total)

f.close()
