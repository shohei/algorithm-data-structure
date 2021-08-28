#!/usr/bin/env python

G = [[1,2,3],[2,5],[4],[4,7],[6],[6],[7],[]]
N = len(G) 
seen = [False]*N

def dfs(G,s):
    seen[s] = True 

    for x in G[s]:
        if seen[x]:
            continue
        dfs(G,x)

s = 2
t = 7
dfs(G,s)
print(seen[t])

