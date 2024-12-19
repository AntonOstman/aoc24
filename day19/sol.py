from itertools import product 
import functools
import sys
sys.setrecursionlimit(100000000)

f = open("input")

patterns, designs = f.read()[:-1].split("\n\n")
patterns = patterns.split(", ")
designs = designs.split("\n")

@functools.cache
def get_patterns(design):
    global patterns
    if not design:
        return 1

    possibilites = 0
    for pattern in patterns:
        if design.startswith(pattern):
            possibilites += get_patterns(design[len(pattern):])

    return possibilites

pos = []
for i, design in enumerate(designs):
    pos.append(get_patterns(design))

print('Part 1', sum([i > 0 for i in pos]))
print('Part 2', sum(pos))

# ans = list(product([j for j in i for i in patterns]))
