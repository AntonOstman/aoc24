import re
import subprocess
from collections import defaultdict
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
from sklearn.cluster import DBSCAN
import math

# The solutions relies on clustering and checking when there is little noise
# So you need to look at the rendered images and if there is no tree you might need
# to tune the parameters of the clustering algo

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
    return px,py,vx,vy



f = open("input")

matplotlib.use('agg')
lines = f.read().split("\n")[0:-1]
subprocess.run("rm time*", shell=True)

total = 0
graph = defaultdict(set)

side_x = 101
side_y = 103

robot_id = defaultdict(tuple)

t = 10000

density_x = float('inf')
density_y = float('inf')

for i in range(t + 2):
    image = np.zeros([side_x, side_y])
    for id, line in enumerate(lines):
        if id not in robot_id:

            state = re.search("\=(-?\d*),(-?\d*) v\=(-?\d*),(-?\d*)",line)
            if state is None:
                assert False, 'Could not parse state'

            px,py, vx,vy = state.groups()
            robot_id[id] = (int(px),int(py),int(vx),int(vy))
            image[int(px),int(py)] = 1
        else:
            px,py,vx,vy = get_next_pos(*robot_id[id])
            robot_id[id] = (px, py, vx, vy)
            image[px,py] = 1

    # eps 1.1 should be enough so 4 but not 8 connectivity is considered
    clusters = DBSCAN(eps = 2, min_samples = 30).fit(image)
    labels = clusters.labels_

    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = list(labels).count(-1)

    if n_noise < 30:
        plt.imshow(image)
        plt.title(f"{i}")
        plt.savefig(f"time{i}_n{n_noise}_clusters{n_clusters}")
        print(f"saving time {i}")

quad = defaultdict(int)

for id, robot in robot_id.items():
    px,py,vx,vy = robot
    if px >= side_x or py >= side_y:

        assert False, f"robot {id} large position, {px, py}"

    if px < side_x // 2 and py < side_y // 2:
        quad[1] += 1
    elif px > side_x // 2 and py < side_y // 2:
        quad[2] += 1
    elif px < side_x // 2 and py > side_y // 2:
        # print('adding',px,py)
        quad[3] += 1
    elif px > side_x // 2 and py > side_y // 2:
        quad[4] += 1

total = 1

for _, num in quad.items():
    total *= num


print(total)

f.close()
