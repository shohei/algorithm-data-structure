#!/usr/bin/env python

class Edge():
    def __init__(self,to,w):
        self.to = to
        self.w = w

G = [[Edge(1,3),Edge(3,100)],
     [Edge(2,50),Edge(3,57),Edge(4,-4)],
     [Edge(3,-10),Edge(4,-5),Edge(5,100)],
     [Edge(1,-5)],
     [Edge(2,57),Edge(3,25),Edge(5,8)],
     []]

def chmin(a,b):
    if a<=b:
        return False 
    else:
        return True 

INF = 9999
exist_negative_cycle = False
N = len(G)
dist = [INF]*N
s = 0
dist[s] = 0

for i in range(N):
    update = False
    for v in range(N):
        if dist[v]==INF:
            continue
        for edge in G[v]:
            if (chmin(dist[edge.to], dist[v]+edge.w)):
                update = True
                dist[edge.to] = dist[v]+edge.w

    if update==False:
        break

    if i==N-1 and update==True:
        exist_negative_cycle = True

if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for v in range(N):
        if dist[v]<INF:
            print(dist[v])
        else:
            "INF"

