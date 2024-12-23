from copy import copy
from collections import defaultdict
from itertools import combinations
f = open("input")

lines = f.read().strip().split("\n")

connections = defaultdict(set)

for line in lines:
    c1, c2 = line.split("-")
    connections[c1].add(c2)
    connections[c2].add(c1)

# Use the bonkerbosh algo, this gives all cliques in a graph.
# A clique is subset of a graph which is a fully connected.
def bronkerbosh(R,P,X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bronkerbosh(
                R.union({v}),
                P.intersection(graph[v]),
                X.intersection(graph[v]),
                graph
                )
        X.add(v)

cliques = list(bronkerbosh(set(), set(connections.keys()), set(), connections))
largest_clique = set() 
for clique in cliques:
    if len(clique) > len(largest_clique):
        largest_clique = clique

print(",".join(sorted(list(largest_clique))))


f.close()
