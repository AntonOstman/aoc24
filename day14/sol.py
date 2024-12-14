import re
from collections import defaultdict
f = open("input")

lines = f.read().split("\n")[0:-1]

total = 0
graph = defaultdict(set)

side_x = 101
side_y = 103
# side_x = 11
# side_y = 7
def get_next_pos(px,py,vx,vy):
    dx = 0
    dy = 0

    if vx < 0:
        dx = -1
    if vy < 0:
        dy = -1
    if vx > 0:
        dx = 1
    if vy > 0:
        dy = 1

    for _ in range(abs(vx)):
        if px + dx >= side_x:
            px = 0
        elif px + dx < 0:
            px = side_x - 1
        else:
            px += dx

    for _ in range(abs(vy)):
        if py + dy < 0:
            py =  side_y - 1
        elif py + dy >= side_y:
            py = 0
        else:
            py += dy 
        # if py >= side_y:
        #     print('wetf')

    # print(px,py,vx,vy)
    # px += vx 
    # py += vy 

    return px,py,vx,vy

robot_id = defaultdict(tuple)

for y, line in enumerate(lines):
    state = re.search("\=(-?\d*),(-?\d*) v\=(-?\d*),(-?\d*)",line)
    if state is None:
        assert False, 'Could not parse state'

    px,py, vx,vy = state.groups()
    t = 100
    for i in range(t):
        px,py,vx,vy = get_next_pos(int(px),int(py),int(vx),int(vy))
    
    robot_id[len(robot_id)] = (px,py,vx,vy)

quad = defaultdict(int)

for id, robot in robot_id.items():
    px,py,vx,vy = robot
    if px >= side_x or py >= side_y:

        assert False, f"robot {id} large position, {px, py}"

    if px < side_x // 2 and py < side_y // 2:
        print('adding',px,py)
        quad[1] += 1
    elif px > side_x // 2 and py < side_y // 2:
        quad[2] += 1
    elif px < side_x // 2 and py > side_y // 2:
        print('adding',px,py)
        quad[3] += 1
    elif px > side_x // 2 and py > side_y // 2:
        quad[4] += 1
    else:
        print('outside',px,py)

total = 1

for _, num in quad.items():
    print(quad)
    total *= num


print(robot_id)

print(total)

f.close()
