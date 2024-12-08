import itertools
import numpy as np
from collections import defaultdict

f = open("input")

lines = f.read().split("\n")[0:-1]
positions = defaultdict(list)
antinodes = list()
map_y = len(lines)
map_x = len(lines[0])

def inside_map(pos):
    global map_x
    global map_y

    return pos[0] >= 0 and pos[0] < map_x and pos[1] >= 0 and pos[1] < map_y

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter.isdigit() or letter.isalpha():
            positions[letter].append(np.array([x,y]))

for letter in positions:

    for i, pos in enumerate(positions[letter]):
        for j in range(i + 1, len(positions[letter])):
            poses = positions[letter]

            dist = np.array([0,0])
            step = 0

            # vector goes from j to i
            while(inside_map(poses[i] + dist)):
                antinodes.append(poses[i] + dist)
                step += 1
                dist = step * (poses[i] - poses[j])

            dist = np.array([0,0])
            step = 0

            while(inside_map(poses[j] - dist)):
                antinodes.append(poses[j] - dist)
                step += 1
                dist = step * (poses[i] - poses[j])

antinodes = set([(int(x), int(y)) for x,y in antinodes])

print(len(antinodes))

f.close()
