#!/usr/bin/env python

def heapify(a,i,N):
    child1 = 2*i+1
    if child1 >= N:
        return
    if (child1+1) < N and a[child1+1]>a[child1]:
        child1 += 1
    if a[child1] <= a[i]:
        return
    a[i],a[child1] = (a[child1],a[i])
    heapify(a,child1,N)

def heapsort(a):
    N = len(a)
    for i in reversed(range(N//2)):
        heapify(a,i,N)
    for i in reversed(range(N)):
        a[0],a[i] = (a[i],a[0])
        heapify(a,0,i)
    return a


xs = [10,12,15,3,8,17,4,1]
print("before:",xs)
xs=heapsort(xs)
print("after:",xs)


