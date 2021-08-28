#!/usr/bin/env python
import numpy as np
np.set_printoptions(suppress=True),
INF = 9999

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
N = len(G)

dp = np.ones((N,N))*INF

#### dp initialization ####
for v in range(N):
    for edge in G[v]:
        dp[v][edge.to] = edge.w

for v in range(N):
    dp[v][v] = 0
#### dp initialization end ####

#### Floyd warshall method ####
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
#### Floyd warshall method end ####

exist_negative_cycle = False
#### check if negative cycle exists ####
for v in range(N):
    if dp[v][v]<0:
        exist_negative_cycle = True
#### check end ####

if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    #### Show result #### 
    for i in range(N):
        print("***** distance from",i,"*****")
        for j in range(N):
            if j>0:
                print(" ",end='')
            if dp[i][j]<INF//2:
                print(int(dp[i][j]),end='')
            else:
                print("INF",end='')
        print()        

