#!/usr/bin/env python
import pdb

class Edge():
    def __init__(self, rev, frm, to, cap):
        self.rev = rev
        self.frm = frm
        self.to = to
        self.cap = cap

class Graph():
    def __init__(self, N=0):
        self.lst = [[]]*N

    def size(self):
        return len(self.lst)

    def redge(self, edge):
        return self.lst[edge.to][edge.rev]

    def run_flow(self, edge, f):
        edge.cap -= f
        self.redge(edge).cap += f
        return [edge.cap, self.redge(edge).cap]
    
    def addedge(self, frm, to, cap):
        fromrev = len(self.lst[frm])
        torev = len(self.lst[to])
        self.lst[frm].append(Edge(torev,frm,to,cap))
        self.lst[to].append(Edge(fromrev,to,frm,0))

class FordFulkerson():
    INF = 9999
    seen=[]

    def __init__(self):
        pass

    def fodfs(self, G, v, t, f):
        self.G = G

        if v==t:
            return f

        self.seen[v] = True

        for i,e in enumerate(self.G.lst[v]):
            if self.seen[e.to]:
                continue
            if e.cap==0:
                continue

            self.flow = self.fodfs(self.G, e.to, t, min(f,e.cap))

            if self.flow==0:
                continue

            self.G.lst[v][i].cap, self.G.lst[e.to][e.rev].cap = self.G.run_flow(e, self.flow)

            return self.flow

        return 0

    def solve(self, G, s, t):
        self.res = 0

        while True:
            self.seen = [False]*G.size()
            self.flow = self.fodfs(G, s, t, self.INF)

            if self.flow==0:
                return self.res

            self.res += self.flow

        return 0

G = [[0,1,5],[0,3,5],[1,3,37],[1,2,4],[3,2,3],[3,4,9],[2,4,56],[2,5,7],[4,5,2]]
N = max([max(uv[0],uv[1]) for uv in G])+1 #Number of vertices
M = len(G) #Number of edges
graph = Graph(N)
for g in G:
    frm = g[0]
    to = g[1] 
    cap = g[2]
    graph.addedge(frm,to,cap)

ff = FordFulkerson()        
s = 0
t = N-1
print(ff.solve(graph,s,t))

