#!/usr/bin/env python

G = [[5],[3,6],[5,7],[0,7],[1,2,6],[],[7],[0]]
N = len(G)
seen = [False]*N
order = []
def rec(G,v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        rec(G,next_v)
    order.append(v)


for v in range(N):
    if seen[v]:
        continue
    rec(G,v)

order.reverse()
print(order)




