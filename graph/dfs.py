#!/usr/bin/env python

G = [[5],[3,6],[5,7],[7,0],[1,2,6],[],[7],[0]]
N = len(G)
seen = [False]*N

def dfs(G,v):
    global seen
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G,next_v)
    return seen

for v in range(N):
    if seen[v]:
        continue
    dfs(G,v)

print(seen)

