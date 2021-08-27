#!/usr/bin/env python

xs = [4,1,3,5,2]
print("before:",xs)

def swap(a,b):
   return (b,a) 

for i in range(len(xs)):
    if xs[i]==0:
        continue
    else:
        for j in range(i,len(xs)):
            if xs[j]<xs[j-1]:
                xs[j],xs[j-1] = swap(xs[j],xs[j-1])

print("after:",xs)
