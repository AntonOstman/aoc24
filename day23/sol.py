from collections import defaultdict
from itertools import combinations
f = open("test")

lines = f.read().strip().split("\n")

connections = defaultdict(set)

for line in lines:
    c1, c2 = line.split("-")
    connections[c1].add(c2)
    connections[c2].add(c1)

true_combs = set()
for pc1, conn in connections.items():
    if pc1[0] == 't':
        for pc2 in conn:
            interconnected = connections[pc1].intersection(connections[pc2])
            for third in interconnected:
                # frozenset is a immutable set, making it hashable.
                # This means that there will be no duplicates e.g. (1,2,3) and (3,2,1)
                true_combs.add(frozenset((pc1,pc2,third)))

print(len(true_combs))




f.close()
