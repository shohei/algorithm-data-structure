#!/usr/bin/env python

def bfs(G,s):
    N = len(G)
    dist = [-1]*N
    que = []

    dist[0] = 0 
    que.append(0)

    while(que!=[]):
        #queue -> breadth-first search
        v = que[0]
        que = que[1:] 
    
        for x in G[v]:
            if (dist[x]!=-1):
                continue
            dist[x] = dist[v] + 1 
            que.append(x)
    return dist 

G = [(1,4,2),(0,3,8),(0,5),(1,7,8),(0,8),(2,6,8),(5,7),(3,6),(1,3,4,5)]
print(bfs(G,0))

