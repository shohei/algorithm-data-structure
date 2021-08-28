#!/usr/bin/env python

G = [[1,3],[0,4,2],[1],[0,4],[1,3]]
N = len(G)
color = [-1]*N

def dfs(G,v,cur=0):
    color[v] = cur
    for next_v in G[v]:
        if color[next_v]!=-1:
            if color[next_v]==cur:
                return false
            continue
        if dfs(G,next_v,1-cur)==False:
            return False
    
    return True

is_bipartite = True
for v in range(N):
    if color[v]!=-1:
        continue
    if dfs(G,v)==False:
        is_bipartite = False

print(is_bipartite)
