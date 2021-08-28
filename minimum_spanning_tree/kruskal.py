#!/usr/bin/env python

class UnionFind():
    def __init__(self, n):
        self.par = [-1]*n
        self.siz = [1]*n

    def root(self, x):
        if self.par[x]==-1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        res = (self.root(x) == self.root(y))
        return res

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x==y:
            return False

        if self.siz[x] < self.siz[y]:
            x,y = (y,x)

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self,x):
        return self.siz[self.root(x)]

    def dump(self):
        print("***dump UnionFind***")
        print("     par:",self.par)
        print("     siz:",self.siz)

G = [[4,(4,1)],[3,(1,6)],[2,(4,6)],[9,(4,2)],[8,(1,3)],[6,(7,3)],[7,(6,7)],[5,(2,7)],[5,(3,0)],[10,(2,5)],[3,(7,0)],[6,(5,0)]]
G.sort()
M = len(G)
N = max([max(uv[1][0],uv[1][1]) for uv in G])+1
res = 0
uf = UnionFind(N)

for i in range(M):
    w = G[i][0]
    u = G[i][1][0]
    v = G[i][1][1]

    if uf.issame(u,v):
        #print("{} and {} are already in the same group".format(u,v))
        continue

    res += w
    uf.unite(u,v)

    #print(res)

print(res)
