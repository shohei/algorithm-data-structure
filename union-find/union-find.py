#!/usr/bin/env python

class UnionFind():
    def __init__(self, n):
        self.par = [-1]*n
        self.siz = [1]*7 

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

uf = UnionFind(7)
print("initialize")
uf.dump()
print("unite 1 and 2")
uf.unite(1,2)
uf.dump()
print("unite 2 and 3")
uf.unite(2,3)
uf.dump()
print("unite 5 and 6")
uf.unite(5,6)
uf.dump()
#print(uf.issame(1,3))
#print(uf.issame(2,5))
print("unite 1 and 6")
uf.unite(1,6)
uf.dump()
#print(uf.issame(2,5))

